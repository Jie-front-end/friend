from flask import render_template,jsonify

def render_page(page,msg={},code=None):
    result = {
        "msg" : msg,
        "code":code
    }
    return render_template(page,**result)

def render_words(msg={},code = None):
    result = {
        "msg":msg,
        "code":code
    }
    return jsonify(result)