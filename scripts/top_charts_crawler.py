from bs4 import BeautifulSoup
import requests
import sys

def getUSTopChart():
    url = 'https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2016'
    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, 'lxml')
    print soup


def main():
    argc = len(sys.argv)
    if argc == 1:
        print "Please specify regions"
        print "US, TH, JP"
        sys.exit(0)
    else:
        region = sys.argv[1]
        if region.lower() == 'us':
            getUSTopChart()
        else:
            raise NotImplementedError

if __name__ == '__main__':
    main()
