import argparse
from fetcher import fetch_grid


def print_grid(grid):
    for line in grid:
        print("".join(line))


def main():
    parser = argparse.ArgumentParser(description="Fetch and render ASCII grid from a Google Doc")

    parser.add_argument(
        "--url",
        type=str,
        required=True,
        help="URL of published Google Doc"
    )

    args = parser.parse_args()

    grid = fetch_grid(args.url)
    print_grid(grid)


if __name__ == "__main__":
    main()