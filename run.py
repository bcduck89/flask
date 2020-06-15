from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>텍스트 문자데이터 형식으로 HTML 문법을 작성하면 된다</h1>'

@app.route('/contents')
def contents():
    return render_template('contents.html')

if __name__ == '__main__':
    app.run()