from urllib import robotparser
from urllib.parse import urlparse


class RobotsParser:
    def __init__(self):
        self.parser = robotparser.RobotFileParser()
        self.cached_robots = {}

    def can_fetch(self, url, user_agent="*"):
        domain = urlparse(url).netloc
        if domain not in self.cached_robots:
            robots_url = f"https://{domain}/robots.txt"
            self.parser.set_url(robots_url)
            self.parser.read()
            self.cached_robots[domain] = self.parser
        else:
            self.parser = self.cached_robots[domain]

        return self.parser.can_fetch(user_agent, url)

    def crawl_delay(self, url, user_agent="*"):
        domain = urlparse(url).netloc
        if domain in self.cached_robots:
            return self.cached_robots[domain].crawl_delay(user_agent)
        return None

    def get_robots_url(self, url):
        domain = urlparse(url).netloc
        return f"https://{domain}/robots.txt"
