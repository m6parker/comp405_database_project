import sqlite3

connection = sqlite3.connect('projectDB.sqlite')
cursor_obj = connection.cursor()


def all_search():
    sql = """SELECT book.title FROM book"""
    print("\nALL BOOKS\n------------------------")
    for row in cursor_obj.execute(sql):
        print(str(row).strip("(,')"))

    ask_to_continue()


def author_search():
    print("\nyou selected SEARCH BY: author")
    # this lists all different authors
    list_all_sql = """SELECT distinct author FROM book"""
    print("\nALL AUTHORS\n------------------------")
    for row in cursor_obj.execute(list_all_sql):
        print(str(row).strip("(,')"))
    # prompts user for an author
    param = input("\nSelect an author to find a book (type all for all books) > ")
    if param == "all":
        all_search()
    else:
        print("\nBOOKS BY: " + param + "\n------------------------")
        sql = """SELECT book.title FROM book where author like ?"""

        for row in cursor_obj.execute(sql, (param,)):
            print(str(row).strip("(,')"))

    ask_to_continue()


def title_search():
    print("\nyou selected SEARCH BY: title")
    # prompts user for a title
    param = input("\nSearch book names to see availability and condition\n(type all for all books) > ")
    if param == "all":
        all_search()
    else:
        print("\nBOOK TITLES: " + param + "\n------------------------")
        sql = """SELECT book.title FROM book where title like ?"""
        i = 1
        for row in cursor_obj.execute(sql, (param,)):
            print(str(i), ") ", (str(row).strip("(,')")))
            i = i + 1

    ask_to_continue()


def isbn_search():
    print("\nyou selected SEARCH BY: ISBN #")
    # prompts user for a number
    param = input("\nSearch book ISBN to see titles, availability, and condition\n(type all for all books) > ")
    if param == "all":
        all_search()
    else:
        # NEED TO FIGURE OUT HOW TO PRINT MULTIPLE COLUMNS
        print("\nBOOK ISBN: " + param + "\n------------------------")
        sql = """SELECT book.ISBN_num FROM book where ISBN_num like ?"""
        i = 1
        for row in cursor_obj.execute(sql, (param,)):
            print(str(i), ") ", (str(row).strip("(,')")))
            i = i + 1

    ask_to_continue()


def availability_search():
    print("\nyou selected SEARCH BY: availability")
    # prompts user for rent or buy
    param = input("\nSearch book availability to see titles and condition\n(type rent, buy, or all) > ")
    if param == "all":
        all_search()
    elif param == "rent":
        # NEED TO FIGURE OUT HOW TO PRINT MULTIPLE COLUMNS
        print("\nBOOKS AVAILABLE TO RENT                                 AUTHOR"
              "\n-------------------------------------------------------------------------")
        sql = """SELECT book.title, book.author FROM book where availible_to=\"rent\""""
        i = 1
        for row in cursor_obj.execute(sql):
            val = 70 - len(str(row))
            print(str(i), ") ", (str(row).strip("(,')").replace("', '", val * " ")))
            i = i + 1
    elif param == "buy":
        print("\nBOOKS AVAILABLE TO BUY                                 AUTHOR"
              "\n--------------------------------------------------------------------------")
        sql = """SELECT book.title, book.author FROM book where availible_to=\"buy\""""
        i = 1
        for row in cursor_obj.execute(sql):
            val = 70 - len(str(row))
            print(str(i), ") ", (str(row).strip("(,')").replace("', '", val * " ")))
            i = i + 1
    else:
        print("invalid input")
        availability_search()

    ask_to_continue()


def add_book():
    # INSERT INTO book VALUES(37849, "Stephen King", "Four Past Midnight", "new", "rent")
    print('you are adding a book to the library\nplease insert these values:')
    new_num = input('ISBN #: ')
    new_author = input('author: ')
    new_title = input('title: ')
    new_con = input('condition: ')
    new_avail = input('rent or buy: ')
    sql2 = """INSERT INTO book VALUES(""" + new_num + """, \"""" + new_author + """\", \"""" + \
           new_title + """\", \"""" + new_con + """\", \"""" + new_avail+"""\")"""
    cursor_obj.execute(sql2)
    connection.commit()
    sql = """SELECT book.title FROM book where ISBN_num = """ + new_num
    print("\nNEW BOOK ADDED\n------------------------")
    for row in cursor_obj.execute(sql):
        print(str(row).strip("(,')"))

    ask_to_continue()


def search_selection():
    print("\nSearch for a book using the following options:\n"
          "1. Author\n2. Title\n3. ISBN #\n4. Availability\n5. Add book\n")
    param = input("(type 1, 2, 3, 4 or 5) > ")

    if param == "1":
        author_search()

    elif param == "2":
        title_search()

    elif param == "3":
        isbn_search()

    elif param == "4":
        availability_search()

    elif param == "5":
        add_book()

    else:
        print("\ninvalid input\n")
        # resets by calling recursively
        search_selection()


def ask_to_continue():
    print("\n\nkeep searching or exit?")
    param = input("select y or n >> ")
    if param == 'y':
        search_selection()
    else:
        connection.close()
        exit()


def welcome():
    # what to add:
    # search for a book by: author, title, ISBN, availability
    # functions for each selection
    # need to print multiple columns for more info about search results

    print("\n----welcome message here----")


def main():
    welcome()
    search_selection()


if __name__ == '__main__':
    main()
