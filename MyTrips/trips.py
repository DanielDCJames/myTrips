from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/tokyo')
def tokyo():
    return render_template('tokyo_template.html')

@app.route('/england')
def england():
    return render_template('england_template.html')

@app.route('/jamaica')
def jamaica():
    return render_template('jamaica_template.html')

@app.route('/russia')
def russia():
    return render_template('russia_template.html')

@app.route('/canada')
def canada():
    return render_template('canada_template.html')




if __name__ =='__main__':
    app.run()
