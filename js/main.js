// Mobile menu
const toggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('.nav ul');
if (toggle) toggle.addEventListener('click', () => {
  const open = menu.classList.toggle('open');
  toggle.setAttribute('aria-expanded', open);
});

// Portfolio filters
document.querySelectorAll('.filters button').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filters button').forEach(b => b.classList.remove('on'));
    btn.classList.add('on');
    const f = btn.dataset.filter;
    document.querySelectorAll('.gallery figure').forEach(fig => {
      fig.style.display = (f === 'all' || fig.dataset.cat.includes(f)) ? '' : 'none';
    });
  });
});

// Lightbox
const lb = document.querySelector('.lightbox');
if (lb) {
  const lbImg = lb.querySelector('img'), lbCap = lb.querySelector('p');
  document.querySelectorAll('.gallery figure').forEach(fig => {
    fig.tabIndex = 0;
    const open = () => {
      const img = fig.querySelector('img');
      lbImg.src = img.src; lbImg.alt = img.alt;
      lbCap.textContent = fig.querySelector('figcaption')?.textContent || '';
      lb.classList.add('open');
    };
    fig.addEventListener('click', open);
    fig.addEventListener('keydown', e => { if (e.key === 'Enter') open(); });
  });
  const close = () => lb.classList.remove('open');
  lb.addEventListener('click', e => { if (e.target !== lbImg) close(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
}

// Footer year
document.querySelectorAll('.year').forEach(el => el.textContent = new Date().getFullYear());
