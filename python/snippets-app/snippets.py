import logging
import argparse
import sys
import psycopg2
import psycopg2.extras

# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

# Connect to the database from python
logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect("dbname='snippets' host='localhost'")
logging.debug("Database connection established")


def get(name):
    """Retrieve the snippet with a given name."""
    while True:
        logging.info("Retrieving snippet {}".format(name))
        with connection.cursor() as cursor:
            cursor.execute(
                "select message from snippets where \
                    hidden=False AND keyword=%s", (name,))
            row = cursor.fetchone()
        logging.debug("Snippet retrieved successfully.")
        if not row:
            ans = raw_input(
                "Snippet doesn't exist. Would you like to create it? (yes/no) ")
            lower_ans = ans.lower()
            if lower_ans == 'yes':
                name = str(raw_input('Enter the snippet name: '))
                snippet = str(raw_input('Enter the snippet message: '))
                put(name, snippet)
            else:
                return "Snippet does not exist."
                break
        else:
            return row[0]
            break


def push(name, snippet, hide=False):
    """Store a snippet with an associated name."""
    logging.info("Storing snippet {}: {}".format(name, snippet))
    with connection.cursor() as cursor:
        cursor.execute(
            "insert into snippets values (%s, %s, %s)",
            (name, snippet, hide)
        )
        logging.debug("Snippet stored successfully.")
        connection.commit()
        return name, snippet


def put(name, snippet, hide=False):
    """Update a snippet with an associated name."""
    logging.info("Storing snippet {}: {}".format(name, snippet))
    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "insert into snippets values (%s, %s, %s)",
                (name, snippet, hide))
        except psycopg2.IntegrityError:
            connection.rollback()
            cursor.execute(
                "update snippets set message=%s, hidden=%s where keyword=%s",
                (snippet, hide, name))
        connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet


def catalog():
    """Query the available keywords from the snippets table."""
    logging.info("Querying the database")
    with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        cursor.execute(
            "select keyword from snippets where hidden=False \
            order by keyword ASC")
        rows = cursor.fetchall()
        for row in rows:
            print row['keyword']
    logging.debug("Query complete")


def search(string):
    """Return a list of snippets containing a given string"""
    logging.info("Searching snippets for {}".format(string))
    with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        # I needed the % signs because ...
        cursor.execute(
            "select * from snippets where hidden=False \
                AND message like '%%'||%s||'%%'", (string,))
        rows = cursor.fetchall()
        for row in rows:
            print row['message']
    logging.debug("Search complete")


def main():
    """Main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(
        description="Store and retrieve snippets of text")

    subparsers = parser.add_subparsers(
        dest="command", help="Available commands")

    # Subparser for the push command
    logging.debug("Constructing push subparser")
    put_parser = subparsers.add_parser("push", help="Store a new snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    put_parser.add_argument(
        "--hide", help="Sets the hidden column to True", action="store_true")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    put_parser.add_argument(
        "--hide", help="Sets the hidden column to True", action="store_true")

    # Subparser for the catalog command
    logging.debug("Constructing catalog subparser")
    subparsers.add_parser("catalog", help="Query snippet keywords")

    # Subparser for the search command
    logging.debug("Constructing search subparser")
    search_parser = subparsers.add_parser(
        "search", help="Search snippets for a string")
    search_parser.add_argument(
        "string", help="The string you are searching for")

    # Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    get_parser.add_argument("name", help="The name of the snippet")

    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "push":
        name, snippet = put(**arguments)
        print("Stored {} as {}.".format(snippet, name))
    elif command == "put":
        name, snippet = put(**arguments)
        print("Stored {} as {}.".format(snippet, name))
    elif command == "get":
        snippet = get(**arguments)
        print("Retrieved snippet: {}".format(snippet))
    elif command == "catalog":
        catalog()
        print("Retrieved keywords")
    elif command == "search":
        search(**arguments)
        print
        print("Search complete")
        print("Found {} in these messages".format(sys.argv[2]))


if __name__ == "__main__":
    main()
