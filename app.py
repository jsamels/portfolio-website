from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Home")

@app.route('/landscape')
def landscape():
    return render_template('project1.html', title="Landscape Design")

@app.route('/medassist')
def medassist():
    return render_template('project2.html', title="MedAssist Project")

@app.route('/adventure')
def adventure():
    return render_template('project3.html', title="Adventure Outfitters")

@app.route('/graphic_design')
def graphic_design():
    return render_template('graphic_design.html', title="Graphic Design")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Me")

if __name__ == '__main__':
    app.run(debug=True)



