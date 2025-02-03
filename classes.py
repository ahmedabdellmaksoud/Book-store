from abc import ABC ,abstractmethod 

# definetion of the 'Item' abstract MAIN class
class Item(ABC):
    _numberofitems = 0

    def __init__(self, title, author, price):
        self._title = title
        self._author = author
        if price < 0:
            raise ValueError
        else:
            self._price = price
        Item._numberofitems += 1

    @abstractmethod
    def search_by_title():
        pass

    @abstractmethod
    def search_by_author():
        pass

    @abstractmethod
    def buy():
        pass

#return the whole number of items in the book store
    @staticmethod
    def number_of_items():
        print( Item._numberofitems)

    def get_details(self):
        print(f"Info: \n\n\tTitle: {self._title} \n\tAuthor: {self._author} \n\tPrice: {self._price} ")

    def update_price(self, new_price):
        self._price = new_price

    def Price(self):
        return self._price



#define Book subclass 
class Book(Item):
    _titles = []
    _authors = []
    _numberofBooks = 0
    _mini_data_base = {}

    def __init__(self, title, author, price, ISBN, number_of_pages ,number_of_books ):
        super().__init__(title, author, price)
        if len(ISBN) != 13 :
            raise ValueError
        else:
            self._ISBN = ISBN
        self.number_of_pages = number_of_pages
        self.number_of_books = number_of_books
        Book._titles.append(title)
        Book._authors.append(author)
        Book._numberofBooks += 1

    def buy(self):
        if(self.number_of_books <= 0):
            raise ValueError 
        else :
            print(f"You have bought {self._title}")
            self.number_of_books -= 1
            if self.number_of_books == 0:
                Book._titles.remove(self._title)

# return number of Books in the store
    @staticmethod
    def number_of_books():
        return Book._number_of_Books

    @staticmethod
    def _Titles():
        for i in range(len(Book._titles)):
            print (i+1 ,f"- {Book._titles[i]}")
#use class method

    @staticmethod
    def search_by_author(author):
        if author in Book._authors :
            print('Yes')
        else :
            print('No')

    @staticmethod
    def search_by_title(title):
        if title in Book._titles :
            print('Yes')
        else :
            print('No')

#define magazine subclass
class Magazine(Item):
    _titles = []
    _authors = []
    _number_of_magazines = 0
    _mini_data_base = {}


    def __init__(self, title, author, price, issue_num, publication_Date, editor, number_of_magazines):            
        super().__init__(title,author,price)
        self.issue_num = issue_num
        self.publication_Date = publication_Date
        self.editor=editor
        self.number_of_magazines = number_of_magazines
        Magazine._titles.append(title)
        Magazine._authors.append(author)
        Magazine._number_of_magazines += 1

    def buy(self):
        if(self.number_of_magazines <= 0):
            raise ValueError 
        else :
            print(f"You have bought {self._title}")
            self.number_of_magazines -= 1

    @staticmethod
    def _Titles():
        for i in range(len(Magazine._titles)):
            print (i+1 ,f"- {Magazine._titles[i]}")

# return number of Magazines in the store
    @staticmethod
    def _number_of_Magazines():
        return Book._number_of_magazines

    @staticmethod
    def search_by_author(author):
        if author in Magazine._authors :
            print('Yes')
        else :
            print('No')

    @staticmethod
    def search_by_title(title):
        if title in Magazine._titles :
            print('Yes')
        else :
            print('No')

    def get_details(self):
        print("Magazine's", end= " ")
        super().get_details()
        print( f"\tIssue Number: {self.issue_num} \n\tPublication Date: {self.publication_Date} \n\tEditor: {self.editor}\n\tNumber of Magazines: {self.number_of_magazines}\n")

#define dvd subclass 
class dvd(Item):
    _titles = []
    _authors = []
    _genres = []
    _numberofdvds = 0
    _mini_data_base = {}

    def __init__(self, title, author, price, director, duration, genre, number_of_DVDs):
        super().__init__(title, author, price)
        self.director = director
        self.duration = duration
        self.genre = genre
        self.number_of_DVDs = number_of_DVDs
        dvd._titles.append(title)
        dvd._authors.append(author)
        dvd._genres.append(genre)
        dvd._numberofdvds += 1

    def buy(self):
        if(self.number_of_DVDs <= 0):
            print("Sorry, No Books Avilable Right Now:( \n\tCome Bach Later :)")
            raise ValueError 
        else :
            print(f"You have bought {self._title}")
            self.number_of_DVDs -= 1

    @staticmethod
    def search_by_genres(genre):
        if genre in dvd._genres :
            print('Yes')
        else :
            print('No')

    @staticmethod
    def search_by_author(author):
        if author in dvd._authors :
            print('Yes')
        else :
            print('No')

    @staticmethod
    def search_by_title(title):
        if title in dvd._titles :
            print('Yes')
        else :
            print('No')    

    @staticmethod
    def _Titles():
        for i in range(len(dvd._titles)):
            print (i+1 ,f"- {dvd._titles[i]}")

# return number of DVDs in the store
    @staticmethod
    def number_of_dvds():
        print( dvd._numberofdvds)

    def get_details(self):
        print("DVD's" ,end= " ")
        super().get_details()
        print (f"\tDirector: {self.director} \n\tDuration: {self.duration} \n\tGenre: {self.genre}\n")

#test the production

d1 = dvd("Noniat Al-Qahtani", "Al-Qahtani", 0 , "Monshed", "55:15" ,"Nashid" ,4533 )
d2 = dvd("Lord of The Rings", "amazing author", 1233 ,"Amazing staff" ,"3:55:20", "Movie" ,44)
d3 = dvd("Sahih AL-Bukhari", "Bukhari", 1500, "mohamed sami", "3 min", "Dars", 200)
dvd._mini_data_base["Noniat Al-Qahtani"] = d1 
dvd._mini_data_base["Lord of The Rings"] = d2
dvd._mini_data_base["Sahih AL-Bukhari"] = d3


b1 = Book("Sahih AL-Bukhari", "Bukhari", 1500 ,"1234656789012", 3600, 20 )
b2 = Book("Al-ekna3" , "Al-Shaf3i" , 230 , "1234567890123" , 300 ,55)
b3 = Book("Nader Fouda" , "Ahed Younis" , 45 , "0123456789123",215 ,1)
Book._mini_data_base["Sahih AL-Bukhari"] = b1
Book._mini_data_base["Al-ekna3"] = b2
Book._mini_data_base["Nader Fouda"] = b3

m1 = Magazine("Capitalism","doctor",123 ,456,2024,"No one",15)
m2 = Magazine("communism","Someone",320,457,2024,"No one",144)
m3 = Magazine("Sahih AL-Bukhari", "Bukhari", 1500, "9090890", "2005", "king batman" ,20)
Magazine._mini_data_base["Capitalism"] = m1
Magazine._mini_data_base["communism"] = m2
Magazine._mini_data_base["Sahih AL-Bukhari"] = m3

