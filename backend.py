import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('keys/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def upload(subreddit, id, author, title, content, next_part="NONE", sentiment="ND", author_gender="ND"):
    

    # if the id of the post is alread in teh database dont uplaod it again
    if db.collection(subreddit).document(id).get().exists:
        print("The post " + title + " already exists")
    else: 
        db.collection(subreddit).document(id).set({
            "id": id,
            "author": author,
            "title": title,
            "content": content,
            "next_part": next_part, 
            "sentiment": sentiment,
            "author_gender": author_gender
        })
        
        print(title + " was uploaded to database")
