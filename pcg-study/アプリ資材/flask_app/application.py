from flask import Flask, render_template, url_for, request, session, redirect, jsonify
from models import rankings

app = Flask(__name__)

#ホームページ
@app.route('/', methods=['GET'])
def index():
    return render_template('welcome.html', title='PCG-Gameのサイトへようこそ！', )

#ゲームのページ
@app.route("/game/tako/", methods=["GET"])
def playtako():
    return render_template("game/tako.html")

@app.route("/game/magicNumber/", methods=["GET"])
def playmagicNumber():
    return render_template("game/magicNumber.html")

#ランキングページ
@app.route("/ranking/", methods=["GET"])
def ranking():
    return render_template("ranking.html", title="ゲーム別ランキング一覧")
 
@app.route('/ajax/<game_name>', methods=['GET'])
def ajax(game_name):
    ranking = rankings.getAll(game_name)
    return jsonify(ranking)

#お問い合わせフォームページ
@app.route("/contact/" ,methods=["GET"])
def contact():
    return render_template("contact.html", title="お問い合わせ")

