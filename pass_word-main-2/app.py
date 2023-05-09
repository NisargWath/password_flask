from flask import Flask, render_template, request
import random
import string

app = Flask(__name__,template_folder="templetes/")
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    if request.method == 'POST':
        length = int(request.form.get('length', 8))
        digits = bool(request.form.get('digits'))
        symbols = bool(request.form.get('symbols'))
        chars = string.ascii_letters
        if digits:
            chars += string.digits
        if symbols:
            chars += string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
