// Backend API for the Awesome-Embodied-AI-Safety project page.
//
// Deployed as a Cloudflare Worker on its OWN host (e.g. embodied-ai-safety-api.<sub>.workers.dev).
// The GitHub Pages site (https://x-zheng16.github.io/Awesome-Embodied-AI-Safety/) fetches it
// from the browser; the site URL itself never changes. CORS below allows exactly the Pages origin.
//
// Endpoints:
//   POST /api/views          -> increment + return { views }        (called once per JS-gated page load)
//   GET  /api/views          -> read-only  { views }
//   GET  /api/votes          -> { counts: { "<paperId>": n, ... } } (all papers with >=1 vote)
//   POST /api/vote           -> toggle a vote; body { paperId, clientId } -> { paperId, count, voted }
//   GET  /api/health | /     -> { ok: true, ... }

const ALLOWED_ORIGINS = new Set([
  'https://x-zheng16.github.io',
]);

// Allow the Pages origin, plus localhost during `wrangler dev`. Anything else is pinned
// back to the canonical Pages origin (a non-browser caller gets a usable, if mismatched, header).
function allowOrigin(origin) {
  if (origin && (ALLOWED_ORIGINS.has(origin) || /^http:\/\/localhost(:\d+)?$/.test(origin))) {
    return origin;
  }
  return 'https://x-zheng16.github.io';
}

function corsHeaders(origin) {
  return {
    'Access-Control-Allow-Origin': allowOrigin(origin),
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
    'Vary': 'Origin',
  };
}

function json(data, origin, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8', ...corsHeaders(origin) },
  });
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin');

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: corsHeaders(origin) });
    }

    const url = new URL(request.url);
    const path = url.pathname.replace(/\/+$/, '') || '/';
    const method = request.method;

    try {
      // --- visitor counter ---
      if (path === '/api/views' && method === 'POST') {
        const row = await env.DB
          .prepare("INSERT INTO views (id, count) VALUES ('total', 1) " +
                   "ON CONFLICT(id) DO UPDATE SET count = count + 1 RETURNING count")
          .first();
        return json({ views: row ? row.count : 1 }, origin);
      }

      if (path === '/api/views' && method === 'GET') {
        const row = await env.DB
          .prepare("SELECT count FROM views WHERE id = 'total'")
          .first();
        return json({ views: row ? row.count : 0 }, origin);
      }

      // --- paper voting ---
      if (path === '/api/votes' && method === 'GET') {
        const { results } = await env.DB
          .prepare('SELECT paper_id, COUNT(*) AS c FROM votes GROUP BY paper_id')
          .all();
        const counts = {};
        for (const r of results) counts[r.paper_id] = r.c;
        return json({ counts }, origin);
      }

      if (path === '/api/vote' && method === 'POST') {
        const body = await request.json().catch(() => ({}));
        const paperId = String(body.paperId || '').slice(0, 200);
        const clientId = String(body.clientId || '').slice(0, 64);
        if (!paperId || !clientId) {
          return json({ error: 'paperId and clientId are required' }, origin, 400);
        }

        const existing = await env.DB
          .prepare('SELECT 1 FROM votes WHERE paper_id = ? AND client_id = ?')
          .bind(paperId, clientId)
          .first();

        let voted;
        if (existing) {
          await env.DB
            .prepare('DELETE FROM votes WHERE paper_id = ? AND client_id = ?')
            .bind(paperId, clientId)
            .run();
          voted = false;
        } else {
          await env.DB
            .prepare('INSERT INTO votes (paper_id, client_id, created_at) VALUES (?, ?, ?)')
            .bind(paperId, clientId, Date.now())
            .run();
          voted = true;
        }

        const row = await env.DB
          .prepare('SELECT COUNT(*) AS c FROM votes WHERE paper_id = ?')
          .bind(paperId)
          .first();
        return json({ paperId, count: row ? row.c : 0, voted }, origin);
      }

      // --- health / root ---
      if (path === '/' || path === '/api' || path === '/api/health') {
        return json({
          ok: true,
          service: 'embodied-ai-safety-api',
          endpoints: ['POST /api/views', 'GET /api/views', 'GET /api/votes', 'POST /api/vote'],
        }, origin);
      }

      return json({ error: 'not found' }, origin, 404);
    } catch (err) {
      return json({ error: 'server error', detail: String(err && err.message || err) }, origin, 500);
    }
  },
};
