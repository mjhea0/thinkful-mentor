from flask import Flask, render_template, request
 
app = Flask(__name__)      
 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    cost = request.form['meal_cost']
    percent = request.form['tip_percentage']
    try:
        tip=int(cost)*float(percent)
    except ValueError:
        tip_error = "Enter a number"
        return render_template("home.html",tip_error=tip_error)
    return render_template('results.html',tip=tip)
 
if __name__ == '__main__':
    app.run(debug=True)
