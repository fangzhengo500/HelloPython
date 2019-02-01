class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPANMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']


f = Filter()
f.init()
print(f.filter([1, 2, 3]))

s = SPANMFilter()
s.init()
print(s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']))