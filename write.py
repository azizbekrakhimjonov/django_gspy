import datetime

from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = ''


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()

resource = {
  # "majorDimension": "ROWS",
  "values": [
    ["1", "Jamshid Jabborov", 24, 82734659],
    ["2", "Jeck", 13, 7865237],
  ]
}

request = service.spreadsheets().values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Sheet1!A1", valueInputOption="USER_ENTERED",
                                                  body=resource)
response = request.execute()

print('Successfuly')