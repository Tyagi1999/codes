# asked by Jane Street
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns
# the first and last element of that pair. For example, car(cons(3, 4))
# returns 3, and cdr(cons(3, 4)) returns 4.
# Given this implementation of cons:

"""def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair"""
# Implement car and cdr.


def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def car(func):
    return func(lambda x,y:x)

def cdr(func):
    return func(lambda x,y:y)

def main():
    x=int(input("enter the first number: "))
    y=int(input("enter the second number: "))
    print("car returns {0}".format(car(cons(x,y))))
    print("cdr returns {0}".format(cdr(cons(x,y))))

if __name__=='__main__':
    main()
