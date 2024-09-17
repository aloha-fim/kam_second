# Swiss Analytics

Welcome to Swiss Analytics! This application offers a unique perspective on marathon running by integrating both physical and mental aspects of the race. Here’s everything you need to know about the project:

## 🚀 Project Overview

Swiss Analytics goes beyond traditional marathon metrics. While most marathon apps focus on physical performance like running time, we emphasize the mental journey of running a marathon. Inspired by a personal challenge, the app combines inspirational quotes with marathon data to help runners overcome mental hurdles.

## 🌐 Access the App

- **URL:** [Swiss Analytics](https://kam-second.onrender.com/)

## 📜 Motivation Behind the App

After a serious bicycle accident that left me questioning my own resilience, I realized the power of motivational support. This app was born from the need to overcome doubt and injury by providing uplifting quotes and mental support to runners. The goal is to help users transform their challenges into personal growth through shared experiences and advice.

## 🛠️ Key Features

- **Inspirational Quotes:** Integrated with Azure AI, our app provides motivational quotes tailored to each runner’s personal reasons for participating in the marathon.
- **Mental Health Support:** Using Azure AI, the app offers recommendations based on mental barriers and connects users with others who share similar experiences.
- **Enhanced Recommendations:** Improvements with Azure AI have led to more accurate and helpful recommendations compared to previous attempts.

## 💡 How It Works

1. **Data Collection:** Use Beautiful Soup to scrape data and format it into CSV files.
2. **Data Storage:** Import data into a Postgres database. Use `seed_db.py` to ensure data adheres to schema types.
3. **Data Enrichment:** Refine the dataset to include age groups and additional metrics with `refine_seed.py`.
4. **API Integration:** Flask is used to create API routes for data interaction, with endpoints like `/load_data` for record output.
5. **Visualization:** Leverage Plotly and Dash for interactive data visualizations.

## 🛠️ Setup and Configuration

1. **Install Dependencies:**
   ```bash
   pip freeze > requirements.txt
   ```
2. **Activate Virtual Environment:**
   ```bash
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. **Run the Application:**
   ```bash
   python app.py
   ```

## 🔄 Data Handling

- **Scraping:** Use Beautiful Soup to scrape data into text or CSV files.
- **Database Import:** Transfer CSV files into Postgres using `seed_db.py` and validate timestamps and dates.
- **Refinement:** Update the dataset to include age groups using `refine_seed.py`.

## 📈 Visualization

- **Plotly & Dash:** Use these libraries for creating and displaying interactive graphs.

## 📹 Video Demonstration

Watch our [demo video](https://drive.google.com/file/d/1803szzAFOaZnbmmcTiGDK0iUmWEitYHW/view?usp=drive_link) to see the app in action!

## 🚧 Known Issues

The app is a work in progress and may contain bugs. The notebook `graphs_azure.ipynb` contains examples of working Azure AI integrations and visualizations.

## 🛠️ Future Plans

- **Community Building:** Enable runners to connect with others who have similar motivations and challenges.
- **Validation:** Allow runners to validate their success and track their progress.

Feel free to contribute or provide feedback to help us improve and evolve the app!

---

**Swiss Analytics** – Running for a cause, not just for records.

