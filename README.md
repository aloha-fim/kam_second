# Swiss Analytics

## URL: https://kam-second.onrender.com/

## LLM AI
- Azure Cloud

```
- App to show records of the Zurich marathon, showing running times as measure to improve performance.

- Azure AI is introduced to improve the "mental" aspect of running a marathon.
- A feature of uplifting and inspiration quotes was attached to the original dataset,
as an example on how each runner could provide a reason for running the race.
- This feature was embedded with Azure AI in python and postgres to provide recommendations
for potential runners on how to succeed.

# Motivation for App

- 2 days ago I was involved in a bicycle accident and it me in a tough spot.

- I needed a reason to Motivate and push through the challenges of doubt and injury.

- So I though of creating an app with inspirational quotes to reframe my mindset.
```

![alt text](./kam/static/assets/images/first_attempt.jpg)

```
- First, I tried to hack the embeddings with Langchain.
- However, recommendations were sparse and even unavailable with the LLM.
```

![alt text](./kam/static/assets/images/recommend_azure.jpg)

```
- Then I made improvements using Azure AI.
- I took in advice from the Microsoft RAGHack sessions such how adding markdowns to csv
can have an affect with LLM's and learned the limitations of my app to make future improvements
such as how Flask does not the async functionality of FastAPI for faster processing.

```

![alt text](./kam/static/assets/images/azure_acc.jpg)

```
- The result has made an impact.
For instance, I asked "Can you provide inspirational quotes to get over my accident?"

- Azure AI responded from Ebert and Liedtke with "Sometimes life hits you in the head with a brick. Don't lose faith."
and "You may find your exasperation turns to inspiration", respectively.

- I hope to continue improving the app so that runners can focus on their perspective to transform
challenges into growth.

-Maybe runners with like-minded reasons for getting through the marathon
could run together as a group.  This would be something cool to build upon.
```

<video controls src="kam/static/raghack.mp4" title="Title"></video>
- Video: https://drive.google.com/file/d/1803szzAFOaZnbmmcTiGDK0iUmWEitYHW/view?usp=drive_link

## Configuration
- command: pip freeze > requirements.txt
- activate virtual environment
- command: python app.py

![alt text](./kam/static/assets/images/python_app.jpg)

## Scrape Data
- Use Beautiful Soup into txt / csv


# Format Data

## Tranfer csv files from csv into postgres database
```
- seed_db.py to adhere with schema data types
- command: python seed_db.py
- Regex replace characters after "," for timestamp validation
- dates
```

![alt text](./kam/static/assets/images/code_seed.jpg)


## add to the dataset - age group and count
```
- command: python refine_seed.py
- Create age group attribute
```

## API
```
- Flask
- seed_db.py validated by Flask forms into Postgres
- API route /load_data created to output records
```

![alt text](./kam/static/assets/images/api_route.jpg)

## Postgres
```
- connect to Postgres SQL database
```

![alt text](./kam/static/assets/images/psql_records.jpg)


## Visualize
- Plotly and Dash

![alt text](./kam/static/assets/images/dash_touch_image.jpg)

![alt text](./kam/static/assets/images/dash_filter_image.jpg)

![alt text](./kam/static/assets/images/simple_graph_image.jpg)



