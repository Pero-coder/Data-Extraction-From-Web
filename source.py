import os
import time
from typing import NamedTuple, Optional, Dict, Tuple, List, Any

import requests
from bs4 import BeautifulSoup


"""
#########################
# CUSTOM-MADE FUNCTIONS #
#########################
"""

all_pages_list = []
def get_all_pages(base_url: str) -> List[str]:
    soup = get_soup(base_url)
    a_tags = soup.find_all("a")
    
    for a in a_tags:
        url = a.get("href")

        if not url.startswith("http"):
            full_url = f"https://python.iamroot.eu/{url}"
            if full_url not in all_pages_list:
                if url.endswith(".html"):
                    if url.find("../") == -1:
                        if url.find("#") == -1:
                            all_pages_list.append(full_url)
                            get_all_pages(full_url)    


def get_soup(base_url: str) -> BeautifulSoup:
    if not base_url == "https://python.iamroot.eu/":
        file_path = base_url[26:]

        if os.path.exists(f"saved_pages/{file_path}"):
            with open(f"saved_pages/{file_path}", "r", encoding="utf-8") as html_file:
                return BeautifulSoup(html_file.read(), "html.parser")

        else:
            responce = download_webpage(base_url)
            page  = responce.text
            save_webpage(file_path, page)
            return BeautifulSoup(page, "html.parser")
    else:
        if os.path.exists(f"saved_pages/index.html"):
            with open(f"saved_pages/index.html", "r", encoding="utf-8") as html_file:
                return BeautifulSoup(html_file.read(), "html.parser")

        else:
            responce = download_webpage(base_url)
            page  = responce.text
            save_webpage("index.html", page)
            return BeautifulSoup(page, "html.parser")

def save_webpage(file_path: str, page_content: str) -> None:
    try:
        with open(f"saved_pages/{file_path}", "w", encoding="utf-8") as html_file:
            html_file.write(page_content)
    except FileNotFoundError:
        splited_path = file_path.split("/")
        os.mkdir(f"saved_pages/{splited_path[0]}")
        with open(f"saved_pages/{splited_path[0]}/{splited_path[1]}", "w", encoding="utf-8") as html_file:
            html_file.write(page_content)


"""
#########################
# TEMPLATE FUNCTIONS #
#########################
"""

class FullScrap(NamedTuple):
    # TUTO TRIDU ROZHODNE NEMEN
    linux_only_availability: List[str]
    most_visited_webpage: Tuple[int, str]
    changes: List[Tuple[int, str]]
    params: List[Tuple[int, str]]
    tea_party: Optional[str]

    def as_dict(self) -> Dict[str, Any]:
        return {
            'linux_only_availability': self.linux_only_availability,
            'most_visited_webpage': self.most_visited_webpage,
            'changes': self.changes,
            'params': self.params,
            'tea_party': self.tea_party
        }


def download_webpage(url: str, *args, **kwargs) -> requests.Response:
    """
    Download the page and returns its response by using requests.get
    :param url: url to download
    :return: requests Response
    """
    # TUTO FUNKCI ROZHODNE NEMEN
    print('GET ', url)
    return requests.get(url, *args, **kwargs)


def get_linux_only_availability(base_url: str) -> List[str]:
    """
    Finds all functions that area available only on Linux systems
    :param base_url: base url of the website
    :return: all function names that area available only on Linux systems
    """
    # Tuto funkci implementuj
    pass


def get_most_visited_webpage(base_url: str) -> Tuple[int, str]:
    """
    Finds the page with most links to it
    :param base_url: base url of the website
    :return: number of anchors to this page and its URL
    """
    pass
    # response = requests.get(base_url)
    # page = response.content
    # soup = BeautifulSoup(page, "html.parser")
    # a_tags = soup.find_all("a")

    # page_visits = []

    # for a in a_tags:
    #     url = a.get("href")

    #     new_page = True
    #     if page_visits != []:
    #         for item in page_visits:
    #             if url in item:
    #                 item[0] += get_page_visits_count(url)
    #                 new_page = False

    #     if new_page:
    #         page_visits.append((get_page_visits_count(url), url))


def get_changes(base_url: str) -> List[Tuple[int, str]]:
    """
    Locates all counts of changes of functions and groups them by version
    :param base_url: base url of the website
    :return: all counts of changes of functions and groups them by version, sorted from the most changes DESC
    """
    # Tuto funkci implementuj
    pass


def get_most_params(base_url: str) -> List[Tuple[int, str]]:
    """
    Finds the function that accepts more than 10 parameters
    :param base_url: base url of the website
    :return: number of parameters of this function and its name, sorted by the count DESC
    """
    # Tuto funkci implementuj
    pass


def find_secret_tea_party(base_url: str) -> Optional[str]:
    """
    Locates a secret Tea party
    :param base_url: base url of the website
    :return: url at which the secret tea party can be found
    """
    # Tuto funkci implementuj
    pass


def scrap_all(base_url: str) -> FullScrap:
    """
    Scrap all the information as efficiently as we can
    :param base_url: base url of the website
    :return: full web scrap of the Python docs
    """
    # Tuto funkci muzes menit, ale musi vracet vzdy tyto data
    scrap = FullScrap(
        linux_only_availability=get_linux_only_availability(base_url),
        most_visited_webpage=get_most_visited_webpage(base_url),
        changes=get_changes(base_url),
        params=get_most_params(base_url),
        tea_party=find_secret_tea_party(base_url)
    )
    return scrap


def main() -> None:
    """
    Do a full scrap and print the results
    :return:
    """
    # Tuto funkci klidne muzes zmenit podle svych preferenci :)
    time_start = time.time()
    
    import json

    if not os.path.isdir("saved_pages"):
        os.mkdir("saved_pages")

    get_all_pages('https://python.iamroot.eu/')
    print(len(all_pages_list))

    print(json.dumps(scrap_all('https://python.iamroot.eu/').as_dict()))
    print('took', int(time.time() - time_start), 's')


if __name__ == '__main__':
    main()
