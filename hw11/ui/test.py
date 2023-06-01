import re

regex = r'(\d\d)-(\d\d)-(\d\d\d\d)'

date = '24-05-2023'

result = re.search(regex, date)

print(result)
