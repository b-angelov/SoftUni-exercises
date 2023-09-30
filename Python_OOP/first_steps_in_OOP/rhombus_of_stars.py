class RhombusOfStars:
    def __init__(self,n):
        self.n = n
        self.out()

    def row(self,n):
        if n == 1:
            return
        spaces = " " * (n - 1)
        stars = (self.n - len(spaces)) * "* "
        print(spaces + stars)

    def out(self):
        n = self.n
        while abs(n) <= self.n:
            self.row(abs(n))
            n -= 1

RhombusOfStars(int(input()))
