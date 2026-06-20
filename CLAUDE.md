# Riot! Riot! — Band Website

Single-page static website for the Paramore cover band **Riot! Riot!** (Florianópolis, SC, Brazil).
Audience: show producers/bookers + fans. **Language: Brazilian Portuguese only.**

## Live & hosting
- **Live:** https://riotriot.com.br (custom domain) · https://riotriot.endy-silveira.workers.dev (Cloudflare default, still works)
- **Host:** Cloudflare Pages connected to this GitHub repo (`endy-s/riotriot`). **Every `git push` to `main` auto-deploys** (~1 min). There is no build step.
- Future: custom domain `riotriot.com.br` (not set up yet — add via Cloudflare custom domain + DNS, no code change).

## Stack & files
- Plain **static HTML + CSS + vanilla JS**. No framework, no bundler, no build.
- `index.html` — the whole page (all content/copy).
- `rider.html` — unlisted technical rider served at `/rider` (`noindex`, no menu link); print-to-PDF. **Keep its content in sync with the site's Técnico section — sources, captação wording, stage info; if they conflict, the most-recently-edited file wins. Intentional exception: the rider's Input List uses the engineer-standard *drums-first* channel order (1–7 drums · 8 bass · 9–10 guitars · 11–13 vocals), while the site summary uses a *vocals-first* presentation order. Keep wording in sync, but NOT the row order.**
- `styles.css` — all styles (brand vars in `:root`).
- `main.js` — nav hamburger toggle, Técnico segmented control (Ilustrado/Técnico), Ao Vivo lightbox with prev/next (arrows + ←/→ keys + Esc). Smooth scroll is CSS (`scroll-behavior`).
- `assets/img/` — photos & logos. `assets/stageplot.svg` — technical stage plot. `stageplot.py` — generator for that SVG.
- `favicon.ico` (root, multi-size 16/32/48 from `favicon.png`) + `.well-known/security.txt` (RFC 9116, contact for vuln reports). **No `robots.txt` in the repo on purpose** — Cloudflare serves a **managed robots.txt** at the edge on `riotriot.com.br` (allows search, blocks AI-training crawlers: GPTBot/ClaudeBot/CCBot/Google-Extended/etc.). Don't add a repo `robots.txt` — it'd be overridden on the domain and only confuse. `/rider` is kept out of search by its `noindex` meta tag, not robots.

## Local preview
```
python3 -m http.server 8000      # from repo root
# open http://localhost:8000
```

## Brand
- Colors (`:root` CSS vars): `--orange:#ff5b29` (primary), `--lilac:#d9a8ff`, `--cream:#ece6d8`, `--ink:#1a1a1a`.
- Fonts (Google Fonts): **Anton** (display / section titles) + **JetBrains Mono** (body).
- Section titles use `.kicker` with **`font-weight:400`** — Anton is single-weight; adding bold faux-bolds it (looks heavy/distorted). Keep 400.

## Sections (top → bottom, single scroll page)
Hero · A Banda · Membros · Repertório & Som (Spotify embed) · Ao Vivo (photo gallery + lightbox) · Técnico/Produção (stage-plot toggle + input list) · Contato (emoji icons + WhatsApp button).

## Images / assets — conventions
- **All photos are pre-graded B&W** (delivered that way). There is **NO CSS `grayscale` filter** anymore — it was removed because a CSS `filter` also desaturates an element's `box-shadow` (it was graying the lilac member-photo shadow). Don't re-add grayscale; grade images at the source instead.
- Optimize images with macOS `sips`, e.g.: `sips -s format jpeg -s formatOptions 78 --resampleWidth 2000 SRC --out OUT.jpg`.
- Logos (`logo-horizontal.png`, `logo-vertical.png`) are recolored to the brand orange via ImageMagick: `magick in.png -channel RGB -fill '#ff5b29' -colorize 100 out.png` (keeps alpha).
- **Member photos** `assets/img/{beto,fernanda,endy,gabriel,greg}.jpg` are the lighter B&W grade; the darker originals are kept as `*-atual.jpg` for easy revert.
- **Open Graph image** (`og:image`) MUST be an **absolute URL** or WhatsApp/social link previews won't fetch it.

## Band roster & Membros order
Roster: **Beto** (Guitarra Base) · **Fernanda** (Vocal) · **Endy** (Guitarra solo + backings) · **Gabriel** (Baixo) · **Greg** (Bateria). *(Pedro left; Gabriel replaced him on bass.)*
- Desktop layout = stage perspective, 3-2: row1 Beto · Fernanda · Endy; row2 Gabriel · Greg.
- Mobile (single column) is reordered via CSS `order` to **Vocal first**: Fernanda, Beto, Endy, Gabriel, Greg.
- Never guess which face is which member — confirm identities before labeling.

## Asset sources (multi-agent)
Photos come from the **drive-agent** over the local agent-bus (this session registers as `site-agent`). Endy approves any public photo selection directly. The hero photo + illustrated stage plot are designer/Claude-made assets supplied by Endy.

## Conventions
- **Commit message:** `<Short description>. Co-Authored-By: Claude <Model> (Endy Silveira)` (substitute the active model, e.g. `Opus 4.8`).
- After pushing, verify the deploy by polling the live URL until the change appears.
- When Endy is "batching", **stage locally (commit, no push)** and only `git push` (= deploy) when he says so.

## Open TODOs
- **"Mapa de Palco" image** (coming in a few days) — Endy will supply an updated illustrated stage plot; replace `assets/img/stageplot-ilustrado.jpg` (used both on the site Técnico section and in `/rider`). The numbered technical SVG (`stageplot.py` → `assets/stageplot.svg`) is separate — only regen it if channel numbers/positions change.
- **Greg's photo** is lower-res (719px) — swap when a hi-res original arrives.
- **Press-kit PDF** download — button was removed; restore once the PDF is generated (the press-kit repo's `build.py`/Playwright pipeline).
- **Custom domain `riotriot.com.br` — ✅ LIVE** (serving with SSL: site, `/rider`, and the og share image all return 200; nameservers on Cloudflare `javier`/`luciana.ns.cloudflare.com`; DNSSEC off; `og:image`/`og:url` point to the domain). **`www.riotriot.com.br` → 301 redirect to the root is set up** (proxied CNAME `www`→`riotriot.com.br` + a Cloudflare Redirect Rule, path/query preserved). Share preview: fresh URL, so the first WhatsApp/FB share scrapes the correct branded card automatically.
