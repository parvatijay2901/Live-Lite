"""
This module scrapes the data from Harvard Health website, process it 
and store in csv format to be used by recommendation tool.

Functions:
- scrape_calories_data()
- process_calories_data()
- write_to_csv()
"""
import csv
import requests
from bs4 import BeautifulSoup
# pylint: disable=line-too-long
# Disbaling this to ensute url remians in single line for readability.

# pylint: disable=too-many-locals
# Code is well structured and readable.
# Using temp local variable for mulyiple column pprocessing.
def scrape_calories_data(filepath):
    """
    Scrapes data from a webpage and processes it to 
    calculate average calories burned per kg and per lbs.
    The processed data is then written into a csv file.
    Args:
        None
    Raises:
        ConnectionError: If there is an issue with connecting to the URL.
        ValueError: If the URL is invalid or if the webpage structure is unexpected
                    or if data points in table are invalid.
    Returns:
        None
    """
    try:
        # URL of the webpage to scrape
        url = "https://www.health.harvard.edu/'diet-and-weight-loss/calories-burned-in-30-minutes-for-people-of-three-different-weights"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all tables containing the data
        tables = soup.find_all("table")
        all_data = []

        # Iterate through each table to load records
        for table in tables:
            table_name_tag = table.find(["h4"])
            table_name = table_name_tag.text.strip() if table_name_tag else "Table"
            activities = []
            calories_125lbs = []
            calories_155lbs = []
            calories_185lbs = []

            for row in table.find_all("tr")[1:]:
                cells = row.find_all("td")
                activity = cells[0].text.strip()
                try:
                    cal_125lbs = int(cells[1].text.strip())
                except ValueError:
                    cal_125lbs = 0
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
            all_data.extend(zip([table_name]*len(activities), activities,
            calories_125lbs, calories_155lbs, calories_185lbs))
        write_to_csv(process_calories_data(all_data), filepath)

    except requests.exceptions.RequestException as ex:
        raise ConnectionError(f"Error connecting to URL: {ex}") from ex

    except (ValueError, AttributeError) as exc:
        raise ValueError(f"Invalid URL or unexpected webpage structure: {exc}") from exc


def process_calories_data(scraped_data):
    """
    Processes the raw scraped data to add calculated fields.
    Args:
        Scraped_data (list): Raw data from website.
    Returns:
        list: List of processed data.
    """
    all_data_processed = []
    for data in scraped_data:
        activity_type, activity, cal_125lbs, cal_155lbs, cal_185lbs = data
        sum_cal_per_lb = 0
        count_nonzero = 0

        # Calculate calories per pound using average weight, excluding 0 values
        if cal_125lbs != 0:
            sum_cal_per_lb += cal_125lbs / 125
            count_nonzero += 1
        if cal_155lbs != 0:
            sum_cal_per_lb += cal_155lbs / 155
            count_nonzero += 1
        if cal_185lbs != 0:
            sum_cal_per_lb += cal_185lbs / 185
            count_nonzero += 1

        # Calculate average calories per pound
        if count_nonzero != 0:
            cal_per_lb_avg = sum_cal_per_lb / count_nonzero
            cal_per_kg_avg = cal_per_lb_avg / 0.453592
        else:
            # If all values are zero, set averages to 0
            cal_per_lb_avg = 0
            cal_per_kg_avg = 0

        all_data_processed.append((activity_type, activity, cal_125lbs, cal_155lbs,
        cal_185lbs, cal_per_lb_avg, cal_per_kg_avg))
    return all_data_processed


def write_to_csv(processed_data,filepath):
    """
    Writes processed data into a csv file, by removing unwanted records.
    Args:
        processes_data (list): list of processed data.
    Returns:
        None
    """
    # Remove unwanted records
    filtered_data = []
    for data in processed_data:
        if data[-1] != 0 and data[1] != "Sleeping":
            filtered_data.append(data)

    # Write the data into a CSV file
    with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Activity Type",
                            "Activity",
                            "Calories (125 lbs)",
                            "Calories (155 lbs)",
                            "Calories (185 lbs)",
                            "cal_per_lb_avg",
                            "cal_per_kg_avg"])
        writer.writerows(filtered_data)
    print(f"File saved to '{filepath}'.")

if __name__ == "__main__":
    IP = "./LiveLite/data/input_files/calories_burned_30_minutes.csv"
    scrape_calories_data(IP)
