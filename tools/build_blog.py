#!/usr/bin/env python3
"""Generate the static blog pages from tools/stories.json.

Run from the project root:  python3 tools/build_blog.py
Output is plain HTML in blog/ and en/blog/ — no build step on Vercel.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORIES = json.load(open(os.path.join(ROOT, "tools", "stories.json"), encoding="utf-8"))
DOMAIN = "https://dmitry-photo.vercel.app"

PAGE = """<!DOCTYPE html>
<html lang="%%LANG%%">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%%TITLE%%</title>
<meta name="description" content="%%DESC%%">
<link rel="canonical" href="%%CANON%%">
<link rel="alternate" hreflang="ru" href="%%RU%%">
<link rel="alternate" hreflang="en" href="%%EN%%">
<link rel="alternate" hreflang="x-default" href="%%RU%%">
<meta property="og:type" content="%%OGTYPE%%">
<meta property="og:site_name" content="Dmitry Kriukov Photography">
<meta property="og:locale" content="%%OGLOCALE%%">
<meta property="og:title" content="%%TITLE%%">
<meta property="og:description" content="%%DESC%%">
<meta property="og:url" content="%%CANON%%">
<meta property="og:image" content="%%ASSET%%img/%%COVER%%">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%%TITLE%%">
<meta name="twitter:description" content="%%DESC%%">
<meta name="twitter:image" content="%%ASSET%%img/%%COVER%%">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23191512'/%3E%3Ctext x='16' y='22' font-family='Georgia,serif' font-size='19' fill='%23FAF7F1' text-anchor='middle'%3EDK%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="%%ASSET%%css/style.css">
<script type="application/ld+json">
%%LD%%
</script>
</head>
<body>
<header class="header header--over-hero" id="top">
  <div class="wrap header__in">
    <a class="header__logo" href="%%HOME%%">%%BRAND%%</a>
    <nav class="header__nav" aria-label="%%NAVLABEL%%">
      <a href="%%HOME%%#portfolio">%%NAV1%%</a>
      <a href="%%HOME%%#services">%%NAV2%%</a>
      <a href="%%HOME%%#prices">%%NAV3%%</a>
      <a href="%%HOME%%#about">%%NAV4%%</a>
      <a href="%%HOME%%#contacts">%%NAV5%%</a>
    </nav>
    <div class="header__right">
      <div class="lang" aria-label="%%LANGLABEL%%">
        <a href="%%RULINK%%" hreflang="ru" %%ARIA_RU%%>RU</a><span>/</span><a href="%%ENLINK%%" hreflang="en" %%ARIA_EN%%>EN</a>
      </div>
    </div>
  </div>
</header>
<main>
%%BODY%%
</main>
<footer class="footer">
  <div class="wrap footer__in">
    <span>© <span data-year>2026</span> %%BRAND%%</span>
    <span>%%FOOTERCITIES%%</span>
    <a href="#top">%%UPTOP%%</a>
  </div>
</footer>
<div class="lightbox" role="dialog" aria-modal="true" aria-label="%%LBLABEL%%">
  <button class="lightbox__btn" type="button" aria-label="%%LBCLOSE%%">×</button>
  <img src="" alt="">
  <p class="lightbox__cap"></p>
</div>
<script src="%%ASSET%%js/main.js" defer></script>
</body>
</html>
"""

I18N = {
    "ru": {
        "brand": "Дмитрий Крюков", "navlabel": "Основная навигация",
        "nav1": "Портфолио", "nav2": "Услуги", "nav3": "Цены", "nav4": "Обо мне", "nav5": "Контакты",
        "langlabel": "Язык", "oglocale": "ru_RU",
        "footercities": "Бар · Будва · Котор · Пераст", "uptop": "Наверх ↑",
        "lblabel": "Просмотр фотографии", "lbclose": "Закрыть",
        "blog_title": "Блог — истории съёмок", "blog_kicker": "Блог",
        "blog_h1": "Истории, которые стоит пересматривать",
        "blog_sub": "Каждая съёмка — отдельная страница: место, дата и кадры. Нажмите, чтобы открыть.",
        "blog_open": "Открыть историю",
        "prev": "← Предыдущая", "next": "Следующая →", "allstories": "Все истории",
        "cta": "Хочу так же — написать мне",
        "desc_blog": "Свадьбы, лавстори и портретные съёмки в Черногории: истории с фотографиями.",
    },
    "en": {
        "brand": "Dmitry Kriukov", "navlabel": "Main navigation",
        "nav1": "Portfolio", "nav2": "Services", "nav3": "Prices", "nav4": "About", "nav5": "Contact",
        "langlabel": "Language", "oglocale": "en_GB",
        "footercities": "Bar · Budva · Kotor · Perast", "uptop": "Back to top ↑",
        "lblabel": "Photo viewer", "lbclose": "Close",
        "blog_title": "Blog — stories from the shoots", "blog_kicker": "Blog",
        "blog_h1": "Stories worth revisiting",
        "blog_sub": "Every shoot gets its own page: place, date and frames. Click to open.",
        "blog_open": "Open the story",
        "prev": "← Previous", "next": "Next →", "allstories": "All stories",
        "cta": "I want the same — write to me",
        "desc_blog": "Weddings, love stories and portrait sessions in Montenegro: stories with photographs.",
    },
}


def paths(lang, slug=None):
    """Relative paths from the page's own folder."""
    ru = "blog" if slug is None else f"blog/{slug}"
    en = "en/blog" if slug is None else f"en/blog/{slug}"
    cur = ru if lang == "ru" else en
    other = en if lang == "ru" else ru
    depth = cur.count("/") + 1
    up = "/".join([".."] * depth)
    rel = os.path.relpath(other, cur).replace(os.sep, "/")
    if not rel.startswith("."):
        rel = "./" + rel
    return {
        "asset": f"{up}/assets/",
        "home": f"{up}/",
        "self": "./",
        "other": rel + "/",
        "cur": cur,
    }


def write(path, html):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


def render(tokens, title, desc, canon, ru_url, en_url, ogtype, ld, body, cover):
    html = PAGE
    values = {
        "%%TITLE%%": title, "%%DESC%%": desc, "%%CANON%%": canon,
        "%%RU%%": ru_url, "%%EN%%": en_url, "%%OGTYPE%%": ogtype,
        "%%LD%%": ld, "%%BODY%%": body, "%%COVER%%": cover,
    }
    values.update(tokens)
    for k, v in values.items():
        html = html.replace(k, v)
    return html


def tokens_for(lang, p):
    t = I18N[lang]
    return {
        "%%LANG%%": lang, "%%BRAND%%": t["brand"], "%%NAVLABEL%%": t["navlabel"],
        "%%NAV1%%": t["nav1"], "%%NAV2%%": t["nav2"], "%%NAV3%%": t["nav3"],
        "%%NAV4%%": t["nav4"], "%%NAV5%%": t["nav5"], "%%LANGLABEL%%": t["langlabel"],
        "%%OGLOCALE%%": t["oglocale"], "%%FOOTERCITIES%%": t["footercities"],
        "%%UPTOP%%": t["uptop"], "%%LBLABEL%%": t["lblabel"], "%%LBCLOSE%%": t["lbclose"],
        "%%ASSET%%": p["asset"], "%%HOME%%": p["home"],
        "%%RULINK%%": "./" if lang == "ru" else p["other"],
        "%%ENLINK%%": p["other"] if lang == "ru" else "./",
        "%%ARIA_RU%%": 'aria-current="true"' if lang == "ru" else "",
        "%%ARIA_EN%%": 'aria-current="true"' if lang == "en" else "",
    }


# ---- blog index ----
for lang in ("ru", "en"):
    t = I18N[lang]
    p = paths(lang)
    canon = f"{DOMAIN}/{p['cur']}/"
    cards = ""
    for s in STORIES:
        d = s[lang]
        cards += f"""
      <article class="blog-card reveal">
        <a class="blog-card__media" href="{s['slug']}/"><img src="{p['asset']}img/{s['cover']}" alt="{d['title']}" width="1400" height="1050" loading="lazy" decoding="async"></a>
        <div class="blog-card__body">
          <p class="blog-card__meta">{d['location']} — {d['date']}</p>
          <h2>{d['title']}</h2>
          <p class="blog-card__text">{d['lead']}</p>
          <a class="album__link" href="{s['slug']}/">{t['blog_open']} →</a>
        </div>
      </article>"""

    body = f"""
  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <p class="eyebrow">{t['blog_kicker']}</p>
        <h2>{t['blog_h1']}</h2>
        <p>{t['blog_sub']}</p>
      </div>
      <div class="blog-list">{cards}
      </div>
    </div>
  </section>"""

    ld = json.dumps({
        "@context": "https://schema.org", "@type": "Blog",
        "name": t["blog_title"], "url": canon,
    }, ensure_ascii=False, indent=2)

    html = render(tokens_for(lang, p), t["blog_title"], t["desc_blog"], canon,
                  f"{DOMAIN}/blog/", f"{DOMAIN}/en/blog/", "blog", ld, body, "hero-beach.jpg")
    write(os.path.join(ROOT, p["cur"], "index.html"), html)

# ---- story pages ----
for i, s in enumerate(STORIES):
    prev_s = STORIES[(i - 1) % len(STORIES)]
    next_s = STORIES[(i + 1) % len(STORIES)]
    for lang in ("ru", "en"):
        t = I18N[lang]
        d = s[lang]
        p = paths(lang, s["slug"])
        canon = f"{DOMAIN}/{p['cur']}/"

        thumbs = ""
        for img in s["images"]:
            thumbs += f"""
          <button type="button" data-lightbox><img src="{p['asset']}img/{img}" alt="{d['title']} — {d['location']}" width="1400" height="1000" loading="lazy" decoding="async"></button>"""

        body = f"""
  <article class="post">
    <header class="post-hero">
      <div class="post-hero__media"><img src="{p['asset']}img/{s['cover']}" alt="{d['title']}" width="2400" height="1500" fetchpriority="high" decoding="async"></div>
      <div class="post-hero__scrim"></div>
      <div class="wrap post-hero__in">
        <p class="eyebrow">{d['location']} — {d['date']}</p>
        <h1>{d['title']}</h1>
        <div class="hero__cta"><a class="btn btn--solid" href="{p['home']}#contacts">{t['cta']}</a></div>
      </div>
    </header>
    <div class="wrap post-body">
      <p class="lead">{d['lead']}</p>
      <p class="text">{d['text']}</p>
      <div class="post-grid">{thumbs}
      </div>
    </div>
    <nav class="wrap post-nav" aria-label="{t['allstories']}">
      <a href="../{prev_s['slug']}/">{t['prev']} {prev_s[lang]['title']}</a>
      <a href="../">{t['allstories']}</a>
      <a href="../{next_s['slug']}/">{t['next']} {next_s[lang]['title']}</a>
    </nav>
  </article>"""

        ld = json.dumps({
            "@context": "https://schema.org", "@type": "BlogPosting",
            "headline": d["title"], "description": d["lead"],
            "url": canon, "image": f"{DOMAIN}/assets/img/{s['cover']}",
            "datePublished": "2026-06-01",
            "author": {"@type": "Person", "name": t["brand"]},
            "location": {"@type": "Place", "name": d["location"]},
        }, ensure_ascii=False, indent=2)

        html = render(tokens_for(lang, p), f"{d['title']} — {d['location']} | {t['brand']}",
                      d["lead"], canon,
                      f"{DOMAIN}/blog/{s['slug']}/", f"{DOMAIN}/en/blog/{s['slug']}/",
                      "article", ld, body, s["cover"])
        write(os.path.join(ROOT, p["cur"], "index.html"), html)

print("blog pages:", len(STORIES) * 2 + 2)
