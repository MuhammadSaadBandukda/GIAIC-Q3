class Book:
    total_book = 0

    @classmethod
    def increment_book(cls):
        cls.total_book+=1


b = Book()
print(b.total_book)
b.increment_book()
print(b.total_book)
b.increment_book()
print(b.total_book)
b.increment_book()
print(b.total_book)
b.increment_book()
print(b.total_book)
b.increment_book()