from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
import sqlite3

DATABASE = 'checklist.db'
SECRET_KEY = 'SHHHH!'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
   

@app.route('/', methods=['GET'])
def home():
    g.db = connect_db()
    cur = g.db.execute('select * from items')
    my_items = [dict(item=row[0], amount=row[1]) for row in cur.fetchall()]  
    g.db.close()
    return render_template('home.html', my_items=my_items)

@app.route('/add', methods=['POST'])
def add():
    item = request.form['item']
    amount = request.form['amount']
    if not item or not amount:
        flash("All fields are required. Please try again.")
        return redirect(url_for('home'))   
    else:
        g.db = connect_db()
        g.db.execute('insert into items (item, amount) values (?, ?)',
         [request.form['item'], request.form['amount']])                 
        g.db.commit()
        g.db.close()
        flash('New entry was successfully posted!')
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)






