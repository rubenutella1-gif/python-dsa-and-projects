class Member:
    def __init__(self,member_id,name,email):
        self.member_id=member_id
        self.name=name
        self.email=email
        self.borrowed_books=[]
    def display_member(self):
        return self.member_id,self.name,self.email,self.borrowed_books