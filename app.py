from flask import Flask, render_template, request
import pyfiglet

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form.get('text')
    font = request.form.get('font', 'slant')
    ascii_art = pyfiglet.figlet_format(text, font=font)
    return render_template('index.html', ascii_art=ascii_art, text=text, font=font)

if __name__ == '__main__':
    app.run(debug=True)
