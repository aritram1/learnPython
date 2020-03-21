# A collection type class that can iterate with custom iterator            

class myiterable:
    count = 0
    current_it_count = 0;

    def __init__(self):
        self.content = {}
        self.iterator = {}

    def add(self, item):
        self.content[myiterable.count] = item
        myiterable.count= myiterable.count + 1

    def __iter__(self):
        each = self.content[myiterable.current_it_count]
        key = list(each.keys())[0];
        self.iterator = {
            'key' : key,
            'value' : each[key]
        }
        return self

    def __next__(self):
        if myiterable.current_it_count >= myiterable.count:
            raise StopIteration();
        result = self.content[myiterable.current_it_count]
        myiterable.current_it_count = myiterable.current_it_count + 1
        return result;

# Lets test 
# Usage
# aritra = myiterable()
# print(next(aritraIterator)) #{'name' : 'aritra'}
# print(next(aritraIterator)) #{'roll' : 123}
# print(next(aritraIterator)) # creates StopIteration exception [hence commented]

aritra = myiterable()

# Add some properties
aritra.add({'name' : 'aritra'})
aritra.add({'roll' : {'a' : 123, 'b': True}})
aritra.add({1 : {'two' : 'three'}})
aritra.add({'otherValues' : {'somemore' : {456 : 'finallValue'}}})
# aritra -> {
# 0: {'name': 'aritra'}, 
# 1: {'roll': {'b': True, 'a': 123}}, 
# 2: {1: {'two': 'three'}}, 
# 3: {'otherValues': {'somemore': {456: 'finallValue'}}}}

aritraIterator = iter(aritra)

# Iterate the iterable and produce values. The values are lazy evaluated.
while(True):
    try:
        print(next(aritraIterator))
    except(StopIteration):
        print('All values printed')
        break

# output:
# {'roll': {'b': True, 'a': 123}}                                                                                                        
# {1: {'two': 'three'}}                                                                                                                  
# {'otherValues': {'somemore': {456: 'finallValue'}}}                                                                                    
# All values printed  
