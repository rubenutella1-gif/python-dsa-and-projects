# class demo():
#     def __init__(self,a,b):
#         self.__a=a #private
#         self._b=b #protected
# class demo2(demo):
#     def output(self):
#         print(self._b)

# d=demo2(2,4)
# d.output()
def demo(a,b):
    print(a+b)
    
demo(1,2)
demo('a','b')
demo([1,23,3],[22,31,42])
demo((1,23,3),(22,31,42))