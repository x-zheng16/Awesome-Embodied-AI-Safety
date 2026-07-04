-- D1 schema for the Awesome-Embodied-AI-Safety project page backend.
-- Apply with:  wrangler d1 execute embodied-ai-safety --remote --file=./schema.sql
--       local: wrangler d1 execute embodied-ai-safety --local  --file=./schema.sql

-- Visitor counter: a single running total (page views), incremented per JS-gated load.
CREATE TABLE IF NOT EXISTS views (
  id    TEXT    PRIMARY KEY,
  count INTEGER NOT NULL DEFAULT 0
);

-- Seed the total so the live number never drops below what the site shows today.
-- Baseline = VISITOR_BASELINE(65) + last-known busuanzi site_pv floor(226) = 291.
-- Adjust to the busuanzi value shown at deploy time if it has moved.
INSERT OR IGNORE INTO views (id, count) VALUES ('total', 291);

-- HuggingFace-style paper voting. One row per (paper, anonymous client) = one upvote.
-- The composite primary key enforces one vote per client per paper (server-side dedup);
-- the client_id is an anonymous UUID the frontend mints and keeps in localStorage.
CREATE TABLE IF NOT EXISTS votes (
  paper_id   TEXT    NOT NULL,
  client_id  TEXT    NOT NULL,
  created_at INTEGER NOT NULL,
  PRIMARY KEY (paper_id, client_id)
);

CREATE INDEX IF NOT EXISTS idx_votes_paper ON votes (paper_id);
