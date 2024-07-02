from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
import threading
import time 
import backend

def scroller(driver):
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

def ingestPost(subreddit, driver):

    posts = SoupStrainer("shreddit-post")

    while True:  

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser", parse_only=posts)

        for story in soup.find_all("shreddit-post"):

            id = story["id"]
            author = story["author"]
            title = story["post-title"]
            content = story.find("a", slot="text-body").div.div.get_text()
                
            backend.upload(subreddit, id, author, title, content)


        print("Waiting for next post to be scraped \n \n \n")
        time.sleep(10)

def main():
    subreddit = "r\AITAH"

    driver = webdriver.Firefox()
    driver.get("https://www.reddit.com/r/AITAH")

    time.sleep(3)

    threading.Thread(target=scroller, args=(driver,)).start()
    threading.Thread(target=ingestPost, args=(subreddit ,driver,)).start()


    input("Press Enter to end session")

    driver.quit()

    
main()


















    