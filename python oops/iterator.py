# t=("mango","banana","apple")
# m=iter(t)
# print(next(m))
# print(next(m))
# print(next(m))
class MyClass:
    def __iter__(self):
        self.a=1
        
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
student=MyClass()
myiter=iter(student)
print(next(myiter))  
print(next(myiter)) 
print(next(myiter)) 
print(next(myiter)) 
print(next(myiter)) 
print(next(myiter))   