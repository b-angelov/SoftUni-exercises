
class Calculator:

    @staticmethod
    def add(*args):#- sums all the arguments passed to the function and returns the result
        return sum (args)
    @staticmethod
    def multiply(*args):#- multiplies all the numbers and returns the result
        res = 1
        for arg in args:
            res *= arg
        return res
    @staticmethod
    def divide(*args):#- divides all the numbers (starting from the first one) and returns the result
        res = 0
        for arg in args:
            if not res:
                res = arg
                continue
            res /= arg
        return res

    @staticmethod
    def subtract(*args):#- subtracts all the numbers (starting from the first one) and returns the result
        res = 0
        for arg in args:
            if not res:
                res = arg
                continue
            res -= arg
        return res

print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))



