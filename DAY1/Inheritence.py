class Siva:
    def c1(etc):
        print("i am c1 method")
    def c2(etc):
        print("i am c2 method")
class Baby1(Siva):
    def d1(etc):
        print("i am d1 method")
class Baby2(Siva):
    def i(etc):
        print("method i")
class Gbaby(Baby1):
    def m(etc):
        print("i am m method")
x=Baby2()
x.c1()
x.c2()
x.i()
y=Gbaby()
y.c1()
y.c2()
y.d1()
y.m()
