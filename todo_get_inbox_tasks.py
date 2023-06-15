
import requests
import pandas as pd

# main
def main():

    # Define the API endpoint and the headers
    url = "https://api.todoist.com/rest/v2/tasks"
    headers = {"Authorization": "Bearer efe5fb6965803037d1fb11a2f18b8e629d9339ce"}

    # Make the API request
    response = requests.get(url, headers=headers)
    tasks = response.json()

    # Convert the JSON data to a DataFrame
    df = pd.DataFrame(tasks)

    # Write the DataFrame to an Excel spreadsheet
    df.to_excel("tasks.xlsx")


if __name__ == "__main__":
    main()

