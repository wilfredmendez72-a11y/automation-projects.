import requests
from bs4 import BeautifulSoup


def print_secret_message(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    points = {}
    for row in soup.find("table").find_all("tr")[1:]:  # skip header row
        cells = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]
        if len(cells) < 3:
            continue
        x, char, y = int(cells[0]), cells[1], int(cells[2])
        points[(x, y)] = char

    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)

    # (0, 0) is the top-left corner, so y increases downward
    for y in range(0, max_y + 1):
        print("".join(points.get((x, y), " ") for x in range(max_x + 1)))


if __name__ == "__main__":
    print_secret_message(
        "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184B
