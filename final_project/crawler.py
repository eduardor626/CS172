from bs4 import BeautifulSoup
import requests
import json


def crawler(seedList, pagesToCrawl):
    scrapedURLs = []
    URLsToBeScraped = []
    # Read in from list of URL from text file
    fi = open(seedList, "r")
    seedUrlsFromFile = fi.readlines()
    fi.close()
    # Need to remove end line characters
    for element in seedUrlsFromFile:
        URLsToBeScraped.append(element.strip())
    print(URLsToBeScraped)

    # Create loop to go over links inside URlsToBeScraped
    while(pagesToCrawl > 0):
        pagesToCrawl -= 1
        # Dequeue URL
        urlToScrape = URLsToBeScraped[0]
        URLsToBeScraped.pop(0)
        if(urlToScrape not in scrapedURLs):
            scrapedURLs.append(urlToScrape)
        else:
            continue
        webPage = requests.get(urlToScrape)
        htmlContent = webPage.text

        # abstract url links from html text
        soupObject = BeautifulSoup(htmlContent, "html.parser")
        bodyContent = soupObject.body.text
        bodyString = (str(bodyContent)).replace('\n', '')

        # Create dictionary that contains html content and url
        dict = {
            "url": urlToScrape,
            "html": bodyString
        }
        with open("data.json", "a") as outfile:
            json.dump(dict, outfile)
            outfile.write('\n')

        hyperlinks = soupObject.find_all('a')

        for url in hyperlinks:
            if("http" in (url.get('href'))):
                if(url.get('href') not in scrapedURLs):
                    URLsToBeScraped.append(url.get('href'))

    print("URLs SCRAPPED: ")
    print(scrapedURLs)


def main():
    crawler("seedUrls.txt", 6)


if __name__ == "__main__":
    main()
