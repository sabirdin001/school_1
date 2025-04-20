from datetime import datetime

# Get current date
# now = datetime.now()

# Extract day and month with leading zero using strftime
day = datetime.now().strftime("%d")   # Day with leading zero (01–31)
# month = strftime("%m") # Month with leading zero (01–12)

print("Day:", day)
# print("Month:", month)
