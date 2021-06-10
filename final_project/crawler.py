from bs4 import BeautifulSoup
import requests
import json
import time
import ast
import os
import sys
arrayOfJSONobjects = []


def crawler(seedList, pagesToCrawl, outputDir):
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
        print(docID)
        pagesToCrawl -= 1
        # Dequeue URL
        urlToScrape = URLsToBeScraped.pop(0)
        if(urlToScrape not in scrapedURLs):
            # if (urlToScrape.endswith('/')):
            #print("Adding URL: " + urlToScrape)
            # scrapedURLs.append(urlToScrape)
            # print(scrapedURLs)
            # print("\n")
            if(urlToScrape.endswith('/') == False):
                #print("Adding URL: " + urlToScrape)
                urlToScrape = urlToScrape + '/'
                # print(scrapedURLs)
                # print("\n")
        else:
            #print("Url is already inside of scrapedUrls " + urlToScrape)
            continue
        try:
            webPage = requests.get(urlToScrape, timeout=50000)
        except:
            continue
        # time.sleep(1)
        htmlContent = webPage.text

        # abstract url links from html text
        soupObject = BeautifulSoup(htmlContent, "html.parser")
        try:
            bodyContent = soupObject.body.text
        except:
            continue
        bodyString = (str(bodyContent)).replace('\n', '').replace(
            '(', "").replace(')', "").replace("`", "").replace("'", "")

        # Create dictionary that contains html content and url
        # print(urlToScrape)
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
        crawledDataFile = open(outputDir, 'w')

        hyperlinks = soupObject.find_all("a", {'href': True})

        for url in hyperlinks:
            # print(url)
            urlInquestion = url.get('href').strip()
            if(urlInquestion.endswith('/') == False):
                urlInquestion = urlInquestion + '/'
            if("https" in urlInquestion):
                if(urlInquestion not in URLsToBeScraped):
                    if(urlInquestion not in scrapedURLs):
                        if("campusstore.ucr.edu" not in urlInquestion):
                            URLsToBeScraped.append(urlInquestion)

        scrapedURLs.append(urlToScrape)

    crawledDataFile = open(outputDir, 'w')

    arrayString = str(arrayOfJSONobjects).replace(
        "'", "").replace("\\\\", "\\")

    crawledDataFile.write(arrayString)
    crawledDataFile.close()
    print("URLs SCRAPPED: ")
    print(scrapedURLs)


def main():
    args = sys.argv[1:]
    # print(args[0])
    # print(args[1])
    # print(args[2])
    crawler(args[0], int(args[1]), args[2])


if __name__ == "__main__":
    main()
