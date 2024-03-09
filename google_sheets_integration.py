import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('path/to/credentials.json', scope)

# Authorize the client
client = gspread.authorize(credentials)

# Open the Google Sheets document
sheet = client.open('Your Spreadsheet Name')

# Select a specific worksheet
worksheet = sheet.get_worksheet(0)

# Write data to a cell
worksheet.update('A1', 'Hello, World!')

# Read data from a cell
cell_value = worksheet.acell('A1').value
print(cell_value)