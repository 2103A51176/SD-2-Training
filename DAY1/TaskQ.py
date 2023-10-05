class parent:
    pass

class child1(parent):
    def _init_(self, a):
        self.a = a

    def magicalPrimes(self):
        num = str(self.a)
        num = int(num[::-1])
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


class child2(parent):
    def _init_(self, a):
        self.a = a

    def neonNumbers(self):
        sq = str(self.a**2)
        s = 0
        for i in sq:
            s += int(i)
        if s == self.a:
            return True
        else:
            return False


c = child1(41)
result = c.magicalPrimes()
if result:
    print("The number is magical primes")
else:
    print("The number is not magical primes")


d = child2(9)
result = d.neonNumbers()
if result:
    print("The number is neon number")
else:
    print("The number is not neon number")
