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

// Ao Vivo: click a photo to view it full-screen
const lb = document.getElementById('lightbox');
if (lb) {
  const lbImg = lb.querySelector('.lightbox-img');
  const closeLb = () => { lb.hidden = true; lbImg.removeAttribute('src'); document.body.style.overflow = ''; };
  document.querySelectorAll('.gallery img').forEach(img =>
    img.addEventListener('click', () => {
      lbImg.src = img.currentSrc || img.src;
      lbImg.alt = img.alt || '';
      lb.hidden = false;
      document.body.style.overflow = 'hidden';
    })
  );
  lb.addEventListener('click', e => { if (e.target !== lbImg) closeLb(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && !lb.hidden) closeLb(); });
}