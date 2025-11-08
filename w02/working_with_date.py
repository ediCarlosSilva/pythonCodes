# 1. Import the necessary libraries
from datetime import datetime

# 2. Here you have the values you want to format (you can set any value)
datetime_value = datetime.now()

# 3. This part is specific to the output format you want
# You can do some research on datetime standards and conventions
# This follows the European format:
datetime_format = "%d/%m/%Y %H:%M"

# 4. Convert and get the value
datetime_formatted = datetime_value.strftime(datetime_format)

# 5. Optionally, print to check the results
print(datetime_formatted)