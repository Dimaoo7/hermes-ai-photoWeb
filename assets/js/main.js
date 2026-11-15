/* Dmitry Kriukov — site interactions. No dependencies. */
(function () {
  'use strict';

  var header = document.querySelector('.header');
  var hero = document.querySelector('.hero, .post-hero');

  /* ---- header: transparent over the hero, solid afterwards ---- */
  function onScroll() {
    var y = window.scrollY || 0;
    if (!hero) { header.classList.add('header--solid'); header.classList.remove('header--over-hero'); return; }
    var trigger = Math.min(hero.offsetHeight - 120, window.innerHeight * 0.7);
    header.classList.toggle('header--solid', y > trigger);
    header.classList.toggle('header--over-hero', y <= trigger);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---- reveal on scroll ---- */
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ---- lightbox ---- */
  var box = document.querySelector('.lightbox');
  if (box) {
    var boxImg = box.querySelector('img');
    var boxCap = box.querySelector('.lightbox__cap');
    var lastFocus = null;

    function open(src, caption) {
      lastFocus = document.activeElement;
      boxImg.src = src;
      boxImg.alt = caption || '';
      boxCap.textContent = caption || '';
      box.classList.add('is-open');
      document.body.classList.add('lightbox-open');
      box.querySelector('.lightbox__btn').focus();
    }
    function close() {
      box.classList.remove('is-open');
      document.body.classList.remove('lightbox-open');
      boxImg.src = '';
      if (lastFocus) lastFocus.focus();
    }

    document.querySelectorAll('[data-lightbox]').forEach(function (el) {
      el.addEventListener('click', function (e) {
        e.preventDefault();
        var img = el.querySelector('img') || el;
        open(img.currentSrc || img.src, img.alt);
      });
    });

    box.addEventListener('click', function (e) { if (e.target === box) close(); });
    box.querySelector('.lightbox__btn').addEventListener('click', close);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && box.classList.contains('is-open')) close();
    });
  }

  /* ---- current year ---- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
