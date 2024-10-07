import pandas as pd
from pathlib import Path
#from django.conf import settings
#settings.configure()
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')


# Construct the path to the Excel file
excel_file_path = Path(backend.settings.BASE_DIR)/scripts/guestlist_test.xlsx


print(excel_file_path)

# Read the Excel file
df = pd.read_excel(excel_file_path)

print(df)

