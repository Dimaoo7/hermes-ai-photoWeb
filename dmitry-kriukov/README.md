# Dmitry Kriukov — photographer site

Статика, без сборки и без бэкенда. Открывается любым веб-сервером.

## Структура

```
index.html          — главная (RU)
en/index.html       — английская версия
assets/css/style.css
assets/js/main.js
assets/img/         — фотографии (сейчас заглушки)
sitemap.xml
robots.txt
```

## Локальный просмотр

```bash
cd sites/dmitry-kriukov
python3 -m http.server 8080
# http://localhost:8080  и  http://localhost:8080/en/
```

## Что заменить перед публикацией

1. **Домен** — везде стоит заглушка `https://dmitrykriukov.com/`
   (canonical, hreflang, og:url, sitemap, schema `url`).
2. **Контакты** — `hello@dmitrykriukov.com`, `+382 69 000 000`,
   Telegram/Instagram/WhatsApp — в `index.html` и `en/index.html`.
3. **Фотографии** — в `assets/img/` сейчас стоковые заглушки.
   Положите свои кадры с теми же именами файлов.
4. **Цены** — примерные, поправьте под себя.

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
