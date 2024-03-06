class Library:
    def __init__(self, racks):
        self.books={}
        self.racks=racks
        self.ctr=0
        self.p={}

    def add_books(self,book):
        self.ctr+=len(book.book_copy)
        if self.ctr>=self.racks:
            print("rack not available")
            return
        for copy in book.book_copy:
            self.p[copy.id]=copy
        self.books[book.id]=book

    def remove_books(self,bc_id):
        del self.p[bc_id]

    def search_books(self,id):
        return self.books[id]