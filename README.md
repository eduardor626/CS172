# CS172

The report should include:

Collaboration Details: Description of contribution of each team member.
## Part 1 - Crawler
### (a) Architecture
We have created a single threaded crawler. There's two seperate arrays that keep track of the URLs that have been crawled and those that haven't. The crawler will take a URL from the front of the array and determine if it is a valid URL to crawl.
### (b) The Crawling or data collection strategy 
We feed in a list of seed URLs to populate the initial array. The crawler will then pop the front of the array and determine if this URL has been scraped or not by checking if it is inside of the array containing all scraped URLs. This is how we prevent duplicate URLs. If it hasn't been scraped, then a request gets sent using the `requests` library. This will return the entire web page. Having this we can eliminate all `html` tags and only obtain the text from the web page. We then use this text to create a `BeautifulSoup` object that will be used to parse the contents of the page. We can then use this `BeautifulSoup` object to find all URL links inside of the page. Before adding them to the array of URLs to scrape, we first check whether or not it has been scraped, and whether or not it is in the array of URLs to be scraped. Once the entire URL has been scraped, we then use `json.dumps` to create objects containing the url, and all of the content found on that page. 
### (c) Data Structures employed
Throughout the program two arrays are used to keep track of URLs that have been scraped and those that are waiting to be scraped. 
### (d) Limitations (if any) of the system.
The max number of URLs that can be scrapped is approximately 1112. Once it reaches the 1113 URL, a bug causes the program to hang.
### (e) Instruction on how to deploy the crawler. 
The crawler expects 3 command line inputs. First is the file containing seed URLs. Second input is the number of pages to crawl. Third input is the output file we wish the program to write to. Format is as follows `python3 ./crawler.py < seed − Fileseed.txt > < num − pages : <1112 > <output−file >`.
Sample call to the crawler: `python3 .\crawler.py seedUrls.txt 6 sd1.json`
## Part 2 - Indexer
Instructions on how to deploy the system. Ideally, you should include an indexer.bat (Windows) or indexer.sh (Unix/Linux) executable file that takes as input all necessary parameters .  Example: [user@server] ./indexer.sh < output − dir >
## Part 3 - Extension
Detailed description of your ‘extension’ and motivation or benefit of the implemented feature or extension. Include screen shots of your system in action.
