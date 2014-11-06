/* Node.js Crypt(3) implementation */

#include <node.h>
#include <v8.h>

#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <nan.h>

using namespace v8;

/* GetApacheSalt: generates 2 char salt. */
const char* GetApacheSalt()
{
    char *salt = new char[3];
    const char *const saltchars = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

    /* Using current time as seed. */
    srand(time(NULL));

    /* Pick two random chars from saltchars. */
    salt[0] = saltchars[rand() % 64];
    salt[1] = saltchars[rand() % 64];
    salt[2] = '\0';

    return salt;
}

NAN_METHOD(Method) {
	NanScope();

    if (args.Length() == 0) {
        NanTypeError("Password is required");
        NanReturnUndefined();
    }

    if (!args[0]->IsString() || (args.Length() > 1 && !args[1]->IsString())) {
        NanTypeError("Wrong arguments");
        NanReturnUndefined();
    }


    v8::String::Utf8Value password(args[0]->ToString());
    v8::String::Utf8Value salt(args.Length() > 1 ? args[1]->ToString() : NanNew<String>(GetApacheSalt()));

    Local<String> res = NanNew<String>( crypt(*password, *salt ) );
    NanReturnValue(res);
}

void init(Handle<Object> exports) {
	exports->Set(NanNew<String>("crypt"), NanNew<FunctionTemplate>(Method)->GetFunction());
}

NODE_MODULE(crypt3, init)

/* EOF */