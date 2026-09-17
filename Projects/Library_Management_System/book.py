class Book:
    def __init__(self,book_id,title,author,category,is_available):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.category=category
        self.is_available=is_available
    def display_book(self):
        return  self.book_id,self.title,self.author,self.category,self.is_available
    def borrow(self):
        if self.is_available:
            self.is_available=False
            print("Book borrowed successfully ")
        else:
            print("Book is already borrowed ")
    def return_book(self):
        if not self.is_available:
            self.is_available=True
            print("Book returned successfully ")
        else:
            print("Book already returned")
book1 = Book(
    "B101",
    "Python Basics",
    "John",
    "Programming",
    True
)
print(book1.display_book())
book1.borrow()
book1.borrow()
book1.return_book()
print(book1.display_book())