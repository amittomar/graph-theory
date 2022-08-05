class MySet:
    def __init__(self, member_test) -> object:
        self.member_test = member_test

    def __contains__(self, item):
        return self.member_test(item)

    def __and__(self, other):
        return  MySet(lambda x: x in self and x in other)



def multiple_of_thre(n):
    return n % 3 == 0
fizz = MySet(multiple_of_thre)

def doesnt_contain_self(X):
    try:
        return  X not in X
    except TypeError:
        return True

Barber = MySet(doesnt_contain_self)
assert (fizz in Barber)

W = MySet(None)
W.member_test = lambda x: x in W

assert (W in W)

# Uncomment below line to go out of Stack trace
# print("BArber in BArber ", Barber in Barber)
print("okay")