import requests
from bs4 import BeautifulSoup


def fetch_grid(url: str):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    tables = soup.find_all("tr")

    cells = []
    for table in tables:
        rows = table.find_all("td")
        for row in rows:
            cells.append(row.get_text(strip=True))

    # remove header junk
    for _ in range(3):
        if cells:
            cells.pop(0)

    letters = [[], [], []]

    for i in range(0, len(cells), 3):
        x = int(cells[i])
        char = cells[i + 1]
        y = int(cells[i + 2])

        letters[0].append(x)
        letters[1].append(y)
        letters[2].append(char)

    max_x = max(letters[0])
    max_y = max(letters[1])

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for i in range(len(letters[2])):
        x = letters[0][i]
        y = letters[1][i]
        grid[max_y - y][x] = letters[2][i]

    return grid