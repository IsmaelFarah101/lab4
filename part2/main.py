from peewee import *
import sqlite3 
##importing the needed packages and set the database name
db = SqliteDatabase('jugglers.db')

class Jugglers(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db

db.connect()

db.create_tables([Jugglers])

def search():
    try:
        ##if the name is empty than the query returns everyting else it returns the specified user
        name = input('Enter the name of the juggler: ')
        if name == "":
            jugglers = Jugglers.select()
            for juggler in jugglers:
                print(juggler.name,juggler.country,juggler.catches)
        else:
            juggler = Jugglers.select().where(Jugglers.name == name)
            for row in juggler:
                print(row)
    ## raises any potential errors
    except sqlite3.Error as e:
        print(f'Error occured: {e}')

def add():
    try:
        ##gets the juggler data from user
        name = input('enter the name of the juggler: ')
        country = input('enter the country of the juggler: ')
        catches = int(input('Enter the number of catches: '))
        ##creates and saves the juggler
        juggler = Jugglers(name=name, country=country, catches=catches)
        juggler.save()
        print('juggler created')
    ##raises input and sqlite error
    except ValueError as e:
        print('catches has to be a number') 
    except sqlite3.Error as e:
        print(f'Error occured: {e}')
def update():
    try:
        ##gets the name and catches
        name = input('enter the name of the juggler: ')
        catches = input('enter the new number of catches: ')
        ##update the juggler
        Jugglers.update(catches=catches).where(Jugglers.name == name).execute()
        print('juggler updated')
    ##raises input and sqlite error
    except ValueError as e:
        print('catches has to be a number')
    except sqlite3.Error as e:
        print(f'Error occured: {e}')
def delete():
    try:
        name = input('enter the name of the juggler: ')
        Jugglers.delete().where(Jugglers.name == name).execute()
        print('juggler deleted')
    ##raises sqlite error
    except sqlite3.Error as e:
        print(f'Error occured: {e}')

def main():
    ##create and print the menu
    menu = 'Enter 1 to search juggler\nEnter 2 to add juggler\nEnter 3 to update a juggler\nEnter 4 to delete a juggler\nEnter any other number to quit'
    print(menu)
    try: 
        ##gets the choice number and calls the appropriate function
        choice = int(input('Enter choice: '))
        while choice:
            if choice == 1:
                search()
                choice = int(input('Enter choice: '))
            elif choice == 2:
                add()
                choice = int(input('Enter choice: '))
            elif choice == 3:
                update()
                choice = int(input('Enter choice: '))
            elif choice == 4:
                delete()
                choice = int(input('Enter choice: '))
            else:
                break
    ##if the user enters a string
    except ValueError as e:
        print('Enter numbers only')
main()