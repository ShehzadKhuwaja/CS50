import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex = r".*src=\"(.+?)\".*?"
    if match := re.search(regex, s):
        url = match.group(1)
        url = url.replace("/embed", "")
        if "youtube" not in url:
            return None
        if "www" in url:
            url = url.replace("www.youtube.com","youtu.be")
        else:
            url = url.replace("youtube.com","youtu.be")
        if "https" not in url:
            url = url.replace("http", "https")
        return url
    else:
        return None

...


if __name__ == "__main__":
    main()
