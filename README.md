# inkpress

Static blog generator: markdown in, tidy HTML out

## Highlights

- Single template, plain str.format, no Jinja
- RSS feed generation
- Markdown posts with fenced code and tables
- Index page with post list by date

## Usage

```bash
mkdir posts && echo '# hello' > posts/first.md
python build.py
# site lands in dist/
```

## Install

```bash
pip install -r requirements.txt
```

## Project structure

```text
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   └── dependabot.yml
├── docs/
│   └── development.md
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── build.py
└── requirements.txt
```

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## License

MIT. Do whatever you want.
