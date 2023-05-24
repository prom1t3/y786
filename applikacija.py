from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kritize', methods=['POST'])
def kritize():
    meal = request.form['meal']
    critique = request.form['critique']
    # Šeit jūs varat ieviest kodu, kas saglabā ēdienu un kritiku datubāzē vai failā
    return render_template('kritize.html', meal=meal, critique=critique)

if __name__ == '__main__':
    app.run()
