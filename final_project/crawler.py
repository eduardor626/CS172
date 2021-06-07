from bs4 import BeautifulSoup
import requests
import json
arrayOfJSONobjects = []


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
    docID = 1

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
        webPage = requests.get(urlToScrape, timeout=50000)
        htmlContent = webPage.text

        # abstract url links from html text
        soupObject = BeautifulSoup(htmlContent, "html.parser")
        bodyContent = soupObject.body.text
        bodyString = (str(bodyContent)).replace('\n', '').replace(
            '(', "").replace(')', "").replace("`", "").replace("'", "")

        # Create dictionary that contains html content and url
        dict = {
            "id": docID,
            "url": urlToScrape,
            "html": bodyString
        }
        docID += 1
        # with open("data.json", "a") as outfile:
        json.dumps(dict)
        # outfile.write('\n')
        arrayOfJSONobjects.append(json.dumps(dict))
        crawledDataFile = open('data.json', 'w')

        hyperlinks = soupObject.find_all('a')

        for url in hyperlinks:
            if("http" in (url.get('href'))):
                if(url.get('href') not in scrapedURLs):
                    URLsToBeScraped.append(url.get('href'))
    crawledDataFile = open('data.json', 'w')

    arrayString = str(arrayOfJSONobjects).replace(
        "'", "").replace("\\\\", "\\")

    crawledDataFile.write(arrayString)
    crawledDataFile.close()
    print("URLs SCRAPPED: ")
    print(scrapedURLs)


def main():
    crawler("seedUrls.txt", 11)


if __name__ == "__main__":
    main()
