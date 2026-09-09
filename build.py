import html
import re
import time
from email.utils import formatdate
from pathlib import Path

import markdown

POSTS = Path("posts")
DIST = Path("dist")
TEMPLATE = ("<!doctype html><html><head><meta charset='utf-8'>"
            "<title>{title}</title>"
            "<style>body{{max-width:680px;margin:3rem auto;"
            "font-family:Georgia,serif;line-height:1.7;padding:0 1rem}}"
            "</style></head><body>{body}</body></html>")


def parse_post(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^# (.+)$", text)
    title = m.group(1).strip() if m else path.stem
    date = time.strftime("%Y-%m-%d", time.localtime(path.stat().st_mtime))
    body = markdown.markdown(text, extensions=["fenced_code", "tables"])
    return {"title": title, "date": date, "body": body,
            "slug": path.stem}


def build():
    DIST.mkdir(exist_ok=True)
    posts = sorted((parse_post(p) for p in POSTS.glob("*.md")),
                   key=lambda p: p["date"], reverse=True)
    for p in posts:
        out = TEMPLATE.format(title=html.escape(p["title"]), body=p["body"])
        (DIST / (p["slug"] + ".html")).write_text(out, encoding="utf-8")
    items = "\n".join(
        "<li>%s &mdash; <a href='%s.html'>%s</a></li>"
        % (p["date"], p["slug"], html.escape(p["title"])) for p in posts)
    index = TEMPLATE.format(title="home", body="<h1>posts</h1><ul>"
                            + items + "</ul>")
    (DIST / "index.html").write_text(index, encoding="utf-8")
    rss_items = "".join(
        "<item><title>%s</title><pubDate>%s</pubDate></item>"
        % (html.escape(p["title"]), formatdate()) for p in posts)
    (DIST / "feed.xml").write_text(
        "<?xml version='1.0'?><rss version='2.0'><channel>"
        + rss_items + "</channel></rss>", encoding="utf-8")
    print("built %d posts -> dist/" % len(posts))


if __name__ == "__main__":
    build()
