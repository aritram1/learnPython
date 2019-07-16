# dict and orderedDict examples

from collections import OrderedDict 

# Data
DAYS = ['Sunday', 'Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday','Saturday']

# Make and display the DAYS in dict (order is NOT retained)
DAYSdict = {day[0:3]:day for day in DAYS}
for day in DAYSdict:
    print('{0} = {1}'.format(day, DAYSdict[day]))

print('-'*20)
# Make and display the DAYS in Ordereddict (order IS retained)
DAYSOrdereddict = OrderedDict()
for day in DAYS:
    shortname = day[0:3]
    DAYSOrdereddict[shortname] = day
for day in DAYSOrdereddict:
    print('{0} = {1}'.format(day, DAYSOrdereddict[day]))
    
    
