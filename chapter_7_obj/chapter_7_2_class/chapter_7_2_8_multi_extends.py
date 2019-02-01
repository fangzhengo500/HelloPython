class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print("Hi, my value is", self.value)


class TC(Calculator, Talker):
    pass


tc = TC()
tc.calculate('1+2*3')
tc.talk()

print(TC.__bases__)
