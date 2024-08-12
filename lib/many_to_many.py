class Author:
    # Class attribute 
    all = []
    def __init__(self, name): 
        self.name = name 
        Author.all.append(self)
       

    def __repr__(self):
        return f"Author's name={self.name}"
    
    def contracts(self):
        # getting all that contracts that are associated with the author 
        return [contract for contract in Contract.all if contract.author == self]
        
    def books(self): 
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalities):
        return Contract(self, book, date, royalities)      
    
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Book:
    all= []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
   
    
    def __repr__(self):
        return f"The title of the book {self.title}"
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]
    
    def sign_contract(self, author, date, royalities):
        return Contract(self, author, date, royalities)


class Contract:
    # Class attribute
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author 
        self.book = book 
        self.date = date 
        self.royalties = royalties
        Contract.all.append(self)
    
# These are checks and balances in order to check the user's work 
    @property 
    def author(self):
        return self._author    
    @author.setter
    def author(self, value):
        if (isinstance (value, Author)):
            self._author = value 
        else: 
            raise Exception("value must be an instance of the Author class")
    
    @property 
    def book(self):
        return self._book    
    @book.setter
    def book(self, value):
        if (isinstance (value, Book)):
            self._book = value 
        else: 
            raise Exception("value must be an instance of the book class")
    

    @property 
    def date(self):
        return self._date 
    @date.setter
    def date(self, value):
        if (isinstance (value, str)):
            self._date = value 
        else: 
            raise Exception("value must be a string")

    @property 
    def royalties(self):
        return self._royalties 
    @royalties.setter
    def royalties(self, value):
        if (isinstance (value, int)):
            self._royalties = value 
        else: 
            raise Exception("value must be an integer")

    
    @classmethod
    def contracts_by_date(cls, date):
         return [contract for contract in cls.all if contract.date == date]