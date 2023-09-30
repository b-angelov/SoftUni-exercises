def math_operations(*args,**kwargs):
    args = list(args)
    operations = {"a":lambda a,b: a+b,"s":lambda a,b:b-a,"d":lambda a,b:b/a if a != 0 else b,"m": lambda a,b: a*b}
    while args:
        for key,val in kwargs.items():
            num = args.pop(0)
            kwargs[key] = operations[key](num,val)
            if not args:
                break
    res = sorted(kwargs.items(), key= lambda x: (-x[1],x[0]))
    return '\n'.join(f"{key}: {value:.1f}" for key,value in res)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print()
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print()
print(math_operations(6.0, a=0, s=0, d=5, m=0))
