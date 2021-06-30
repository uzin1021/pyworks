from flask import Flask , render_template

app = Flask(__name__)
@app.route('/') # 루트 경로
def index():
    return render_template("index.html")
@app.route('/register')
def register(): # 이름 비슷하게 설정
    return "<h1>회원가입 페이지입니다.</h1>"
@app.route('/board')
def board():
    return "<h2>게시판 목록입니다</h2>"


if __name__=="__main__":
    app.run()
