# embodied-ai-safety-api

Self-hosted backend for the [Awesome-Embodied-AI-Safety](https://x-zheng16.github.io/Awesome-Embodied-AI-Safety/)
project page: a durable **visitor counter** (replaces the flaky busuanzi JSONP) and
**HuggingFace-style paper voting**. Runs as a single Cloudflare Worker backed by D1 (SQLite).

## Architecture

The project page stays on GitHub Pages at its current URL — **nothing about the site
address changes**. This Worker is a *separate* API host that the page's JavaScript calls
from the browser:

```
Browser ──GET Pages──▶ x-zheng16.github.io/Awesome-Embodied-AI-Safety/   (unchanged)
   │
   └──fetch (CORS)──▶ embodied-ai-safety-api.<subdomain>.workers.dev/api/...
                          │
                          └── D1 (SQLite): views + votes tables
```

CORS in `src/index.js` allows exactly the Pages origin (`https://x-zheng16.github.io`),
plus `localhost` for local dev.

## API

| Method + path      | Body                       | Returns                                  |
| ------------------ | -------------------------- | ---------------------------------------- |
| `POST /api/views`  | —                          | `{ views }` (increments, then reads)     |
| `GET  /api/views`  | —                          | `{ views }` (read-only)                  |
| `GET  /api/votes`  | —                          | `{ counts: { "<paperId>": n, ... } }`    |
| `POST /api/vote`   | `{ paperId, clientId }`    | `{ paperId, count, voted }` (toggles)    |
| `GET  /api/health` | —                          | `{ ok: true, ... }`                      |

Voting is one upvote per anonymous client per paper — the `(paper_id, client_id)` primary
key enforces dedup server-side. `clientId` is a UUID the frontend mints once and keeps in
`localStorage`; `POST /api/vote` toggles (vote / un-vote) and returns the authoritative count.

## Deploy (one-time)

Prereqs: a Cloudflare account and Node. From this `worker/` directory:

```bash
pnpm install                       # installs wrangler
pnpm exec wrangler login           # opens browser once to authorize

# 1. create the D1 database, then paste the printed database_id into wrangler.toml
pnpm run db:create

# 2. apply the schema to the REMOTE database (creates tables + seeds the view baseline)
pnpm run db:schema

# 3. deploy the Worker — note the printed https://embodied-ai-safety-api.<sub>.workers.dev URL
pnpm run deploy
```

Then wire the frontend: set the API base URL in `docs/index.html` (see **Frontend integration**)
to the deployed `workers.dev` URL and push. GitHub Pages redeploys automatically.

### View-count baseline

`schema.sql` seeds `views.total = 291` (the number the site shows today:
`VISITOR_BASELINE 65` + last busuanzi `site_pv` floor `226`). If busuanzi has moved by
deploy time, set it to the current displayed value so the count never drops:

```bash
pnpm exec wrangler d1 execute embodied-ai-safety --remote \
  --command "UPDATE views SET count = <current-displayed-number> WHERE id = 'total'"
```

## Local test (no deploy, no account needed)

```bash
pnpm install
pnpm run db:schema:local           # applies schema to a LOCAL sqlite
pnpm run dev                       # serves at http://localhost:8787
```

Smoke-test in another shell:

```bash
curl -s -X POST http://localhost:8787/api/views
curl -s       http://localhost:8787/api/votes
curl -s -X POST http://localhost:8787/api/vote \
  -H 'content-type: application/json' \
  -d '{"paperId":"demo","clientId":"test-client-1"}'
```

## Frontend integration (lands with the site redeploy)

Add near the top of the page `<script>`:

```js
const API_BASE = 'https://embodied-ai-safety-api.<sub>.workers.dev';
// one anonymous id per browser, for vote dedup
const CLIENT_ID = (() => {
  let id = localStorage.getItem('eais_client');
  if (!id) { id = crypto.randomUUID(); localStorage.setItem('eais_client', id); }
  return id;
})();
```

- **Visitor count** replaces the busuanzi block: `fetch(API_BASE + '/api/views', {method:'POST'})`
  on load, render `.views` into `#visitorNum`, and keep the last value in `localStorage` as the
  never-blank fallback (same resilience the current stat has).
- **Voting**: on load `fetch(API_BASE + '/api/votes')` and paint counts onto each paper's
  upvote button; on click `POST /api/vote` with `{paperId, clientId: CLIENT_ID}`, update the
  button from the returned `{count, voted}`, and mirror `voted` into a local `Set` for the
  highlight state.

`paperId` should be a stable per-paper string (e.g. the arXiv id, or a slug of the title) that
matches whatever id the paper rows already carry in `papers.json`.

## Cost / limits

Cloudflare free tier: 100k Worker requests/day and 5M D1 rows-read + 100k rows-written/day —
far above this site's traffic. No paid plan required.

## Hardening (future, not in v1)

- Rate-limit `/api/vote` and `/api/views` per IP (e.g. hash `CF-Connecting-IP` into a KV/D1
  bucket) to blunt scripted inflation. v1 relies on `clientId` dedup only, which is adequate
  for a research site.
