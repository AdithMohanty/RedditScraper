### README for Reddit Subreddit Scraper with Firebase Integration

This Python project scrapes Reddit posts from a specific subreddit, processes the data, and uploads it to a **Firestore database** using Firebase. The scraper is designed to handle dynamic page content using **Selenium** and **BeautifulSoup** and runs in a multithreaded environment to efficiently scroll and scrape posts concurrently. 

#### Key Features:
1. **Automated Dynamic Scrolling**: Uses Selenium to continuously scroll down a Reddit page to load more posts dynamically.
2. **Post Scraping**: Extracts post details (author, title, content) from the subreddit’s HTML using BeautifulSoup.
3. **Firestore Database Upload**: After scraping, the post data is uploaded to a Firestore database, preventing duplicate entries.
4. **Multithreading**: Two threads run simultaneously: one for scrolling and one for scraping, improving efficiency.

#### Code Breakdown:
1. **`scroller(driver)`**: 
   - This function continuously scrolls down the subreddit page using Selenium, allowing new content to load dynamically. It pauses for 5 seconds between scrolls to let the page load.
   
2. **`ingestPost(subreddit, driver)`**: 
   - Scrapes posts from the subreddit, extracts information like post ID, author, title, and content, and then calls `upload()` to store the data in Firestore.
   - The `SoupStrainer` filters out non-relevant content, focusing only on Reddit posts (`shreddit-post` elements).
   
3. **`upload()`** (Added in the second file):
   - Initializes Firebase with credentials stored in `serviceAccountKey.json`.
   - Checks if the post ID already exists in the Firestore database to avoid duplicates.
   - If the post does not exist, it stores the post details such as author, title, content, and other metadata like sentiment and author gender.
   
4. **`execute(subreddit)`**: 
   - Opens a Firefox browser using Selenium and navigates to the target subreddit.
   - Starts two threads: one for scrolling and one for scraping, both of which run until the user terminates the process.

#### Firebase Integration:
The **Firebase Firestore** database is used to store the scraped data. The script interacts with the Firestore using the `firebase_admin` SDK, with the following key points:
- **Initialization**: The Firebase app is initialized using a service account key stored in the `keys/serviceAccountKey.json` file.
- **Upload Logic**: The `upload()` function ensures that each post is uploaded only once, preventing duplicate entries.
- **Data Structure**: Each post document contains fields like `id`, `author`, `title`, `content`, along with additional fields like `next_part`, `sentiment`, and `author_gender` which can be used for future data processing.

#### Dependencies:
- **BeautifulSoup4**: For parsing the HTML content of the Reddit page.
- **Selenium**: For interacting with the dynamically loading Reddit page.
- **Firebase Admin SDK**: For uploading data to the Firestore database.
- **Threading**: To manage scrolling and scraping simultaneously.

#### Installation:
1. **Install Python Dependencies**:
   Make sure you have the required packages installed:
   ```bash
   pip install beautifulsoup4 selenium firebase-admin
   ```
   
2. **Set Up GeckoDriver for Selenium**:
   - Download and install **GeckoDriver** from [GeckoDriver GitHub](https://github.com/mozilla/geckodriver/releases), or use a package manager like Homebrew to install it.
   
3. **Set Up Firebase**:
   - Download your Firebase **service account key** and save it as `keys/serviceAccountKey.json`.
   - Ensure that your Firestore database is set up in Firebase, and that the necessary permissions are granted to your service account for database writes.

4. **Running the Script**:
   To run the script:
   ```bash
   python <script_name.py>
   ```
   The script will open a Firefox window, load the subreddit, and start scraping posts while uploading them to Firestore.

5. **Stopping the Script**:
   The scraping and scrolling process will continue until you manually stop it by pressing "Enter" in the console.

#### Example:
```python
execute("berkeley") 
```
This will start scraping posts from the **r/berkeley** subreddit.

#### Error Handling:
- **Duplicate Posts**: If a post has already been uploaded to Firestore, it will not be uploaded again.
- **Scraping Issues**: If no posts are found or the scraping fails for some reason, the script will continue retrying without crashing.

#### Project Structure:
```
/project-directory
│
├── scraper.py                # Main scraping script
├── backend.py                # Firebase integration script
└── keys/
    └── serviceAccountKey.json # Firebase service account key
```

#### Future Improvements:
- **Sentiment Analysis**: The current script includes a placeholder for `sentiment` analysis. This can be enhanced using libraries like **roBERTa**.
- **Rate Limiting**: Adding error handling and delays to avoid being blocked by Reddit.
