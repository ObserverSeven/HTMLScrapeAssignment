from bs4 import BeautifulSoup
import requests

def URLfetch_return(arg) :

    response = requests.get(arg)
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all("tr")
    cells = []
    for table in tables:
        rows= table.find_all("td")
        for row in rows:
            cells.append(row.get_text(strip=True))
    i = 0
    while i < 3:
        cells.pop(0)
        i += 1
    letters = [ [] , [] , []]
    mode = 1
    for i in range(0, len(cells), 3):
        x = int(cells[i])
        char = cells[i + 1]
        y = int(cells[i + 2])
        letters[0].append(x)
        letters[1].append(y)
        letters[2].append(char)
    max_x = max(x for x in letters[0])
    print(max_x)
    max_y = max(y for y in letters[1])
    print(max_y)
    grid = [
        [" " for _ in range(max_x + 1)]
        for _ in range(max_y + 1)]
    for i in range(len(letters[2])):
        x = letters[0][i]
        y = letters[1][i]
        grid[max_y - y][x] = letters[2][i]
    for line in grid:
        print("".join(line))
            
    input("\n Holding...")

URLfetch_return("https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub")