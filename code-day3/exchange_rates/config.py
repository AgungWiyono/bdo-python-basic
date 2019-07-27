# The currency that we want to analyze
WANTED_KURS = ['MYR', 'JPY', 'CNY', 'USD']

# The day range of the data that we want to scrape
# Starting for today until past x days
DAY_RANGE = 14

# Folder where the folder will be saved
# Don't use / at the end of the folder name
# Default is result.csv in this folder
SAVEFILE = None

if not SAVEFILE:
    SAVEFILE = "result.csv"

# Parsing delay
PARSING_DELAY = 2
