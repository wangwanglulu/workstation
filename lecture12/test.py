from datetime import datetime
first_date = datetime.strptime('2021-7-1', '%Y-%m-%d') 
second_date = datetime.strptime('2022-9-1', '%Y-%m-%d') 
print(second_date-first_date)