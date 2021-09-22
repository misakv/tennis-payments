"""Module s API"""

import os
import pickle

import pandas as pd
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


SAMPLE_SPREADSHEET_ID_input = "1FalpFHNGuca2pJzbUk7DQG2BXQTPjwUmDOqTMlUOppU"
SAMPLE_RANGE_NAME = "A1:AA1000"


def main():
    global values_input, service
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "my_json_file.json", SCOPES
            )  # here enter the name of your downloaded JSON file
            creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result_input = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values_input = result_input.get("values", [])

    if not values_input and not values_expansion:
        raise ValueError("No data found.")


main()

df = pd.DataFrame(values_input[1:], columns=values_input[0])


def get_player(dataframe: pd.DataFrame) -> tuple:
    """Funkce vrátí dvojici jmen ve formátu
    dluh, dlužník (1. pád) , věřitel (3. pád)"""
    vojta = 0
    marek = 0
    for index in range(0, len(df)):

        if df.iat[index, 6] == "Marek":
            marek += int(df.iat[index, 5])

        else:
            vojta += int(df.iat[index, 5])

    dluh = abs(vojta - marek)
    veritel = "Vojtovi" if vojta >= marek else "Markovi"
    dluznik = "Marek" if veritel == "Vojtovi" else "Vojta"

    return dluh, dluznik, veritel
