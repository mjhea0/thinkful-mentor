import pdb


#####
#simple decorator
def one_adder(func):
    def inner(a):
        ret = func(a)
        return ret + 1
    return inner


@one_adder
def barney(a) :
    return a * a


print barney(2)

#################################
# this is a little contrived

def span(func):
    def inner(txt):
        ret = func(txt)
        return "<span>{}</span>".format(ret)
    return inner

@span
def upper(txt):
    return txt.upper()

print upper("hello")

################################
# this might be more realistic

def http_handler(func):
    def inner(*args):
        ret = func(*args)
        #pdb.set_trace()
        response = """
        HTTP/1.1 {status}
        Content-Type: {content_type}; charset={charset}
        Content-Length:{content_length}

        {content}
        """.format(status = ret["status"], content_type=ret["content_type"],
         charset= ret["charset"], content_length=len(ret["content"]), content=ret["content"])
        return response
    return inner

@http_handler
def index(username):
    if username:
        content = "Hello {}".format(username)
    else:
        content = "Hi there, please log in."
    
    return {
        "content" : content,
        "status" : 200,
        "content_type":"text/html",
        "charset" : "utf8"
    }

print index("Sam")
print index(None)

##################################