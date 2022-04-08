import os
import time
from typing import NamedTuple, Optional, Dict, Tuple, List, Any

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


all_pages_list = []
def get_all_pages(base_url: str) -> None:
    """
    Loops from all pages and saves link of each to all_pages_list.
    """
    soup = get_soup(base_url)
    a_tags = soup.find_all("a")
    
    for a in a_tags:
        url = a.get("href")

        if is_url_valid(url):
            full_url = urljoin(base_url, url)
            if not full_url in all_pages_list:
                all_pages_list.append(full_url)
                get_all_pages(full_url)    


def is_url_valid(url: str) -> bool:
    """
    Checks if url is on same domain as base_url.
    """
    if not url.startswith("http"):
        if url.endswith(".html"):
            if url.find("#") == -1:
                return True
    return False


def get_soup(base_url: str) -> BeautifulSoup:
    """
    Chcecks if page was already downloaded and creates a BeautifulSoup 
    object.
    """
    if not base_url == "https://python.iamroot.eu/":
        file_path = base_url[26:]

        if os.path.exists(f"saved_pages/{file_path}"):
            with open(f"saved_pages/{file_path}", "r", encoding="utf-8") as html_file:
                return BeautifulSoup(html_file.read(), "html.parser")

        else:
            time.sleep(0.5)
            responce = download_webpage(base_url)
            page  = responce.text
            save_webpage(file_path, page)
            return BeautifulSoup(page, "html.parser")
    else:
        if os.path.exists(f"saved_pages/index.html"):
            with open(f"saved_pages/index.html", "r", encoding="utf-8") as html_file:
                return BeautifulSoup(html_file.read(), "html.parser")

        else:
            time.sleep(0.5)
            responce = download_webpage(base_url)
            page  = responce.text
            save_webpage("index.html", page)
            return BeautifulSoup(page, "html.parser")


def save_webpage(file_path: str, page_content: str) -> None:
    """
    Saves page on local disk.
    """
    try:
        with open(f"saved_pages/{file_path}", "w", encoding="utf-8") as html_file:
            html_file.write(page_content)

    except FileNotFoundError:
        splited_path = file_path.split("/")
        os.mkdir(f"saved_pages/{splited_path[0]}")

        with open(f"saved_pages/{splited_path[0]}/{splited_path[1]}", "w",
                  encoding="utf-8") as html_file:

            html_file.write(page_content)


class FullScrap(NamedTuple):
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
    """
    print('GET ', url)
    return requests.get(url, *args, **kwargs)


def get_linux_only_availability() -> List[str]:
    """
    Finds all functions that area available only on Linux systems
    """
    print("Getting linux avaible functions...")
    unix_avaible_functions = []
    required_words = ["Unix", "Linux"]
    prohibited_words = ["Windows", "BSD", "AIX"]
    for page in all_pages_list:
        soup = get_soup(page)

        func = soup.find_all("dl", class_ = "function")
        for dl in func:
            try:
                p = dl.find("p", class_ = "availability")
                required_word = [
                    x for x in required_words if p.text.find(x) > -1]
                prohibited_word = [
                    x for x in prohibited_words if p.text.find(x) > -1]
                if required_word and not prohibited_word:
                    dt = dl.find("dt")
                    unix_avaible_functions.append(dt.get("id"))

            except AttributeError:
                pass

        method = soup.find_all("dl", class_ = "method")
        for dl in method:
            try:
                p = dl.find("p", class_ = "availability")
                required_word = [
                    x for x in required_words if p.text.find(x) > -1]
                prohibited_word = [
                    x for x in prohibited_words if p.text.find(x) > -1]
                if required_word and not prohibited_word:
                    dt = dl.find("dt")
                    unix_avaible_functions.append(dt.get("id"))

            except AttributeError:
                pass

    return unix_avaible_functions


def get_most_visited_webpage() -> Tuple[int, str]:
    """
    Finds the page with most links to it
    """
    print("Getting most visited page...")
    link_visits = {}
    for page in all_pages_list:
        soup = get_soup(page)
        a_tags = soup.find_all("a")

        for a in a_tags:
            url = a.get("href")
            if is_url_valid(url):
                full_url = urljoin(page, url)
                try:
                    link_visits[full_url] += 1
                except KeyError:
                    link_visits[full_url] = 1

    most_visited_page = max(link_visits)
    return (link_visits[most_visited_page], most_visited_page)


def get_changes() -> List[Tuple[int, str]]:
    """
    Locates all counts of changes of functions and groups them by version
    """
    print("Getting changes...")
    changes = {}

    for page in all_pages_list:
        soup = get_soup(page)

        ver_added = soup.find_all("span", class_ = "versionmodified added")
        ver_changed = soup.find_all("span", class_ = "versionmodified changed")

        for span in ver_added:
            cut = span.text.find("3.")

            if cut != -1:
                try:
                    changes[span.text[cut:cut + 3]] += 1
                except KeyError:
                    changes[span.text[cut:cut + 3]] = 1
        
        for span in ver_changed:
            cut = span.text.find("3.")

            if cut != -1:
                try:
                    changes[span.text[cut:cut + 3]] += 1
                except KeyError:
                    changes[span.text[cut:cut + 3]] = 1

    result = sorted(changes.items(), key=lambda x: x[1], reverse=True)
    swaped_result = []

    for i in result:
        swaped_result.append((i[1], i[0]))

    return swaped_result


def get_most_params() -> List[Tuple[int, str]]:
    """
    Finds the function that accepts more than 10 parameters
    """
    print("Getting most parameters...")
    most_parm_functions = {}

    for page in all_pages_list:
        soup = get_soup(page)

        func = soup.find_all("dl", class_ = "function")
        for dl in func:
            func_names = dl.find_all("dt")
            for dt in func_names:
                parameters = dt.find_all("em", class_ = "sig-param")
                parm_count = 0

                for _ in parameters:
                    parm_count += 1

                if parm_count >= 10:
                    most_parm_functions[dt.get("id")] = parm_count
        
        methods = soup.find_all("dl", class_ = "method")
        for dl in methods:
            method_names = dl.find_all("dt")
            for dt in method_names:
                parameters = dt.find_all("em", class_ = "sig-param")
                parm_count = 0

                for _ in parameters:
                    parm_count += 1

                if parm_count >= 10:
                    most_parm_functions[dt.get("id")] = parm_count

    result = sorted(most_parm_functions.items(), key=lambda x: x[1], reverse=True)
    swaped_result = []

    for i in result:
        swaped_result.append((i[1], i[0]))

    return swaped_result


def scrap_all(base_url: str) -> FullScrap:
    """
    Scrap all the information as efficiently as we can
    """
    scrap = FullScrap(
        linux_only_availability=get_linux_only_availability(),
        most_visited_webpage=get_most_visited_webpage(),
        changes=get_changes(),
        params=get_most_params(),
        tea_party=find_secret_tea_party(base_url)
    )
    return scrap


def main() -> None:
    """
    Do a full scrap and print the results
    """
    time_start = time.time()
    
    import json

    if not os.path.isdir("saved_pages"):
        os.mkdir("saved_pages")

    print("Getting all pages...")
    get_all_pages('https://python.iamroot.eu/')
    print(len(all_pages_list), "in list")
    
    print(json.dumps(scrap_all('https://python.iamroot.eu/').as_dict()))
    print('took', int(time.time() - time_start), 's')


if __name__ == '__main__':
    main()
