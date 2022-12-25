import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request, make_response, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
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
    # build a request object
    req = request.get_json(force=True)
    # fetch queryResult from json
    action =  req.get("queryResult").get("action")
    # msg =  req.get("queryResult").get("queryText")
    # info = "動作：" + action + "； 查詢內容：" + msg

    if(action == "choice"):
    #    flavor = req.get("queryResult").get("parmeters").get("flavor")
    #    info = "您選擇的口味是：" + flavor


      flavor =  req.get("queryResult").get("parameters").get("flavor ")
         info = "您選擇的口味是：" + flavor +"，相關資料：\n\n"
#您要查詢減肥菜單的時段
        collection_ref = db.collection("樂事餅乾")
        docs = collection_ref.get()
        result = ""
        for doc in docs:
            dict = doc.to_dict()
            if flavor in dict["口味"]
                info += "品名：" + dict["品名"] + "\n\n"
                info += "口味：" + dict["口味"] + "\n\n"
                info += "介紹：" + dict["介紹"] + "\n\n"
       
        info += result  
    return make_response(jsonify({"fulfillmentText": info}))

if __name__ == "__main__":
    app.run()