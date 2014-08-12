from blog import app


@app.template_filter()
def dateformat(date, format):
    if not date:
        return None
    return date.strftime(format)
