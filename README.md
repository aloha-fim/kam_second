# Swiss Analytics

## LLM AI
- Azure Cloud





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

![alt text](./kam/static/assets/images/cover_page.jpg)

![alt text](./kam/static/assets/images/dash_touch_image.jpg)

![alt text](./kam/static/assets/images/dash_filter_image.jpg)

![alt text](./kam/static/assets/images/simple_graph_image.jpg)



