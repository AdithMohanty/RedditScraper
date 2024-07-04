from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
import threading
import time 
import backend

# Continuously loads the dynamic page
def scroller(driver):
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

# Scrapes posts from subreddit and uploads to database
def ingestPost(subreddit, driver):

    # Filters all posts
    posts = SoupStrainer("shreddit-post")
    text = SoupStrainer("a", slot="text-body")
    subreddit = "r\\" + subreddit

    while True:  
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser", parse_only=posts)

        for story in soup.find_all("shreddit-post"):
            try: 
                id = story["id"]
                author = story["author"]
                title = story["post-title"]
                content = story.find("a", slot="text-body").div.div.get_text()
                    
                backend.upload(subreddit, id, author, title, content)

            except:
                print("No posts found or Invalid post")
                continue

        print("Waiting for next post to be scraped \n \n \n")
        time.sleep(10)


# Executes the scraper
def execute(subreddit):

    driver = webdriver.Firefox()
    driver.get("https://www.reddit.com/r/" + subreddit)

    # loadtime
    time.sleep(3)

    threading.Thread(target=scroller, args=(driver,)).start()
    threading.Thread(target=ingestPost, args=(subreddit ,driver,)).start()


    input("Press Enter to end session")

    driver.quit()

    
execute("berkeley")