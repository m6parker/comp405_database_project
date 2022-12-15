import sqlite3

connection = sqlite3.connect('projectDB.sqlite')
cursor_obj = connection.cursor()


def all_search(param):
    sql = """SELECT book.title FROM book"""
    print("\nALL BOOKS\n------------------------")
    for row in cursor_obj.execute(sql):
        print(str(row).strip("(,')"))


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
        all_search(param)
    else:
        print("\nBOOKS BY: " + param + "\n------------------------")
        sql = """SELECT book.title FROM book where author like ?"""

        for row in cursor_obj.execute(sql, (param,)):
            print(str(row).strip("(,')"))


def title_search():
    print("\nyou selected SEARCH BY: title")
    # prompts user for an author
    param = input("\nSearch book names to see availability and condition\n(type all for all books) > ")
    if param == "all":
        all_search(param)
    else:
        print("\nBOOK TITLES: " + param + "\n------------------------")
        sql = """SELECT book.title FROM book where title like ?"""
        i = 1
        for row in cursor_obj.execute(sql, (param,)):
            print(str(i), ") ", (str(row).strip("(,')")))
            i = i + 1


def isbn_search():
    print("\nyou selected SEARCH BY: ISBN #")
    # prompts user for an author
    param = input("\nSearch book ISBN to see titles, availability, and condition\n(type all for all books) > ")
    if param == "all":
        all_search(param)
    else:
        # NEED TO FIGURE OUT HOW TO PRINT MULTIPLE COLUMNS
        print("\nBOOK ISBN: " + param + "\n------------------------")
        sql = """SELECT book.ISBN_num FROM book where ISBN_num like ?"""
        i = 1
        for row in cursor_obj.execute(sql, (param,)):
            print(str(i), ") ", (str(row).strip("(,')")))
            i = i + 1


def search_selection():
    print("\nSearch for a book using the following options:\n"
          "1. Author\n2. Title\n3. ISBN #\n4. Availability\n")
    param = input("(type 1, 2, 3, or 4) > ")

    if param == "1":
        author_search()

    elif param == "2":
        title_search()

    elif param == "3":
        isbn_search()

    elif param == "4":
        title_search()

    else:
        print("\ninvalid input\n")
        # resets by calling recursively
        search_selection()


def welcome():
    # what to add:
    # search for a book by: author, title, ISBN, availability
    # functions for each selection
    # need to print multiple columns for more info about search results

    print("\n----welcome message here----")


def main():
    welcome()
    search_selection()

    # connection.close()


if __name__ == '__main__':
    main()
