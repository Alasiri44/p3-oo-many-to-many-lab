from datetime import datetime
class Author:
    related_royalties = 0
    authors = []
    
    def __init__(self, name):
        self.name = name
        Author.authors.append(self)
                
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties )
               
        
    def total_royalties(self):
        for contract in self.contracts():
            Author.related_royalties += contract.royalties
        return Author.related_royalties

class Book:
    books = []
    def __init__(self, title):
        self.title = title
        Book.books.append(self)
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []
    def __init__(self, author, book, contract_date, royalties):
        self.author = author
        self.book = book
        self.date = contract_date
        self.royalties = royalties
        Contract.all.append(self)
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception('Author must be an instance of Author Class')
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception('Book must be an instance of Book Class')
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, contract_date):
        if isinstance(contract_date, str):
            self._date = contract_date
        else:
            raise Exception('Date must be of type string')
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception('Royalties must be of type integer')
        
    @classmethod
    def contracts_by_date(cls, date):      
        return [contract for contract in cls.all if contract.date == date]  
            
