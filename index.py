import requests
from bs4 import Mc

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("KEY.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

from flask import Flask, render_template, request, make_response, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>吳佳哲Python讀取Firestore</h1>"
    homepage += "<a href=/account>網頁表單輸入實例</a><br><br>"
    homepage += "<a href=/search>Mc</a><br><br>"
    return homepage

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")





@app.route("/webhook", methods=["POST"])
def webhook():
    
    req = request.get_json(force=True)
    
    action =  req.get("queryResult").get("action")
    #msg =  req.get("queryResult").get("queryText")
    #info = "動作：" + action + "； 查詢內容：" + msg
    return make_response(jsonify({"fulfillmentText": info}))
    #if(action == "choice")

if __name__ == "__main__":
    app.run()