import logging
import argparse
import sys
import psycopg2
import psycopg2.extras

# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

# Connect to the database from python
logging.debug("Connecting to PostgreSQL")
# connection = psycopg2.connect("dbname='snippets' user='action' host='localhost'")
connection = psycopg2.connect("dbname='snippets' host='localhost'")
logging.debug("Database connection established")


def put(name, snippet, hide=False):
    """Store a snippet with an associated name."""
    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    with connection, connection.cursor() as cursor:
        try:
            cursor.execute("insert into snippets values (%s, %s, %s)", (name, snippet, hide))
        except psycopg2.IntegrityError as e:
            connection.rollback()
            cursor.execute("update snippets set message=%s where keyword=%s", (snippet, name))
        connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet


def catalog():
    """Query the available keywords from the snippets table."""
    logging.info("Querying the database")
    with connection, connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        cursor.execute("select keyword from snippets where hidden=False order by keyword ASC")
        rows = cursor.fetchall()
        for row in rows:
            print row['keyword']
    logging.debug("Query complete")


def search(string):
    """Return a list of snippets containing a given string"""
    logging.info("Searching snippets for {!r}".format(string))
    with connection, connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        # I needed the % signs because ...
        cursor.execute("select * from snippets where message like '%%'||%s||'%%'", (string,))
        rows = cursor.fetchall()
        for row in rows:
            print row['message']
    logging.debug("Search complete")


def get(name):
    """Retrieve the snippet with a given name."""
    logging.info("Retrieving snippet {!r}".format(name))
    with connection, connection.cursor() as cursor:
        cursor.execute("select message from snippets where keyword=%s", (name,))
        row = cursor.fetchone()
    logging.debug("Snippet retrieved successfully.")
    if not row:
        ans = raw_input('Would you like to create it? ')
        if ans == 'yes':
            print "ok, we can do that"
            # put(name, snippet)
        else:
            # break?
            print "ok, nevermind"
    else:
        return row[0]


def main():
    """Main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    put_parser.add_argument("--hide", help="Sets the hidden column to True", action="store_true")

    # Subparser for the catalog command
    logging.debug("Constructing catalog subparser")
    catalog_parser = subparsers.add_parser("catalog", help="Query snippet keywords")

    # Subparser for the search command
    logging.debug("Constructing search subparser")
    search_parser = subparsers.add_parser("search", help="Search snippets for a string")
    search_parser.add_argument("string", help="The string you are searching for")

    # Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    get_parser.add_argument("name", help="The name of the snippet")

    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print("Stored {!r} as {!r}.".format(snippet, name))
    elif command == "get":
        snippet = get(**arguments)
        print("Retrieved snippet: {!r}".format(snippet))
    elif command == "catalog":
        keywords = catalog()
        print("Retrieved keywords")
    elif command == "search":
        search(**arguments)
        print
        print("Search complete")
        print("Found {!r} in these messages".format(sys.argv[2]))
if __name__ == "__main__":
    main()
