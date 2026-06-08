# ASCII Grid Fetcher

A small Python tool that fetches a published Google Doc table and renders it as an ASCII grid.

## Features
- Scrapes structured table data from a URL
- Converts coordinate + character data into a 2D grid
- Prints rendered ASCII output

Note that it's specifically interested in table structure within google docs, in a specific manner. 
Here's a reference of the expected table structure.
https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub

## Usage

```bash
python run.py --url "<google-doc-url>"
```

Docker:
```bash
docker build -t gridfetcher .
```

Docker run:
```bash
docker run gridfetcher --url "<google doc url>"
```