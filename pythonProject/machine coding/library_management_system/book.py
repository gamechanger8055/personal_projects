class Book:
    def __init__(self,id,title):
        self.id=id
        self.title=title
        self.author= []
        self.pub= []
        self.book_copy={}

    def add_book_copy(self, book_copy):
        self.book_copy[self.id]=book_copy



