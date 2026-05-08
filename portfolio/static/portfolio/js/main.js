/* === PORTFOLIO MAIN JS === */

// AOS Init
AOS.init({ duration: 700, easing: 'ease-out-cubic', once: true, offset: 60 });

// Theme Toggle
const html = document.documentElement;
const themeToggle = document.getElementById('themeToggle');
const themeIcon = document.getElementById('themeIcon');
const savedTheme = localStorage.getItem('theme') || 'dark';
html.setAttribute('data-theme', savedTheme);
updateThemeIcon(savedTheme);

themeToggle.addEventListener('click', () => {
  const next = html.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
  html.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
  updateThemeIcon(next);
});

function updateThemeIcon(theme) {
  themeIcon.className = theme === 'dark' ? 'bi bi-moon-fill' : 'bi bi-sun-fill';
}

// Sticky Navbar
const navbar = document.getElementById('mainNav');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 60);
}, { passive: true });

// Mobile Menu
const mobileToggle = document.getElementById('mobileToggle');
const mobileMenu = document.getElementById('mobileMenu');
if (mobileToggle && mobileMenu) {
  mobileToggle.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
    mobileToggle.classList.toggle('active');
  });
  document.querySelectorAll('.mobile-link').forEach(link => {
    link.addEventListener('click', () => {
      mobileMenu.classList.remove('open');
      mobileToggle.classList.remove('active');
    });
  });
}

// Active Nav Link on Scroll
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link[href^="#"]');
function updateActiveNav() {
  let current = '';
  sections.forEach(section => {
    if (window.scrollY >= section.offsetTop - 100) current = section.id;
  });
  navLinks.forEach(link => {
    link.classList.toggle('active', link.getAttribute('href') === `#${current}`);
  });
}
window.addEventListener('scroll', updateActiveNav, { passive: true });

// Project Filtering
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const filter = btn.dataset.filter;
    document.querySelectorAll('.project-card-wrap').forEach(card => {
      if (filter === 'all') {
        card.classList.remove('hidden-card');
      } else {
        const techs = (card.dataset.tech || '').toLowerCase().split(',').map(t => t.trim());
        card.classList.toggle('hidden-card', !techs.some(t => t.includes(filter.toLowerCase())));
      }
    });
  });
});

// Contact Form AJAX
const contactForm = document.getElementById('contactForm');
const submitBtn = document.getElementById('submitBtn');
const formSuccess = document.getElementById('formSuccess');
if (contactForm) {
  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const btnLabel = submitBtn.querySelector('.btn-label');
    const btnLoading = submitBtn.querySelector('.btn-loading');
    btnLabel.classList.add('hidden');
    btnLoading.classList.remove('hidden');
    submitBtn.disabled = true;
    try {
      const res = await fetch(window.location.href, {
        method: 'POST',
        body: new FormData(contactForm),
        headers: { 'X-Requested-With': 'XMLHttpRequest' },
      });
      const data = await res.json();
      if (data.success) {
        contactForm.reset();
        formSuccess.classList.remove('hidden');
        setTimeout(() => formSuccess.classList.add('hidden'), 5000);
      } else {
        alert(data.message || 'Something went wrong.');
      }
    } catch {
      alert('Network error. Please try again.');
    } finally {
      btnLabel.classList.remove('hidden');
      btnLoading.classList.add('hidden');
      submitBtn.disabled = false;
    }
  });
}

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// Counter Animation
function animateCounter(el, target, duration = 1800) {
  let start = 0;
  const step = target / (duration / 16);
  const timer = setInterval(() => {
    start += step;
    if (start >= target) {
      el.textContent = target;
      clearInterval(timer);
    } else {
      el.textContent = Math.floor(start);
    }
  }, 16);
}

const statObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll('.stat-number').forEach(el => {
        const num = parseInt(el.dataset.count || el.textContent.replace(/\D/g, ''));
        if (num) animateCounter(el, num);
      });
      statObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });

const statsRow = document.querySelector('.stats-row');
if (statsRow) statObserver.observe(statsRow);

// Typing Effect
const heroRole = document.getElementById('heroRole');
if (heroRole) {
  const titles = [
    'Python Backend Developer',
    'Django & FastAPI Expert',
    'Cloud-Native Architect',
    'API Design Specialist',
  ];
  let currentTitle = 0, charIndex = 0, isDeleting = false, speed = 80;
  function typeEffect() {
    const full = titles[currentTitle];
    if (!isDeleting) {
      heroRole.textContent = full.slice(0, charIndex + 1);
      charIndex++;
      speed = charIndex === full.length ? 2800 : 80;
      if (charIndex === full.length) isDeleting = true;
    } else {
      heroRole.textContent = full.slice(0, charIndex - 1);
      charIndex--;
      if (charIndex === 0) {
        isDeleting = false;
        currentTitle = (currentTitle + 1) % titles.length;
        speed = 300;
      } else {
        speed = 40;
      }
    }
    setTimeout(typeEffect, speed);
  }
  setTimeout(typeEffect, 1200);
}

// Certificate Lightbox
function openCert(btn) {
  const frame = btn.closest('.cert-frame');
  const img = frame.querySelector('.cert-img');
  const lightbox = document.getElementById('certLightbox');
  document.getElementById('lightboxImg').src = img.src;
  document.getElementById('lightboxImg').alt = img.alt;
  document.getElementById('lightboxLabel').textContent = img.dataset.cert;
  lightbox.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  document.getElementById('certLightbox').classList.remove('open');
  document.body.style.overflow = '';
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeLightbox();
});

// Page load
window.addEventListener('load', () => {
  document.body.style.opacity = '1';
});