from flask import Flask, render_template

# instantiate a flask app
app = Flask(__name__)

# routes
@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/education')
def education():
    return render_template('education.html')

if __name__=='__main__':
    app.run(debug=True)
