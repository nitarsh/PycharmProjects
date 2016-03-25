def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def multiple(n, m):
    if (n % m != 0):
        return False
    else:
        return True


def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]


import sys

from collections import deque


# num = int(input("Gimme a number, Dawg!"))
# print "Heres what I got:" , fact(num)

# m = int(input("Gimme a number, Dawg!"))
# n = int(input("Now give a multiple, Yo!"))
#
# if(multiple(n,m)):
#     print "You got brains son! "
# else:
#     print n," aint multiple of ",m, " fool!"
class GameEntry:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return ({0}, {1}).__format__(self._name, self._score)  # e.g., (Bob, 98)


somelist = [1, 2, 4, 8, 16, 32, 64, 128, 256]
# somelist.append("ff")
#
# sometup = (1, 2, 2, 8, 16, 32, 64, 128, 256)
#
# this_set = {1, 2, 13, 24, 7}
#
# str = "Hi my name is Shrinath"
#
# ge = GameEntry(name="Shrinath",score=12)
# print ge.get_name()
#
# print sys.getsizeof(sometup)
#
# for x in this_set:
#     print x, " then"
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     if len(w) > 6 and len(words)<15 :
#         #words.insert(0, w)
#         words.remove(w)
#
# for w in words:
#     print w

# cheeseshop("Limburger", "It's very runny, sir.","It's really very, VERY runny, sir.", shopkeeper='Michael Palin',client="John Cleese",sketch="Cheese Shop Sketch")

somelist.append(512)
somelist.append(1024)
somelist.pop()


def fil1(ffun, list):
    new_list = []
    for l in list:
        if (ffun(l)):
            new_list.append(l)
    return new_list



def f(x): return x == 2 or x == 64


def cube(x): return x * x * x

def add(x1,x2,x3): return x1+x2+x3

def mul(*arg):
    result=1;
    for a in arg:
        result*=a
    return result

def mymap(fun, *arg):
    return [fun(*(array[a] for array in arg)) for a in range(len(arg[0]))]



# print fil1(f, somelist)
#
# print filter(f,map(cube,somelist))

print somelist
print mymap(mul,somelist,somelist,somelist)

# for w in somelist:
#     print w
#
# queue = deque(("name1","name2",'name3'))
# for de in queue:
#     print de
