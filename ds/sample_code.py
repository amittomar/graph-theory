from russell_paradox import MySet
def multiple_of_thre(n):
    return n % 3 == 0


fizz = MySet(multiple_of_thre)

assert (3 in fizz)
assert (3 in fizz)
assert (not 5 in fizz)

Buzz = MySet(lambda x: x % 5 == 0)
assert (5 in Buzz)
assert (67215721535815 in Buzz)

fizz_buzz = fizz and Buzz
assert (15 in fizz_buzz)
assert (6 not in fizz_buzz)

