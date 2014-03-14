from flask import Flask, render_template, request
 
app = Flask(__name__)      
 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    cost = request.form['meal_cost']
    percent = request.form['tip_percentage']
    tip=int(cost)*float(percent)
    return render_template('results.html',tip=tip)
 
if __name__ == '__main__':
    app.run(debug=True)
