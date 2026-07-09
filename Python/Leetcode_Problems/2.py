#Add two numbers using linkedlist
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    def AddTwoNumbers(self,l1,l2):
        dummy=ListNode()
        current=dummy
        carry=0
        
        while l1 or l2 or carry:
            
            if l1:
                x=l1.val
            else:
                x=0
                
            if l2:
                y=l2.val
            else:
                y=0
                
            total=x+y+carry
            
            carry=total//10
            
            digit=total%10
            
            current.next=ListNode(digit)
            
            current=current.next
            if l1:
                l1=l1.next
                
            if l2:
                l2=l2.next
                
        return dummy.next
    
l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)

l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)

obj=Solution()
result=obj.AddTwoNumbers(l1,l2)

print("Result Linked List:")

while result:
    print(result.val, end=" -> ")
    result = result.next

print("None")
