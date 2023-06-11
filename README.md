# Data Science Jobs Analysis
My first ever dashboard

## Objective
To develop a single, interactive interface that captures emerging skill requirements for in-demand job roles, including Data Engineer, Data Analyst, and Data Scientist. The goal was to streamline the career transition process by facilitating the knowledge of key skills required in each role and reduce the amount of time needed for research

## Process
### Data Collection
Data was scraped using **Power Automate from naukri.com** (Indian website for job search) and saved into **Excel**

### Data Cleaning/Transformation
Data was cleaned and processed in **Jupyter Notebook** (notebooks can be found in this repo). Then, the cleaned data was imported into **Power BI** and some final transformations were applied.
- Checked for duplicate and null values
- Correct data formatting
- Feature Engineering

### Data Visualization/Business Intelligence
- Pie chart illustrating the percentage breakdown of jobs based on required experience.
- Bar chart displaying the demand for different technologies in the job market.
- Column charts comparing the requirement of programming languages and libraries in the job market.
- A custom map of India was uploaded to Power BI (the map source is mentioned below).


![dashboard](dataroles_dashboard.png)
# References
- Map data: https://github.com/datameet/maps
- Jobs Data: https://www.naukri.com/
