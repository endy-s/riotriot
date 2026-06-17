const toggle = document.querySelector('.nav-toggle');
const links = document.querySelector('.nav-links');
toggle.addEventListener('click', () => {
  const open = links.classList.toggle('open');
  toggle.setAttribute('aria-expanded', String(open));
});
links.querySelectorAll('a').forEach(a =>
  a.addEventListener('click', () => {
    links.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  })
);

// Técnico: segmented control switching stage-plot views
const segs = document.querySelectorAll('#tecnico .plot-switch .seg');
if (segs.length) {
  const ilus = document.querySelector('.plot-ilustrado');
  const tec = document.querySelector('.plot-tecnico');
  segs.forEach(btn => btn.addEventListener('click', () => {
    const showIlustrado = btn.dataset.view === 'ilustrado';
    segs.forEach(b => b.classList.toggle('active', b === btn));
    if (ilus) ilus.hidden = !showIlustrado;
    if (tec) tec.hidden = showIlustrado;
  }));
}

// Ao Vivo: lightbox gallery with prev/next (arrows + keyboard)
const lb = document.getElementById('lightbox');
if (lb) {
  const lbImg = lb.querySelector('.lightbox-img');
  const gImgs = Array.from(document.querySelectorAll('.gallery img'));
  let idx = 0;
  const show = i => {
    idx = (i + gImgs.length) % gImgs.length;
    const img = gImgs[idx];
    lbImg.src = img.currentSrc || img.src;
    lbImg.alt = img.alt || '';
  };
  const openLb = i => { show(i); lb.hidden = false; document.body.style.overflow = 'hidden'; };
  const closeLb = () => { lb.hidden = true; lbImg.removeAttribute('src'); document.body.style.overflow = ''; };
  gImgs.forEach((img, i) => img.addEventListener('click', () => openLb(i)));
  lb.querySelector('.lightbox-prev').addEventListener('click', e => { e.stopPropagation(); show(idx - 1); });
  lb.querySelector('.lightbox-next').addEventListener('click', e => { e.stopPropagation(); show(idx + 1); });
  lb.addEventListener('click', e => { if (e.target !== lbImg) closeLb(); });
  document.addEventListener('keydown', e => {
    if (lb.hidden) return;
    if (e.key === 'Escape') closeLb();
    else if (e.key === 'ArrowRight') show(idx + 1);
    else if (e.key === 'ArrowLeft') show(idx - 1);
  });
}

// Font test toggle (JetBrains vs Roboto Mono) — TEMP, remove once a font is chosen
const fSegs = document.querySelectorAll('.font-switch .seg');
fSegs.forEach(btn => btn.addEventListener('click', () => {
  fSegs.forEach(b => b.classList.toggle('active', b === btn));
  document.body.classList.toggle('font-roboto', btn.dataset.font === 'roboto');
}));