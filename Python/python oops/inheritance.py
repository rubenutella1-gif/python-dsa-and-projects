# class grandfather():
#     def outputgf(self):
#         print("I am the Grandfather")
        
# class parent(grandfather):
#     def output(self):
#         print("I am the Parent")
    
# class child(parent):
#     def outputc(self):
#         print("I am the child")
        
# obj=child()
# obj.output()
# obj.outputc()
# obj.outputgf()

# class father():
#     def output(self):
#         print("I am the Father")
# class mother():
#    def outputgf(self):
#         print("I am the Mother")
    
# class child(mother,father):
#     def outputc(self):
#         print("I am the child")
        
# obj=child()
# obj.output()
# obj.outputc()
# obj.outputgf()

class father():
    def output(self):
        print("I am the Father")
class child1(father):
   def outputgf(self):
        print("I am the child1")
    
class child2(father):
    def outputc(self):
        print("I am the child2")
        
obj=child1()
obj2=child2()
obj.output()
obj2.output()
obj.outputgf()
obj2.outputc()