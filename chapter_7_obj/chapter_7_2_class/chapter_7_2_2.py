class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print('Hello, world! I\'m {}'.format(self.name))

foo = Person()
bar = Person()

foo.set_name('Lucky')
bar.set_name('Kimi')

foo.greet()
bar.greet()

print(foo.name)
