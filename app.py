from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/landscape')
def landscape():
    return render_template('project1.html', title="Landscape Design")

@app.route('/medassist')
def medassist():
    return render_template('project2.html', title="MedAssist Project")

@app.route('/adventure')
def adventure():
    return render_template('project3.html', title="Adventure Outfitters")

if __name__ == '__main__':
    app.run(debug=True)
