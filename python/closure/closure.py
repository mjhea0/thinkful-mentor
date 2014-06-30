def write_message(message_text):

    def _private_message(private_message_text):  # private function
        return "{}: {}".format(message_text, private_message_text)

    return _private_message  # returns private function

new_message = write_message("My message")
print type(new_message)
print new_message("Hello, World")


# new message is a function because `write_message()` returns a function
