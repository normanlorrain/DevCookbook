import os

OUTPUT="site"

def write_home_page(home_page: str):
    """Writes the home_page HTML to file

    Args:
        home_page (str): A string of HTML to be written to file
    """

    with open(f"./{OUTPUT}/index.html", "w+") as f:
        f.write(home_page)


def write_page(slug: str, page: str):
    """Writes the page HTML to `/{slug}/index.html`

    Args:
        slug (str):
        page (str): A string of HTML to be written to file
    """

    assert slug != "index"

    if not os.path.exists(f"./{OUTPUT}/{slug}"):
        os.makedirs(f"./{OUTPUT}/{slug}")

    with open(f"./{OUTPUT}/{slug}/index.html", "w+") as f:
        f.write(page)
