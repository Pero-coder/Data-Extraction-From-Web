import os
import time
from typing import NamedTuple, Optional, Dict, Tuple, List, Any

import requests
from bs4 import BeautifulSoup



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


def save_webpage(url: str) -> None:
    pass
    # splited_url = url.split("/")[3:]

    # if len(splited_url) == 1:
    #     page_file = f"saved_pages/{splited_url[0]}"

    # else: 
    #     if not os.path.isdir(f"saved_pages/{splited_url[0]}"):
    #         os.mkdir(f"saved_pages/{splited_url[0]}")
    #     page_file = f"saved_pages/{splited_url[0]}/{splited_url[1]}"

    # with open(page_file, "w") as page:
    #     page.write()


def get_linux_only_availability(base_url: str) -> List[str]:
    """
    Finds all functions that area available only on Linux systems
    :param base_url: base url of the website
    :return: all function names that area available only on Linux systems
    """
    # Tuto funkci implementuj
    pass

all_pages_list = ["https://python.iamroot.eu/"]
def get_all_pages(base_url: str) -> List[str]:
    # try:
    #     splited_url = base_url.split("/")[3:]

    #     if len(splited_url) == 1:
    #         page_file = open(f"saved_pages/{splited_url[0]}", "r")

    #     else: 
    #         page_file = open(f"saved_pages/{splited_url[0]}/{splited_url[1]}", "r")

    #     page = page_file.read()
    #     page_file.close()
    
    # except:
    responce = download_webpage(base_url)
    page  = responce.content
    save_webpage(base_url)

    soup = BeautifulSoup(page, "html.parser")
    a_tags = soup.find_all("a")
    
    for a in a_tags:
        url = a.get("href")
        print(url)
        if url != base_url and url not in all_pages_list and url.startswith("https://python.iamroot.eu/"):
            all_pages_list.append(url)
            get_all_pages(url)
    


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
    import json

    if not os.path.isdir("saved_pages"):
        os.mkdir("saved_pages")

    get_all_pages('https://python.iamroot.eu/')
    print(all_pages_list)

    time_start = time.time()
    print(json.dumps(scrap_all('https://python.iamroot.eu/').as_dict()))
    print('took', int(time.time() - time_start), 's')


if __name__ == '__main__':
    main()
