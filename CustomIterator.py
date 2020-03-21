# A collection type class that can iterate with custom iterator            

class myiterable:
    count = 0
    current_it_count = 0;

    def __init__(self):
        self.content = {}
        self.iterator = {}

    def add(self, item):
        self.content['myiterable' + str(myiterable.count)] = item
        myiterable.count= myiterable.count + 1

    def __iter__(self):
        each = self.content['myiterable' + str(myiterable.current_it_count)]
        key = list(each.keys())[0];
        self.iterator = {
            'key' : key,
            'value' : each[key]
        }
        return self

    def __next__(self):
        if myiterable.current_it_count >= myiterable.count:
            raise StopIteration();
        result = self.content['myiterable'+str(myiterable.current_it_count)]
        myiterable.current_it_count = myiterable.current_it_count + 1
        return result;

# Lets test 
aritra = myiterable()

# Add some properties
aritra.add({'name' : 'aritra'})
aritra.add({'roll' : {'a' : '123'}})
aritra.add({'one' : {'two' : 'three'}})
aritra.add({'otherValues' : {'somemore' : {'someother' : 'finallValue'}}})
aritraIterator = iter(aritra)

# Usage
# print(next(aritraIterator)) #{'name' : 'aritra'}
# print(next(aritraIterator)) #{'roll' : 123}
# print(next(aritraIterator)) # creates StopIteration exception [hence commented]

while(True):
try:
    print(next(aritraIterator))
except(StopIteration):
    print('All values printed')
    break

# output:
# {'roll': {'a': '123'}}                                                                                                                 
#{'one': {'two': 'three'}}                                                                                                              
# {'otherValues': {'somemore': {'someother': 'finallValue'}}}                                                                            
# All values printed 
