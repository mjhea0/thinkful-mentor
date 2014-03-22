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
    open_items = g.db.execute('select * from items where status = 1')
    closed_items = g.db.execute('select * from items where status = 0')
    my_items = [dict(id=row[0], description=row[1], amount=row[2]) for row in open_items.fetchall()] 
    my_closed_items = [dict(id=row[0], description=row[1], amount=row[2]) for row in closed_items.fetchall()]  
    g.db.close()
    return render_template('home.html', my_items=my_items,my_closed_items=my_closed_items)

@app.route('/add', methods=['POST'])
def add():
    description = request.form['description']
    amount = request.form['amount']
    if not description or not amount:
        flash("All fields are required. Please try again.")
        return redirect(url_for('home'))   
    else:
        g.db = connect_db()
        g.db.execute('insert into items (description, amount, status) values (?, ?, ?)',
         [request.form['description'], request.form['amount'],1])                 
        g.db.commit()
        g.db.close()
        flash('New entry was successfully posted!')
        return redirect(url_for('home'))

@app.route('/complete/<int:id>')
def complete(id):
    g.db = connect_db()
    g.db.execute('update items set status = 0 where id ='+ str(id))
    g.db.commit()
    g.db.close()
    flash('Completed!')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)






