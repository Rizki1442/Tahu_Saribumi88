from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/lokasi')
def lokasi():
    return render_template('lokasi.html')

@app.route('/proses-pembuatan')
def proses_pembuatan():
    return render_template('proses-pembuatan.html')

if __name__ == '__main__':
    app.run(debug=True)