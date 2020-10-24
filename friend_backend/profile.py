from flask import Blueprint,session, request
from friend.config.turn import *
from friend.model.user import User
from friend.Marriage.merry import *
from friend.config.define import *
from friend.files.ZhanBu import BaziPaipan
import time,re

pf = Blueprint("profile",__name__,url_prefix="/profile")

@pf.before_request
def before_request():
    login_name = session.get("login_name")
    user_info = User.query.filter_by(login_name = login_name).first()
    if user_info:
        nickname = user_info.nickname
        session["nickname"] = nickname  #  nickname存入session，前端每个页面都调用

        return
    else:
        return render_words(400)

@pf.route("/host")  #  用户登录之后的档案页面
def files():
    __bit_one = {
        "0": "环境变动：\n没有在工作环境或者住所环境的变动。\n",
        "1": "环境变动：\n有在工作环境或者住所环境的变动，比如工作的公司变动、部门调动、行业变动或者搬家等。\n"
    }

    __bit_three = {
        "0": "感情：☆☆☆☆\n意味着：只能给一个稳定的评价，上一年如何这一年就如何，有对象的不会散，不过没有对象的在这一年也容易在感情上有惊喜。\n",
        "1": "感情：☆☆☆\n意味着：为了感情你做了很大的努力，表面上风平浪静，但感情之事让你心累，付出总比收获少。\n",
        "2": "感情：☆☆\n意味着：感情上求而不得。你是想和他好好在一起的，可就是如不了你的愿。\n",
        "3": "感情：☆\n意味着：不利感情发展。概括来讲就是很糟心，因为这一年你感情不稳定，对感情的关注度很低，即便有对象也很容易分手。\n",
        "4": "感情：☆☆☆☆☆\n意味着：利于感情发展。很容易有桃花或者是自己喜欢的人。\n",
        "5": "感情：☆☆☆\n意味着：感情的转折。如果之前没有对象，这一年容易有桃花；如果之前有对象，这一年在感情上不顺利。\n",
        "6": "感情：☆☆☆☆☆\n意味着：利于感情发展。很容易有桃花或者是自己喜欢的人。\n",
        "7": "感情：☆☆☆☆\n意味着：感情发展有坎坷。很容易有新桃花，但是并不是两情相悦的人，或者这一年经历过感情的坎坷。\n",
        "8": "感情：☆☆☆☆\n意味着：利于感情发展。比较容易有桃花，而且还是让自己心动的人。\n"
    }

    __bit_four = {
        "0": "财运：☆☆☆☆\n意味着：财运平平，相比上一年差不多，所留下的钱还是稳步上涨的。\n",
        "1": "财运：☆☆☆\n意味着：控制不住想花钱，收入没怎么涨，花销倒是更大了。\n",
        "2": "财运：☆☆\n意味着：收入上受到了负面影响，挣得少或者有大的开销。\n",
        "3": "财运：☆\n意味着：不利财运。财运非常暗淡，入不敷出，很难存下钱，也会为财方面的事忧虑。\n",
        "4": "财运：☆☆☆☆☆\n意味着：利于努力得财。和上一年比起来，财运上好了一些，存下的钱相对变多。\n",
        "5": "财运：☆☆☆☆☆\n意味着：利于得外财。和上一年比起来，财运上好了一些，尤其是很容易添一些偏财。\n",
        "6": "财运：☆☆☆☆☆\n意味着：利于努力进财。和上一年比起来，进财更多或者花费更少，存款更多了一些。\n",
        "7": "财运：☆☆☆☆\n意味着：虽然相比之前有更多进财，但是花费也随之增多。\n",
        "8": "财运：☆☆☆\n意味着：在整体进项上出现问题，相比之前收入变少，或者花销更大。\n"
    }

    __bit_five = {
        "0": "工作学业：☆☆☆☆\n意味着：学业工作上是平平淡淡的一年，没什么大事，也没什么起伏，但会更加忙碌一些。\n",
        "1": "工作学业：☆☆☆\n意味着：做事情会遇到阻碍，虽然结果也算差强人意，但是自己也遇到了很多坎坷，付出了太多的努力。\n",
        "2": "工作学业：☆☆\n意味着：即便努力了也找不到方法，也达不到自己给自己定下的目标，甚至受累不讨好。\n",
        "3": "工作学业：☆\n意味着：不利工作学业。工作学业上不顺利，很难达到自己的要求。\n",
        "4": "工作学业：☆☆☆☆☆\n意味着：利于努力工作读书。工作学业上关注度比较高，也比较忙碌，自己会感到十分充实，能达到自己的目标。\n",
        "5": "工作学业：☆☆☆☆☆\n意味着：利于努力工作读书。工作学业上关注度比较高，也比较忙碌，能达到自己的目标。\n",
        "6": "工作学业：☆☆☆☆☆\n意味着：利于努力工作读书。工作学业上比较忙碌，但是自己也会从中获得很大成就感，能达到自己的目标。\n",
        "7": "工作学业：☆☆☆\n意味着：虽然在工作或者学业上比较忙，但是心思很杂乱，坎坷比较多，很难有积累。\n",
        "8": "工作学业：☆☆☆☆\n意味着：在工作或者学业上并没有让自己满意，容易受累不讨好，辜负自己的付出。\n"
    }

    __bit_six = {
        "0": "考试/领导关系：☆☆☆☆\n意味着：在考试/领导关系上谈不上顺也谈不上不顺，都是一般般的状态。\n",
        "1": "考试/领导关系：☆☆☆\n意味着：累心于考试/领导关系一类事情上，虽然最后也能差强人意，但是总有心有余悸的感觉。\n",
        "2": "考试/领导关系：☆☆\n意味着：因为考试/领导关系的事让自己自信心受挫，并没有达到之前计划好的目标。\n",
        "3": "考试/领导关系：☆\n意味着：不利考试与事业。与领导很容易不合，很难达到领导的要求。考试上也是不能尽如人意。\n",
        "4": "考试/领导关系：☆☆☆☆☆\n意味着：利于考试与事业。在考试/领导关系上可以说是相当顺利，自信心十足，自己也十分的满意，能达成之前计划定下的目标。\n",
        "5": "考试/领导关系：☆☆☆☆☆\n意味着：利于考试与事业。在考试/领导关系上可以说是相当顺利，自信心十足，自己也十分的满意，能达成之前计划定下的目标。\n",
        "6": "考试/领导关系：☆☆☆☆☆\n意味着：利于考试与事业。在考试/领导关系上关注度比较高，比较努力，而这方面也可以说是相当顺利，能达成之前计划定下的目标。\n",
        "7": "考试/领导关系：☆☆☆\n意味着：不利于考试与事业。虽然能完成既定的目标，但是中间并不顺利，坎坷比较多，需要费尽心思努力争取。\n",
        "8": "考试/领导关系：☆☆☆\n意味着：不利于考试与事业。在考试/领导关系上虽然用心了，但是并没有达到既定目标，排名通过类考试不易通过。\n"
    }

    login_name = session.get("login_name")
    user_info = User.query.filter_by(login_name = login_name).first()
    birthday = user_info.birthday
    birth = re.split(r"(\D+)",birthday)
    year = birth[0]
    month = birth[2]
    day = birth[4]
    hour = birth[6]
    ac_sex = user_info.sex
    sex = "0"
    if ac_sex == "男":
        sex = "1"
    elif ac_sex == "女":
        sex = "0"
    ####个人的优缺点等 ####
    char = profiles(birthday).Char()
    adv = advantage[char['adv_num']]
    f_e = five_elements[char["fe_num"]]
    dis_adv = disadvantage[char["dis_num"]]
    att = char["attention"]
    ####计算八字####
    eight= BaziPaipan(int(year),int(month),int(day),int(hour)).pre_Bazi_words()
    eight_year = eight[0][0] + eight[0][1]
    eight_month = eight[0][2] + eight[0][3]
    eight_day = eight[0][4] + eight[0][5]
    eight_hour = eight[0][6] + eight[0][7]

    result = {"nick": user_info.nickname, "user_adv": adv, "user_dis": dis_adv, "attention": att, "five_elements": f_e,
              "sex": user_info.sex, "birth_year": eight_year, "birth_month": eight_month, "birth_day": eight_day, "birth_hour": eight_hour,
              "sign":user_info.sign,"career":user_info.career}
    ####计算连续几年的流年####
    predict = int(time.strftime("%Y",time.localtime(time.time())))
    star_num = []
    res_list = []
    for i in range(predict-3,predict+2):
        date = str(birthday) + " " + sex + " " + str(i)
        water = Year().result(date)
        year_star = {"year":str(i),"emotion":count(__bit_three[water[2]]).counter(),"money":count(__bit_four[water[3]]).counter(),"word":count(__bit_five[water[4]]).counter(),"leader":count(__bit_six[water[5]]).counter()}
        water_res = {"year":str(i),"emotion":__bit_three[water[2]],"money":__bit_four[water[3]],"word":__bit_five[water[4]],"leader":__bit_six[water[5]],"envir":__bit_one[water[0]]}
        res_list.append(water_res)
        star_num.append(year_star)

    result["lucky"] = res_list
    result["star"] = star_num
    return render_words(result,200)
    ###################

@pf.route("/search",methods = ["GET","POST"])
def search():
    #####合婚搜索框#######
    if request.method == "POST":
        marriage_name = request.json["search"]
        search_list = User.query.filter_by(nickname = marriage_name).all()
        result = {}
        for a in search_list:
            birthday = a.birthday  #  所有生日的列表
            birth = re.split(r"(\D+)", birthday)
            year = str(birth[0])
            month = str(birth[2])
            day = str(birth[4])
            date = year + "年" + month + "月" + day + "日"  # 1995年6月22日8点
            login_name = a.login_name   #  所有login_name的列表
            city = a.city
            sex = a.sex
            result["birth"] = date
            result["login_name"] = login_name
            result["city"] = city
            result["sex"] = sex



    #  将所选中的nickname对应的loginname传参给marry函数

        return render_words(result,code=200)

"""
result为登陆之后，用户档案页面，返回用户信息，用户优点，缺点，前后几个流年。
search为合婚的搜索框。用户在输入nickname之后，会弹出所有和这个nickname对应的login_name，并存在search_name列表中。
用户在选择search_name列表中的login_name的时候，记住login_name并给接口/profile/<name>传参login_name
"""

@pf.route("/recommend")
def recommend():

    recom_advan = {
        "偏财":["伤官","劫财"],
        "正财":["偏财","伤官"],
        "官":["食神","劫财"],
        "偏印":["正印","食神"],
        "正印":["偏印","官"],
        "比肩":["伤官","劫财"],
        "劫财":["官","偏财"],
        "食神":["偏印","正财"],
        "伤官":["比肩","偏财"]
    }

    recom_disad = {
        "偏财": "偏财",
        "正财": "正财",
        "偏官": "偏官",
        "正官": "正官",
        "偏印": "偏印",
        "正印": "正印",
        "比肩": "比肩",
        "劫财": "劫财",
        "食神": "食神",
        "伤官": "伤官"
    }

    recom_fe = {
        "金": "金",
        "木": "木",
        "水": "水",
        "火": "火",
        "土": "土",
    }

    login_name = session.get("login_name")
    """这一部分是取登陆用户的优缺点，用来匹配推荐的人"""
    user_info = User.query.filter_by(login_name = login_name).first()
    user_advan = user_info.advantage  # 给的是十神的优点
    user_dis = user_info.disadvantage
    user_fe = user_info.five_element


    """这一部分是由登陆用户的优点和五行，确定推荐用户的优点和五行"""
    #  user_advan 推荐的人应该有的优点
    #  user_advan 推荐的人应该有的缺点
    #  user_fe  推荐人的五行
    """这一部分是找到推荐的用户的信息，这部分应该是列表套列表形式，应该用{% for i in *** %}的形式"""
    rec_first = User.query.filter_by(advantage = recom_advan[user_advan][0]).all() # 按照性格推荐的人的列表
    r_first = []
    for i in rec_first:
        r_first.append({"nickname":i.nickname,"city":i.city,"sex":i.sex,"login_name":i.login_name})

    rec_fst = User.query.filter_by(advantage = recom_advan[user_advan][1]).all() # 按照性格推荐的人的列表
    for j in rec_fst:
        r_first.append({"nickname":j.nickname,"city":j.city,"sex":j.sex,"login_name":j.login_name})

    rec_second = User.query.filter_by(five_element = recom_fe[user_fe]).all() # 按照五行推荐的人的列表
    r_second = []
    for k in rec_second:
        r_second.append({"nickname":k.nickname,"city":k.city,"sex":k.sex,"login_name":k.login_name})
    rec_third = User.query.filter_by(advantage = recom_disad[user_dis]).all() # 按照缺点推荐的人的列表
    r_third = []
    for l in rec_third:
        r_third.append({"nickname":l.nickname,"city":l.city,"sex":l.sex,"login_name":l.login_name})
    recommend_first = User.query.filter_by(five_element = user_fe,advantage = recom_advan[user_advan][0]).all()  # 优先推荐
    recommend_first1 = User.query.filter_by(five_element = user_fe,advantage = recom_advan[user_advan][1]).all()  # 优先推荐
    recom = []
    for (m,n) in zip(recommend_first,recommend_first1):
        recom.append({"nickname":m.nickname,"city":m.city,"sex":m.sex,"login_name":m.login_name})
        recom.append({"nickname": n.nickname, "city": n.city, "sex": n.sex, "login_name": n.login_name})


    result = {"first":recom,
              "second":r_first,
              "third":r_second,
              "forth": r_third
              }
    return render_words(result,200)

"""
所有适合的人的匹配列表。
"""

@pf.route("/detail/<name>")
def other(name):


    water = time.strftime("%Y",(time.localtime(time.time())))
    predict = str(int(water)+1)

    profile = User.query.filter_by(login_name = name).first()
    nickname = profile.nickname
    sex = profile.sex
    act_sex = 0
    if sex == "男":
        act_sex = 1
    elif sex == "女":
        act_sex = 0
    city = profile.city
    other_adv = advantage[trans[profile.advantage]]
    other_coop = coop[trans[profile.advantage]]
    other_dis = disadvantage[trans[profile.disadvantage]]
    birth = profile.birthday
    birthday = birth+" "+str(act_sex)+" "+ predict
    # emotion_lucky1 = Year().result(birthday)
    result = {"nickname" : nickname,"sex":sex,"advantage":other_adv,"disadvantage":other_dis,"city":city,"other_coop":other_coop,
              "sign": profile.sign, "career": profile.career}
    return render_words(result,200)

@pf.route("/co/<name>")
def  marry(name):
    host = session.get("login_name")
    host_info = User.query.filter_by(login_name = host).first()
    host_birthday = host_info.birthday
    host_sex = host_info.sex
    host_actsex = "0"
    if host_sex == "男":
        host_actsex = "1"
    elif host_sex == "女":
        host_actsex = "0"

    other = User.query.filter_by(login_name = name).first()
    other_birthday = other.birthday
    other_sex = other.sex
    other_actsex = "0"
    if other_sex == "男":
        other_actsex = "1"
    elif other_sex == "女":
        other_actsex = "0"

    if host_sex == "男" and other_sex == "女":
        h = Merry()
        res = h.final(host_birthday,host_actsex,other_birthday,other_actsex)

    elif host_sex == "女" and other_sex == "男":
        h = Merry()
        res = h.final(other_birthday,other_actsex,host_birthday,host_actsex)


    else:
        h = Merry()
        res = h.final(host_birthday,host_actsex,other_birthday,other_actsex)


    result = {"result":res}

    return render_words(result,200)

"""
输入为纯文字：harmony为合不合的断语，emotion为感情流年，可以后期适当删减，
charactor为性格的注意事项，money为财运的流年，后期可以适当删减。
"""


