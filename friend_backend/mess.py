# encoding:utf-8

from flask import Blueprint, session, request
import time
from friend.model.message import Message,db
from friend.config.turn import *
from friend.model.user import User

me = Blueprint("me",__name__,url_prefix="/message")

@me.before_request
def before_request():
    login_name = session.get("login_name")
    user_info = User.query.filter_by(login_name = login_name).first()
    if user_info:
        nickname = user_info.nickname
        session["nickname"] = nickname  #  nickname存入session，前端每个页面都调用

        return
    else:
        return render_words(400)

@me.route("/box")
def box():  #  私信列表，返回收发件人和已读未读。

    host = session.get("login_name")
    box_info = []
    box_name = []
    login_code = {}
    accept_list = Message.query.filter_by(accept=host).all()  #  我在收件位置时的列表
    send_list = Message.query.filter_by(send=host).all()  # 我在发件位置时的列表

    for (a,b) in zip(accept_list,send_list):
        login_list = a.send + b.accept   #  所有收发件人的列表
        box_name.append(login_list)

    for j in set(box_name):
        box_info.append(j)

    for i in accept_list:
        if i.status == 0:
            login_code[i.send] = "0"
        else:
            login_code[i.send] = "1"

    result = {'name':box_info,'code':login_code}
    return render_words(result,200)

"""
使用方法：
“name”为所有收发件人，列表形式。使用时用for遍历。
“code”为字典形式，形式为{"发件人": 1}。如果是发件人对应1，那么则有未读信息。
判断在“code”中是否有“name”中的值，如果没有，则为未读。如果有且为1，则说明有已读。
"""

@me.route("/content/<name>",methods = ["GET","POST"])
def content(name):
    if request.method == "POST":
        pass

    accept_info = {}
    send_info = {}
    time_list = []
    host = session.get("login_name")
    # name 是发件人或者收件人
    """收到的信息"""

    accept_list = Message.query.filter_by(accept = host,send = name).all()  # 我作为收件人
    for i in accept_list:
        a_timestamp = i.time
        accept_info[a_timestamp] = i.content
        id = i.Id
        if i.status == 0:
            Message.query.filter_by(Id = id).update({'status':1})
            db.session.commit()


    """发送的信息"""
    send_list = Message.query.filter_by(accept = name,send = host).all()  # 我作为发件人
    for j in send_list:
        s_timestamp = j.time
        send_info[s_timestamp] = j.content

    for (a,b) in zip(accept_info,send_info):
        time_list.append(a)
        time_list.append(b)
        time_list.sort()

    result = {'acceptor': accept_info, 'sender': send_info, "timelist":time_list}


    return render_words(result,200)

"""
调用方法：
所有收的信息和所有发的信息均以列表形式保存，accept_info为我收到的信息，send_info为我发送的信息
所有信息均为{时间戳：内容}格式。
timelist为所有时间戳列表，形式为列表，该列表是已经排序过的。
把收件人字典和发件人字典中的key（时间戳）对照，通过“字典名[key]”的形式取出内容。
如果内容发件人的，就放在左边，如果是收件人的就放在右边。
"""

@me.route("/send",methods = ["GET","POST"])
def send():

    if request.method == "POST":
        host = session.get("login_name")
        acceptor = request.json["login_name"]
        timestamp = time.time()
        content = request.json['content']

        u = Message()
        u.send = host
        u.accept = acceptor
        u.time = timestamp
        u.content = content
        db.session.add(u)
        # db.session.commit()
        try:
            db.session.commit()
        except:
            db.session.rollback()

        return render_words("发送成功",200)

"""
在查看其它用户档案页面，有发件接口。
传参为收件人，即浏览页面的login_name，发件人为注册用户
传参为login_name
"""