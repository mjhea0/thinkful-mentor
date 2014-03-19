from flask import Flask, render_template, request
 
app = Flask(__name__)      
 
@app.route('/', methods=['GET', 'POST'])
def home():
    my_items = {"apples":13.45,"more apples":21.99}
    new_item = {}
    if request.method == 'POST':
        item = request.form["item"]
        amount = request.form["amount"]
        my_items[item] = amount
        return render_template('home.html', my_items=my_items)
    else:
        return render_template('home.html', my_items=my_items)


if __name__ == '__main__':
    app.run(debug=True)
