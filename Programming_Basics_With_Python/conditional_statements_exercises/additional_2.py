import matplotlib.pylab as p

percent = [35, 25 ,20, 10, 10]
languages =["Python",'Java','C++','Go','JavaScript']

p.pie(percent, labels=languages)
p.show()
