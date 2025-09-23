**Charity Data Analysis and Web Scraping Demo**
Project Overview

This project demonstrates data analysis and web scraping workflows using charity data. The main goals were:

Data Analysis: Clean, analyze, and visualize a real-world charity dataset.

Web Scraping Demo: Showcase a mini web scraping workflow to extract charity information from a public website.

Datasets Used
1. Kaggle Dataset

Source: Pennsylvania Charities

Format: CSV (pennsylvania_charities.csv)

Content: Includes charity names, EIN, category, address, city, state, contact info, and financial information.

Use: This dataset was used to perform full-scale data analysis, including:

Data cleaning (handling missing values, standardizing text)

Frequency analysis of charity categories

Visualization of top charity categories using bar charts

Exporting cleaned data to CSV for further analysis

2. Web Scraping Attempt

Target: Charity Navigator search page (https://www.charitynavigator.org/search?q=children)

Objective: Extract charity names and categories directly from the website using Python and Selenium.

Outcome:

The page is dynamic and loads results via JavaScript after a keyword search.

Using requests or even Selenium without simulating typing and search results in zero data, because the charity cards do not exist in the static HTML.

Despite using Selenium with WebDriverWait, no charity elements were detected because the page requires interaction and JavaScript execution to display content.

Conclusion: Direct scraping of this dynamic search page is not reliable for automated scripts. Instead, Kaggle’s dataset provides a GDPR-friendly and reproducible source of charity data for analysis.

Project Structure
WebScrapping/
│
├── pennsylvania_charities.csv     # Original Kaggle dataset
├── scraper_kaggle.py              # Script for analyzing Kaggle CSV
├── webscraping_demo.py            # Small Selenium demo (optional)
├── charities_cleaned.csv          # Cleaned CSV output from Kaggle data
├── charity_word_freq.png          # Bar chart visualization
└── README.md                      # Project documentation

Analysis Highlights

Top Charity Categories (from Kaggle data):

Other, Activities, Related, Development, Educational, Institutions, Services, Multipurpose, Church

Visualizations:

Bar chart of the 10 most frequent categories

Cleaned Dataset:

Saved as charities_cleaned.csv

Technical Details
Kaggle CSV Analysis

Libraries Used: pandas, matplotlib, re, collections

Workflow:

Load CSV using pandas

Clean category text (remove stop words, normalize)

Count word frequencies using Counter

Plot top 10 words in a bar chart

Save cleaned CSV for reproducibility

Web Scraping Demo

Libraries Used: selenium, webdriver-manager (optional), pandas

Workflow:

Launch headless Chrome browser

Navigate to Charity Navigator search page

Attempt to locate charity cards using CSS selectors

Save results to CSV (note: this produces no data on dynamic pages without typing the search keyword)

This demo illustrates a real-world challenge in web scraping: dynamic pages often require user interaction or API access.

Key Takeaways

Static vs Dynamic Data: Kaggle CSV provided reliable static data for analysis. Web scraping dynamic pages may fail without simulating user actions.

GDPR and Compliance: Using publicly available datasets avoids legal and privacy issues when handling charity data.

Portfolio Ready: Combines a practical data analysis project with a web scraping demonstration for professional showcase.

How to Run

Kaggle Analysis:

python scraper_kaggle.py


Produces charities_cleaned.csv and charity_word_freq.png.

Web Scraping Demo (optional):

python webscraping_demo.py


Requires ChromeDriver and Selenium installed.

May produce no results on dynamic search pages without keyword interaction.
