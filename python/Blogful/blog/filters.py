from blog import app


@app.template_filter()
def dateformat(date, format):
    #the date argument is piped in from the template
    #format string we provide as an argument
    if not date:
        return None
    return date.strftime(format)
