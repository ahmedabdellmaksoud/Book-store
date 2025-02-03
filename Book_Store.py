from classes import Book ,Magazine ,dvd
import os , time

def clear_screan():
    return os.system( "cls" if os.name == "nt" else "clear" )
class Book_store( Book , Magazine , dvd ):

    @staticmethod
    def menu():
        print('\t\tHello to our Book Store "E-JUST Library"')
        print("Choose A Catagory ")
        print("\t1-Books \n\t2-DVDs \n\t3-Magazines")
        choices = {
            1: Book_store.Book_menu,
            2: Book_store.dvd_menu,
            3: Book_store.magazine_menu
        }
        choice = Book_store.choice_menu(3)
        choices[choice]()

    @staticmethod
    def second1( n , c ):
        print("What you want to do ?\n")
        print("\t1- Buy \n\t2- Main Menu\n\t3-Details \n\t4- Quit")
        choice = Book_store.choice_menu(4)
        if choice == 1: # Buy
                Book_store.__BUY(n , c)
        elif choice == 2:
            clear_screan()
            Book_store.menu()
        elif choice == 3:
            Book_store.Get_Details(n,c)
        else:
            time.sleep(3)
            print("Good Bye")
            time.sleep(3)
            clear_screan()

    @staticmethod
    def second2( n , c ):
        print("is there anthing you want to do ?\n")
        print("\t1- Buy \n\t2- Main Menu\n\t3- Details \n\t4- Quit")
        choice = Book_store.choice_menu(4)
        if choice == 1: # Buy
                Book_store.__BUY(n , c)
        elif choice == 2:
            clear_screan()
            Book_store.menu()
        elif choice == 3:
            Book_store.Get_Details( n , c )
        else:
            print("Good Bye")
            time.sleep(3)
            clear_screan()

    @staticmethod
    def choice_menu(max):
        try :
            choice = int(input())
            if choice > max or choice <1:
                raise TypeError
    
        except ValueError:
            print("Write Numbers Only  ")
    
        except TypeError:
            print(f"Number Must be from '1' to '{max}'  ")
        
        else:
            return choice
        

    @staticmethod
    def magazine_menu():
        print("="*30)
        Magazine._Titles()
        print("="*30)
        c = Book_store.__item_menu()
        Book_store.second1(3 , c)

    @staticmethod
    def Book_menu():
        print("="*30)
        Book._Titles()
        print("="*30)
        c = Book_store.__item_menu()
        Book_store.second1(1 , c)

    @staticmethod
    def dvd_menu():
        print("="*30)
        dvd._Titles()
        print("="*30)
        c = Book_store.__item_menu()
        Book_store.second1(2 , c )

    @staticmethod
    def __item_menu():
        while True:
            c = input("Choose One\t\n")
            if c.isdigit() and int(c) > 0 and int(c) <= len(dvd._titles):
                return int(c)
            else :
                print(f"Enter a valid number bitween 1 and {len(dvd._titles)}\n")

    @staticmethod
    def __BUY( n , c ):
        choices ={
            1 : Book._mini_data_base[Book._titles[c-1]].buy,
            2 : dvd._mini_data_base[dvd._titles[c-1]].buy,
            3 : Magazine._mini_data_base[Magazine._titles[c-1]].buy
        }
        choices[n]()
        time.sleep(2)
        clear_screan()
        Book_store.second2(n,c)

    @staticmethod
    def Get_Details(n,c):
        choices ={
            1 : Book._mini_data_base[Book._titles[c-1]].get_details,
            2 : dvd._mini_data_base[dvd._titles[c-1]].get_details,
            3 : Magazine._mini_data_base[Magazine._titles[c-1]].get_details
        }
        clear_screan()
        choices[n]()
        time.sleep(2)
        Book_store.second2(n,c)

Book_store.menu()