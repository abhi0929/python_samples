class book:
    total_books=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        book.total_books +=1
@classmethod
def from_string(cls,book_str):
    title, author = book_str.split("-")
    return cls(title,author)
@staticmethod
def is_valid_title(title):
    return len(title) >=3

bts = "harrypoter - j.k.rowling"
b1 = book.from_string(cls,book_str)

b2 = book("ice and fire","martin")
