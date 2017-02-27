class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
        
    def top3(self):
        return sorted(set([t for t in self.times]))[0:3]
    

sarah = Athlete('Sarah Sweeney', '2017-02-22', ['2:28','1:56','2:22','2:28','3:00'])
print(sarah.top3())

class NamedList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name
        
        
john = NamedList("John")
print('a')