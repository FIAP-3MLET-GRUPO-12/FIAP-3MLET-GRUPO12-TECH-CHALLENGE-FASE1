import requests
import pandas as pd
from io import BytesIO

def download_csv_from_url(url: str) -> pd.DataFrame:
    """
    Downloads a CSV file from the given URL and returns it as a pandas DataFrame.

    Args:
        url (str): The URL of the CSV file to download.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the CSV file.
                      Returns None if there is an error during the download or parsing process.

    Raises:
        requests.exceptions.HTTPError: If an HTTP error occurs during the request.
        requests.exceptions.RequestException: If a request exception occurs.
        Exception: For any other exceptions that occur.

    Example:
        df = download_csv_from_url('http://example.com/data.csv')
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = BytesIO(response.content)
        df = pd.read_csv(data, delimiter=';')

        return df
    
    except requests.exceptions.HTTPError as err:
        print(f"Http Error: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
        return None
    except Exception as err:
        print(f"Unexpected Error: {err}")