#import the libraries
import requests
import json
import time
import datetime
import os

#HackerNews API
headers = {"User-Agent": "TrendPulse/1.0"}
storiesurl="https://hacker-news.firebaseio.com/v0/topstories.json" 

#Fetches the top 500 story id
try:   
        respond=requests.get(storiesurl,headers=headers,timeout=10)
        respond.raise_for_status()

        storyid=respond.json()[:500] 
        print(f"Fetched stories {len(storyid)}")
except requests.RequestException as e:
    print(f"Error fetching story ID:{e}")
    storyid=[]

#Get details of each story    
storydetail=[]
for story_id in storyid:
    url=f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

    try:
        response=requests.get(url,headers=headers,timeout=10)
        response.raise_for_status()
        story=response.json()
        if isinstance(story,dict)and story.get("title"):
            storydetail.append(story)
    except requests.RequestException as e:
        print("Error{story_id}:{e}")
print(f"Fetched{len(storydetail)}stories")   

#keywords to identify the categories  
categories={
    "technology":["AI","software","code","cloud","computer","data","API","GPU","LLM"],
    "worldnews":["war","government","country","president","election","climate","global","attack"],
    "sports":["NFL","NBA","FIFA","sport","game","team","player","league","championship"],
    "science":["research","study","space","physics","biology","discovery","NASA","genome"],
    "entertainment":["movie","film","music","Netflix","game","book","show","award","streaming"]
}

# function to find category 

def categoriesstory(title):
   if not title:
      return None
   title_lower=title.lower()
   for category,keywords in categories.items():
      for keyword in keywords:
         if keyword.lower() in title_lower:
            return category
   return None

categorydata={
    category:[] 
    for category in categories
}

#Collects 25 stories
for category in categories:
 for story in storydetail:
    if len(categorydata[category])>=25:
          break

    if not isinstance(story,dict):
        continue

    title = story.get("title")
 
    category1=categoriesstory(title)
    if category1 !=category:
      continue
   
#Create the fields   
    storykeywords={
       "post_id":story.get("id"),
       "title":story.get("title"),
       "score":story.get("score",0),
       "author":story.get("by"),
       "num_comments":story.get("descendants",0),
       "category":category,
       "collected_at":datetime.datetime.now().isoformat()
    }


    categorydata[category].append(storykeywords)
print(
    f"{category}:"
    f"{len(categorydata[category])} stories collected"
)

#waits 2 second between categories
time.sleep(2)
 #Combines all categories into list
allstories = []
for category in categorydata:
     allstories.extend(categorydata[category])

#create data folder
os.makedirs("data",exist_ok=True)

#cteate filename
today=datetime.datetime.utcnow().strftime("%d%m%y")
filename= f"data/trends_{today}.json"


with open (filename,"w", encoding="utf-8") as f:
     json.dump (allstories,f,indent=4,ensure_ascii=False)

total=len(allstories)
print(f"Collected Stories{total}")
print(f"Saved to:{filename}")
print("\nStories per Category")

for category in categorydata:
     print(f"{category}:{len(categorydata[category])}")
