from flask import Flask, render_template, request, redirect, url_for
from flask import session

app = Flask(
    __name__,
    static_folder="static", #靜態檔案資料夾名稱
    static_url_path="/static" #靜態檔案對應網址路徑
    )

#session 必須要設置一組 secret_key 
app.secret_key = "ji324ARWR#3j"

#網頁上方訊息統整
pageTitle1 = "歡迎光臨，請輸入帳號密碼"   
pageTitle2 = "歡迎光臨，這是會員頁"
pageTitle3 = "失敗頁面"

@app.route("/")
def index():
        return render_template("index.html", pageTitle = pageTitle1)

@app.route("/signin", methods=["GET", "POST"])
def singin():

    #收到 POST 資料時，先將 session 清空
    if request.method == "POST":
        session.pop("loginUsername", None)

    #將 POST 資料存入變數
    username = request.form["username"]
    pwd = request.form["password"]

    #判斷帳號密碼是否都等於 test
    if (username == "test") & (pwd == "test"):
        #帳號密碼相符，session 寫入資料，並導向 member 頁
        session["loginUsername"] = username
        return redirect(url_for('member'))
    else:
        session.pop("loginUsername", None)
        return redirect(url_for('error'))


#會員路由判斷
@app.route("/error")
def error():
        return render_template("error.html", pageTitle = pageTitle3)

#會員路由判斷
@app.route("/member")
def member():
    #判斷 session 有沒有存資料，有資料等於
    if session.get("loginUsername") != None:
        return render_template("member.html", pageTitle = pageTitle2)
    else:
        return redirect(url_for('index'))

#登出
@app.route("/signout")
def signout():
    #將 session 記錄清空
    #print(session)
    session.pop("loginUsername", None)
    #print(session)
    return redirect(url_for('index'))



#設定 host & port
app.run(host="127.0.0.1" ,port=3000)