# from faker import Faker
# import datetime

# d = datetime.date(2023, 5, 25)
# a = datetime.datetime.now()
# fake = Faker()

# for i in range(10):
# 	a = fake.date_time_between_dates(datetime_start =d, datetime_end =a)
# 	print(a)
import pandas as pd 
from part import CustomPartProvider
from pain import CustomPainProvider
from faker import Faker
import datetime

my_fake = Faker()
#  time span of 3  months 
d = datetime.date(2023, 5, 1)
a = datetime.datetime.now()



my_fake.add_provider(CustomPartProvider)
my_fake.add_provider(CustomPainProvider)

test_data  = []

for i in range(200):
    
 userId = "3f957e60-aae2-48aa-8c91-fd48be2471dc"
    #noteid 
 noteId = i
    #part
 part = my_fake.part()
	# pain level
 pain_level = my_fake.pain()
    #description
 description = my_fake.text()
    #time
 tod = my_fake.date_time_between_dates(datetime_start =d, datetime_end =a)

 test_data.append([userId, noteId, part, pain_level, description, tod] )

df = pd.DataFrame(test_data)
df.to_csv("synthetic.csv")