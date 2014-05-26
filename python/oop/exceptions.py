import requests

def my_function():
    try:
        r = requests.get("cnn.com")
        r.status_code
    except requests.exceptions.ConnectionError:
        return "bla"



def main():
    x = my_function()
    if x == "blah":
        # something happens
    else:



if __name__ == '__main__':
    main()
