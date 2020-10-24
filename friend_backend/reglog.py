from flask import Blueprint,request,session
from friend.config.turn import *
from friend.config.define import PassWord,Birth,profiles
from friend.model.user import User,db
from friend.config.define import split


rl = Blueprint("reglog",__name__,url_prefix="/user")

@rl.route("/register",methods = ["GET","POST"])
def reg():

    if request.method == "POST":

        req = request.json
        login_name = req["login_name"] if "login_name" in req else ""
        if len(login_name) < 4:
            return render_words(msg="用户名需大于4位",code=404)
        user_info = User.query.filter_by(login_name=login_name).first()
        if user_info:
            return render_words(msg="用户名已被注册",code=500)
        pwd = req["pwd"] if "pwd" in req else ""
        if len(pwd) < 6:
            return render_words(msg="密码需大于6位",code=404)
        md_pwd = PassWord(pwd).PWD()
        nickname = req["nickname"] if "nickname" in req else ""
        sex = req["sex"] if "sex" in req else ""
        date = req["date"]
        min = req['time']
        birth = str(date).split("-")
        year = birth[0]
        month = birth[1]
        day = birth[2]
        time = str(min).split(":")
        hour = time[0]
        minute = time[1]
        city = req["city"] if "city" in req else ""
        birthday = Birth(year,month,day,hour,minute,city).birth()    #  这是一个真太阳时，返回 %Y-%m-%d %H

        os = request.user_agent.platform
        ip = request.remote_addr
        ####################"""生成优缺点和五行"""##############
        char = profiles(birthday).Char()
        advantage = char["advantage"]
        disadvantage = char["disadvantage"]
        five_elements = char["five_elements"]
        ########################################################
        user = User()
        user.login_name = login_name
        user.pwd = md_pwd
        user.status = "1"
        user.nickname = nickname
        user.sex = sex
        user.city = city
        user.birthday = birthday
        user.os = os
        user.ip = ip
        user.advantage = advantage
        user.disadvantage = disadvantage
        user.five_element = five_elements
        db.session.add(user)
        try:
            db.session.commit()
            print("成功")
            return render_words(msg="注册成功", code=200)
        except:
            db.session.rollback()
            print("失败")
            return render_words("注册失败",400)



"""
调用方法：
注册接口，注册内容：注册名（唯一），密码（MD5），昵称，性别，年月日时分，出生地
返回注册成功文字，并跳转到登陆页面
"""

@rl.route('/login',methods = ["GET","POST"])
def login():
    if request.method == "GET":
        login_name = session.get("login_name")
        pwd = session.get("login_pwd")
        login_pwd = PassWord(pwd).PWD()
        print(len(login_name),len(login_pwd))
        user_info = User.query.filter_by(login_name=login_name).first()
        print("自动的：",login_pwd)
        if user_info and login_pwd == user_info.pwd:
            login = {"username":login_name,"password":user_info}
            return render_words(msg=login, code=200)
        else:
            return render_words(404)

    elif request.method == "POST":
        req = request.json
        login_name = req["login_name"] if "login_name" in req else ""
        login_pwd = req["login_pwd"] if "login_pwd" in req else ""
        md_pwd = PassWord(login_pwd).PWD()
        if len(login_name) < 4 or login_name is None:
            return render_words(msg="用户名需大于4位",code=404)
        if len(login_pwd) < 6 or login_pwd is None:
            return render_words(msg="密码需大于6位",code=404)
        user_info = User.query.filter_by(login_name = login_name).first()

        if not user_info:
            return render_words(msg="请输入正确的用户名和密码",code=500)
        if md_pwd != user_info.pwd:
            return render_words(msg="请输入正确的用户名和密码",code=500)
        if user_info.status != "1":
            return render_words(msg="账户被禁用，请联系管理员",code=500)

        session["login_name"] = login_name,
        session["login_pwd"] = md_pwd
        result = {
            "login_name":login_name,
            "statuscode":200
        }
        return render_words(msg=result,code=200)  #  把用户名和密码加入session

"""
调用方法：
如果是GET的话，后端先判断有没有session，如果有，传给前端，直接登陆，如果没有就没有了。
如果是POST方法，输入用户名和密码进行登陆。
"""


@rl.route("/info", methods=["GET", "POST"])
def info():
    if request.method == "POST":
        res = request.json
        sign = res["sign"]
        career = res["career"]
        login_name = session.get("login_name")
        z = User.query.filter_by(login_name = login_name).update({"sign":sign,"career":career})
        try:
            db.session.commit()
            return render_words("提交成功", 200)
        except:
            db.session.rollback()
            return render_words("提交失败", 400)



@rl.route("/forget/first",methods=["GET", "POST"])
def forget():
    if request.method == "POST":
        res = request.json
        login_name = res["login_name"]
        city = res["city"]
        date = res["date"]
        time = res["time"]
        birth = str(date)+"-"+str(time)
        bir = split(birth).split()
        year = bir[0]
        month = bir[1]
        day = bir[2]
        hour = bir[3]
        minute = bir[4]
        birthday = Birth(year,month,day,hour,minute,city).birth()

        user = User.query.filter_by(login_name = login_name,birthday = birthday,city = city).first()
        if user:
            return render_words(code=200)
        else:
            return render_words("该用户不存在",400)
# 获取注册名、年月日时分、出生地，判断在不在，如果不在跳转登陆页面，在的话跳转/forget/<name>页面

@rl.route("/forget/second",methods=["GET", "POST"])
def revise():
    if request.method == "POST":
        name = session["login_name"]
        res = request.json
        pwd = res["pwd"]
        md_pwd = PassWord(pwd).PWD()

        user = User.query.filter_by(login_name = name).update({"pwd":md_pwd})
        try:
            db.session.commit()
            return render_words("修改成功",200)
        except:
            db.session.rollback()
            return render_words("修改失败", code=400)



# 传参为注册名。成功之后跳转登陆页面。