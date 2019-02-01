class MemberCounter:
    members = 0;

    def init(self):
        MemberCounter.members += 1

m1 = MemberCounter()
m2 = MemberCounter()

m1.init()
print(MemberCounter.members)
m2.init()
print(MemberCounter.members)
print()
print(m1.members)
print(m2.members)
print()
m1.members = 'm2'   # 遮盖类级别变量
print(m1.members)
print(m2.members)
print()
