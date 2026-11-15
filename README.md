# Dmitry Kriukov — photographer site

Статика, без сборки и без бэкенда. Открывается любым веб-сервером.

## Структура

```
index.html          — главная (RU)
en/index.html       — английская версия
blog/               — блог: список историй и страницы съёмок (RU)
en/blog/            — то же на английском
assets/css/style.css
assets/js/main.js
assets/img/         — фотографии (сейчас заглушки)
sitemap.xml
robots.txt
tools/stories.json  — данные историй блога (правьте здесь)
tools/build_blog.py — генератор страниц блога
```

## Локальный просмотр

```bash
python3 -m http.server 8080
# http://localhost:8080  и  http://localhost:8080/en/
```

## Что заменить перед публикацией

1. **Фотографии** — в `assets/img/` сейчас стоковые заглушки. Положите свои кадры
   с теми же именами файлов.
2. **Цены** — примерные (490 / 1490 / 190 €), поправьте под себя.
3. **Домен** — сейчас прописан `https://dmitry-photo.vercel.app` во всех мета-тегах
   (canonical, hreflang, og, twitter), в `sitemap.xml` и в schema `url`.
   При переезде на свой домен замените его целиком.

## SEO

- `lang`, `canonical`, `hreflang` (ru/en), `og:*`, `twitter:*`
- JSON-LD `ProfessionalService`: адрес Бар, зоны обслуживания, телефон, почта
- `sitemap.xml` + `robots.txt` со ссылкой на него
- у изображений `width`/`height`, `loading="lazy"`, `alt`

## Возможности

- прозрачная шапка над  hero, становится плотной при скролле
- плавные reveal-анимации, бегущая строка городов
- лайтбокс по клику на кадры
- аккордеон FAQ на нативных `<details>` (индексируется)
- адаптив 390 / 768 / 1080 / 1440, учтён `prefers-reduced-motion`

## Блог

Правишь `tools/stories.json` (название, место, дата, текст, список кадров) и
запускаешь:

```bash
python3 tools/build_blog.py
```

Появляются `blog/<slug>/index.html` и `en/blog/<slug>/index.html`, плюс обновляется
список в `blog/index.html`. Не забудь добавить новые URL в `sitemap.xml`.
