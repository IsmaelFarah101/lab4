import sqlite3
##import the library and set the database name
db = 'jugglers.db'

def add():
    with sqlite3.connect(db) as conn:
        try:
            ## get the information needed to create the juggler
            name = input('enter the jugglers name: ')
            country = input('enter the country name: ')
            catches = int(input('enter the number of catches: '))
            ##creates the table if it doesnt exist
            conn.execute('create table if not exists jugglers (name text, country text, catches int)')
            ##add the juggler here
            conn.execute('insert into jugglers values (?,?,?)', (name, country, catches))
            print('juggler added')
        ##raise and sqlite or value error here
        except sqlite3.Error as e:
            print(f'Error occured: {e}')
        except ValueError as e:
            print('catches has to be a number')

def search():
    with sqlite3.connect(db) as conn:
        try:
            conn.row_factory = sqlite3.Row
            conn.execute('create table if not exists jugglers (name text, country text, catches int)')
            name = input('enter the name of the juggler: ')
            ##if the user input is empty it just returns everything
            if name == "":
                for row in conn.execute('select * from jugglers'):
                    print(row['name'], row['country'], row['catches'])
            ##if the use specifies a name than it returns the user
            else:
                for row in conn.execute('select * from jugglers where name = ?',(name,)):
                    print(row['name'], row['country'], row['catches'])
        except sqlite3.Error as e:
            print(f'Error occured: {e}')

def update():
     with sqlite3.connect(db) as conn:
        try:
            conn.execute('create table if not exists jugglers (name text, country text, catches int)')
            name = input('enter the name of the juggler: ')
            catches = int(input('enter the new number of catches: '))
            ##query that updates th users catches
            conn.execute('update jugglers set catches = ? where name = ?',(catches,name))
            print('juggler updated')
        ##raise and sqlite or value error here
        except sqlite3.Error as e:
            print(f'Error occured: {e}')
        except ValueError as e:
            print('catches has to a number')
def delete():
    with sqlite3.connect(db) as conn:
        try:
            conn.execute('create table if not exists jugglers (name text, country text, catches int)')
            ##this gets th users name and then deletes the user
            name = input('enter the name of the juggler you want to delete: ')
            conn.execute('delete from jugglers where name = ?',(name,))
            print('juggler deleted')
        except sqlite3.Error as e:
            print(f'Error occured: {e}')

def main():
    ##this is the menu that the user will see
    menu = 'Enter 1 to search juggler\nEnter 2 to add juggler\nEnter 3 to update a juggler\nEnter 4 to delete a juggler\nEnter any other number to quit'
    print(menu)
    try: 
        ##asks the user these questions expecting calls the appropriate function
        ##if user enters anything else the program quits
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
    ##if the user enters a string as a choice
    except ValueError as e:
        print('Enter numbers only')

main()