from datetime import datetime, timedelta

# creating date
data = datetime(2020, 9, 25)

print(data)

# format data
print(data.strftime('%d/%m/%Y'))

newData = datetime.strptime('20/04/2020', '%d/%m/%Y')

print(newData)
