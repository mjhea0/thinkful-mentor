from flask import Flask, render_template, request, redirect, url_for
 
app = Flask(__name__)      
 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    cost = request.form['meal_cost']
    percent = request.form['tip_percentage']
    try:
        tip=int(cost)*(int(percent)*.01)
        if int(cost) > 0 and int(percent) > 0:
            return render_template("results.html",tip=tip)
        else:
            tip_error = "Please enter a valid number"
            return render_template("home.html",tip_error=tip_error) 
    except ValueError:
        tip_error = "Please enter a valid number"
        return render_template("home.html",tip_error=tip_error)
 
if __name__ == '__main__':
    app.run(debug=True)
