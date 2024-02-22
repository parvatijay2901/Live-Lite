import requests
from bs4 import BeautifulSoup
import csv

# URL of the webpage to scrape
url = "https://www.health.harvard.edu/diet-and-weight-loss/calories-burned-in-30-minutes-for-people-of-three-different-weights"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all tables containing the data
tables = soup.find_all("table")

# Initialize list to store all data
all_data = []

# Default table name when no <h3> tag is found
default_table_name = "Table"

# Iterate through each table
for table in tables:
    # Get the table name
    table_name_tag = table.find(["h4"])
    table_name = table_name_tag.text.strip() if table_name_tag else "Table"


    # Initialize lists to store data for this table
    activities = []
    calories_125lbs = []
    calories_155lbs = []
    calories_185lbs = []

   
    # Iterate through each row of the table
    for row in table.find_all("tr")[1:]:
        # Extract data from each cell in the row
        cells = row.find_all("td")
        activity = cells[0].text.strip()
        try:
            cal_125lbs = int(cells[1].text.strip())
        except ValueError:
            cal_125lbs = 0  # Set default value if conversion fails, handling blanks or ":"
        try:
            cal_155lbs = int(cells[2].text.strip())
        except ValueError:
            cal_155lbs = 0  
        try:
            cal_185lbs = int(cells[3].text.strip())
        except ValueError:
            cal_185lbs = 0  


        # Append the data to respective lists
        activities.append(activity)
        calories_125lbs.append(cal_125lbs)
        calories_155lbs.append(cal_155lbs)
        calories_185lbs.append(cal_185lbs)

    # Append data for this table to all_data with activity type
    all_data.extend(zip([table_name]*len(activities), activities, calories_125lbs, calories_155lbs, calories_185lbs))

all_data_processed = []
for data in all_data:
    activity_type, activity, cal_125lbs, cal_155lbs, cal_185lbs = data
    
    # Calculate calories per pound using average weight
    cal_per_lb_avg = ((data[2]/125) + (data[3]/155) + (data[4]/185)) / 3 
    all_data_processed.append((activity_type, activity, cal_125lbs, cal_155lbs, cal_185lbs, cal_per_lb_avg))


for data in all_data_processed:
    if data[-1]==0:
        all_data_processed.remove(data)   

# Write the data into a CSV file
with open("calories_burned_30_minutes.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Activity Type", "Activity", "Calories (125 lbs)", "Calories (155 lbs)", "Calories (185 lbs)", "cal_per_lb_avg"])
    for data in all_data_processed:
        writer.writerow(data)
