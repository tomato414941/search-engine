import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from .robots_parser import RobotsParser


class Crawler:
    def __init__(self, use_robots_parser=True, default_delay=1, user_agent=""):
        self.pages = {}
        self.links = {}
        self.use_robots_parser = use_robots_parser
        self.default_delay = default_delay
        self.user_agent = user_agent
        self.robots_parser = RobotsParser() if use_robots_parser else None

    def crawl(self, start_url, max_pages=10):
        print(f"Crawling {start_url}...")
        self._crawl_recursive(start_url, max_pages)
        print(f"Crawled {len(self.pages)} pages.")
        return self.pages, self.links

    def _crawl_recursive(self, url, max_pages):
        if len(self.pages) >= max_pages or url in self.pages:
            return

        robots_info = {"can_fetch": True, "crawl_delay": None, "robots_url": None}

        if self.use_robots_parser:
            robots_info["robots_url"] = self.robots_parser.get_robots_url(url)
            robots_info["can_fetch"] = self.robots_parser.can_fetch(
                url, self.user_agent
            )
            if not robots_info["can_fetch"]:
                print(f"Robots.txt disallows crawling {url}")
                self.pages[url] = {"robots_info": robots_info}
                return
            robots_info["crawl_delay"] = self.robots_parser.crawl_delay(
                url, self.user_agent
            )

        # Use the default delay if no crawl delay is specified in robots.txt
        delay = (
            robots_info["crawl_delay"]
            if robots_info["crawl_delay"] is not None
            else self.default_delay
        )

        try:
            time.sleep(delay)

            response = requests.get(url, headers={"User-Agent": self.user_agent})
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                self.pages[url] = {
                    "title": soup.title.string if soup.title else "",
                    "content": soup.get_text(),
                    "snippet": soup.p.text[:200] + "..." if soup.p else "",
                    "last_crawled": response.headers.get("Date", ""),
                    "robots_info": robots_info,
                }

                print(f"Crawled {url}")

                self.links[url] = []
                for link in soup.find_all("a"):
                    next_url = urljoin(url, link.get("href"))
                    if next_url.startswith(("http://", "https://")):
                        self.links[url].append(next_url)
                        self._crawl_recursive(next_url, max_pages)
            else:
                print(f"Failed to crawl {url}: HTTP {response.status_code}")
                self.pages[url] = {
                    "robots_info": robots_info,
                    "error": f"HTTP {response.status_code}",
                }

        except Exception as e:
            print(f"Error crawling {url}: {e}")
            self.pages[url] = {"robots_info": robots_info, "error": str(e)}
