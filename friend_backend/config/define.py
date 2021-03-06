# -*- coding: utf-8 -*-

from hashlib import md5
import re
from suntime import TrueTime
from friend.files.charactor_returnnum import *
from collections import Counter

five_elements = {
        "1": "水",
        "2": "木",
        "3": "火",
        "4": "土",
        "5": "金",
    }

advantage = {
        "3": "十神性格：偏印。感情上，偏印有很高的标准， 因此会时常对自己和伴侣相对的苛责。事事追求完美的偏印，很少说出称赞的话，而往往在人际交往中更关注如何把事情做到最好。 在亲密关系中的偏印，往往体现出控制欲比较强，在争吵时寸步不让，愿意自己拿主意。",
        "9": "十神性格：伤官。感情上，伤官渴望别人的爱或良好关系、甘愿迁就他人、以人为本。伤官要别人觉得需要自己、甚至常会忽略自己 。伤官很在意别人的感情和需要，十分热心，愿意付出爱给别人，看到别人满足地接受自己的爱，自己也一样满足。伤官愿意为了自己的伴侣无私的奉献，因此常常扮演两人中给予者的角色，有时甚至因此而失去自我。",
        "7": "十神性格：官。感情上，官会把自己看成为颇大、颇重要的，所以有一点点的自恋、自我膨胀。所以官都会把自己最好的一面给友另一半看，甚至极端时，会在另一半面前撒谎，以求“保持”自己在另一半心目中的形象。很多时候，官真正的实力往往没有那么强，因为官的表达有时有一点点夸张。",
        "1": "十神性格：比肩。比肩是个情绪化比较重的人，追求浪漫和艺术情调，对自我和和自身的细腻情感观察入微。感情上，比肩会表现出较高的情感需求，渴望一位能了解独特自己的心灵伴侣是比肩感情生活中的基本需求。另一方面，比肩是感情主导的人，所以遇到比肩不喜欢的人，比肩会毫不掩饰的拒绝。",
        "4": "十神性格：正印。正印喜欢思考分析，要知很多，但缺乏行动，对物质生活要求不高，喜欢精神生活，不善表达内心感受。感情上，往往也需求更多的独立空间，并不希望和另一半天天黏在一起。同时，富于深刻思索的正印其实并不需要另一半对他们言听计从。和而不同，有自己独立的想法，从而可以相互交流的另一半才是他们所需要的。",
        "6": "十神性格：正财。在感情中比较被动，安全感对正财很重要，因为正财更习惯于旧的稳定的关系，而因此对新事物显得疑虑，对独立的抉择感到害怕。正财是恋爱关系中忠诚的追随者，需要一个可以相互信任互相扶持的伴侣，另一半的爱是正财应对这个纷繁世界的强大依靠。",
        "8": "十神性格：食神。食神是开心和愉悦气氛的制造机，喜欢新鲜感，不喜承受压力，渴望过比较享受的生活。感情上，食神追求快乐的爱情而非稳定长远的爱情，不喜欢被束缚、被控制，食神讨厌过于拘束的男女关系，对于分分合合也十分果断，并不会拖泥带水。",
        "5": "十神性格：偏财。偏财追求能力，讲求实力，不靠他人，有正义感。有明确而强烈的目标并且富于自信，不愿意受别人控制。感情上，偏财希望把爱人的一切也都扛在自己的肩上，有着英雄主义爱情观的偏财常常为伴侣预设立场，希望同伴按照你的欲望行事。",
        "2": "十神性格：劫财。劫财主见较少，不善于拒绝别人，显得很温和，不愿意与别人发生冲突，甚至也乐于接受别人的安排做一个很好的支持者。感情上，劫财追求和谐，相互融合的爱情，劫财不奢望轰轰烈烈可歌可泣，取而代之的是持久，安稳，细水长流。",
        "a": "十神性格：劫财。劫财主见较少，不善于拒绝别人，显得很温和，不愿意与别人发生冲突，甚至也乐于接受别人的安排做一个很好的支持者。感情上，劫财追求和谐，相互融合的爱情，劫财不奢望轰轰烈烈可歌可泣，取而代之的是持久，安稳，细水长流。",
        "b":"十神性格：偏印。感情上，偏印有很高的标准， 因此会时常对自己和伴侣相对的苛责。事事追求完美的偏印，很少说出称赞的话，而往往在人际交往中更关注如何把事情做到最好。 在亲密关系中的偏印，往往体现出控制欲比较强，在争吵时寸步不让，愿意自己拿主意。",
        "c": "十神性格：偏财。偏财追求能力，讲求实力，不靠他人，有正义感。有明确而强烈的目标并且富于自信，不愿意受别人控制。感情上，偏财希望把爱人的一切也都扛在自己的肩上，有着英雄主义爱情观的偏财常常为伴侣预设立场，希望同伴按照你的欲望行事。",
        "d":"十神性格：官。感情上，官会把自己看成为颇大、颇重要的，所以有一点点的自恋、自我膨胀。所以官都会把自己最好的一面给友另一半看，甚至极端时，会在另一半面前撒谎，以求“保持”自己在另一半心目中的形象。很多时候，官真正的实力往往没有那么强，因为官的表达有时有一点点夸张。",
        "e": "十神性格：伤官。感情上，伤官渴望别人的爱或良好关系、甘愿迁就他人、以人为本。伤官要别人觉得需要自己、甚至常会忽略自己 。伤官很在意别人的感情和需要，十分热心，愿意付出爱给别人，看到别人满足地接受自己的爱，自己也一样满足。伤官愿意为了自己的伴侣无私的奉献，因此常常扮演两人中给予者的角色，有时甚至因此而失去自我。",
    }

coop = {
        "3": "事业上，偏印是个很有条理的人，办事井然有序，喜欢各种规则和等级制度。在偏印心里，比较容易对人有划分，非黑即白，非好即坏，认为做事情只有一种正确的方法。偏印是一个理想主义者，追求道德、公正、真理，并希望自己完美得无可挑剔。因此，偏印往往会以很高的标准要求自己，同样也要求别人。",
        "9": "事业上，伤官能十分敏锐的判断出别人的需要，并能调整自己的感情去适应他人，甚至放弃自己的需要。亲切友好，待人热情，人们总是可以从伤官这里得到安慰和鼓舞。伤官希望通过帮助别人来得到他人的认可，并感到自己对别人的价值。但是伤官也不容有自己的立场，很容易成为墙头草。",
        "7": "事业上，官是个目标感很强的人，办事讲求效率。同时官渴望成就，以自己的成功为荣，为了成功即使牺牲自己的个人生活也在所不惜，官会以一个人取得的成就和相应的社会地位来衡量这个人，掌声、鲜花、金钱、地位，这些和人的价值捆绑在一起，拥有了这些，对官而言也就体现了自己的价值，就拥有了快乐。",
        "1": "事业上，比肩性格温和、喜欢和谐的气氛。尽量避免和他人发生冲突，甚至可以说尽量避免一切形式的冲突，避免内心被扰乱，避免外在的矛盾。比肩不喜欢表明鲜明的立场，而善于听取正反两方面的意见，所以你在做决定时往往犹豫不决。比肩是一个愿意倾听他人的人，很有耐心，能体谅他人的心情，欣赏和包容他人。",
        "4": "事业上，正印喜欢研究事物，喜欢知识， 喜欢用自己的大脑分析问题。对正印来说，正印需要自己私人的空间去考虑事情。正印往往会把关注点放在事情本身，而不是人身上，所以正印常常让周围人觉得难以接近。相对于和人交往而言，正印更喜欢对一件事或物的思考与探索，因为正印渴望能够懂得多，做一个有智慧的人。",
        "6": "事业上，正财是一个谨慎的人，也是一个被动的人，相比于进攻，正财会把更多的关注放在防守之上。正财很小心谨慎，危机意识很强，总担心事情会出错，经常预备好应变计划，以防问题真的发生。而在与人交往中，正财也并不是一个会轻信人的人。正财有着比较强的分析能力，有时会过分考虑事情的负面因素，但也可以事前清晰预见障碍。",
        "8": "事业上，食神是一个乐观、精力充沛的人，对世界充满了好奇，喜欢追求刺激。思想跳脱，能让自己不受负面情绪的困扰。贪玩，乐天知命，喜欢探索新的领域。领导团队喜爱变革创新，做人做事没有固定的模式。内心恐惧受制于人，自己的时间空间被他人占用。",
        "5": "事业上，偏财是一个直来直去，讨厌拐弯抹角的人。喜欢结交朋友，外向主动，重视正义与公平。喜欢占据领导地位，也会有攻击性。做事富有对抗性，会带有独裁、严厉的做事风格，富有威严，不拘小节。渴望自己当家做主，恐惧被他人支配。",
        "2": "事业上，劫财是一个和平主义者，喜欢和谐而舒适的生活。劫财善于了解每个人的观点，配合他人的安排，不愿起冲突。做事以人为本，顺其自然，不好争斗。讨厌被人施压，这会让劫财变得烦躁、易怒。善于调解，处事圆滑，内心恐惧被他人疏远。",
        "a": "事业上，劫财是一个和平主义者，喜欢和谐而舒适的生活。劫财善于了解每个人的观点，配合他人的安排，不愿起冲突。做事以人为本，顺其自然，不好争斗。讨厌被人施压，这会让劫财变得烦躁、易怒。善于调解，处事圆滑，内心恐惧被他人疏远。",
        "b": "事业上，偏印是个很有条理的人，办事井然有序，喜欢各种规则和等级制度。在偏印心里，比较容易对人有划分，非黑即白，非好即坏，认为做事情只有一种正确的方法。偏印是一个理想主义者，追求道德、公正、真理，并希望自己完美得无可挑剔。因此，偏印往往会以很高的标准要求自己，同样也要求别人。",
        "c": "事业上，偏财是一个直来直去，讨厌拐弯抹角的人。喜欢结交朋友，外向主动，重视正义与公平。喜欢占据领导地位，也会有攻击性。做事富有对抗性，会带有独裁、严厉的做事风格，富有威严，不拘小节。渴望自己当家做主，恐惧被他人支配。",
        "d":  "事业上，官是个目标感很强的人，办事讲求效率。同时官渴望成就，以自己的成功为荣，为了成功即使牺牲自己的个人生活也在所不惜，官会以一个人取得的成就和相应的社会地位来衡量这个人，掌声、鲜花、金钱、地位，这些和人的价值捆绑在一起，拥有了这些，对官而言也就体现了自己的价值，就拥有了快乐。",
        "e": "事业上，伤官能十分敏锐的判断出别人的需要，并能调整自己的感情去适应他人，甚至放弃自己的需要。亲切友好，待人热情，人们总是可以从伤官这里得到安慰和鼓舞。伤官希望通过帮助别人来得到他人的认可，并感到自己对别人的价值。但是伤官也不容有自己的立场，很容易成为墙头草。",
    }

disadvantage = {
        "0": "你的整体特质比较平均，并没有很突出的缺点，但是这也代表了你并没有很突出的优点可以利用。",
        "3": "办事条理性不强，不喜欢条条框框的约束。不会非黑即白的给人分类，认为能解决事情的方法就是可接受的方法。是一个现实主义者，对人对己都不会苛求完美，差不多就行，对道德、公证、真理没有太高的追求欲望。",
        "9": "以自己为中心，不会放低自己的需要去迁就别人。个性独立，有自己的态度，不太在乎他人的看法，对人不会很热情，容易让人有距离感，通常也不是人们会来寻求安慰、鼓舞的对象。 ",
        "7": "目标感很弱，对成功也没有很强的欲望，比起成功更关注自己的个人生活。认为金钱、地位这些外在的光鲜与世俗衡量尺并不能全然代表一个人的价值，一个人的价值和快乐更多的是来源于身心灵的追求。",
        "1": "性格比较急躁，直来直去，容易与人发生冲突。对人对事立场鲜明，行事独断，不愿听取他人意见，也比较一根筋，不会换位思考。内心坚定，不容易被外在的声音影响。",
        "4": "感性大于理性，不喜欢一板一眼的钻研死物，为人处世比较灵活，喜欢跟人打交道，也会让周围的人都觉得很好相处。面对事物往往是凭直觉和感性感官判断，而不是深思熟虑后再做决定。",
        "6": "神经大条，今日不想明日事，不喜欢做提前规划，缺乏谨慎心。做事主动性强，也比较冒进，容易忽略细节，缺乏危机意识。也容易轻信他人，对待事情有时容易过分乐观。",
        "8": "性格不是很活泼，相对比较闭塞，不喜欢尝试新鲜事务。玩心不大，没有固定的兴趣爱好。无论是感情上还是工作上，都缺乏跳跃性思维，也并没有嗯强烈的探索新领域或新方法的心，对于变革没有强烈的主动性。",
        "5": "性格相对内向被动，对社交并不热衷，为人处世比较圆滑委婉，不喜欢产生冲突，没有攻击性。做事富有合作性，能很好地扮演辅助者的角色，行事风格比较温吞、细致，注重细节。",
        "2": "个性比较强势，喜欢占主导地位。做事很主动积极，力争上游，常会在工作中因专注于追赶目标，而忽略了人的情绪。对道德、公正、真理也有较高的追求。",
    }

attention = {
        "0": "你并没有什么需要过多关注的地方，因为你的整体特质比较平均。一定要切记无论是在沟通还是在事情的处理上都切忌极端即可。",
        "3": "【1】你必须以理性、合乎逻辑，并且正经的态度和他们沟通，才能获得他们的认同。【2】接着你可以适时表现一些幽默感，缓和他们的严肃僵硬，藉以牵引他们放松心情，放心发挥他们可以有的幽默、并且凡事试着朝正面想。【3】当他们不知为何生气，或是显得很“龟毛”时，我们不必太在意，不必追究他们的态度由来，不必跟之衡突，因为他们的怒气大多不是冲着你来的。它可能只是把无名火，也可能是针对其它跟你完全没相关的事！【4】说话要真诚、直截了当，因为他们十分敏感，加上判断力很佳，对于别人玩弄技俩、背后动机，他了然在心。如果你拐弯抹角只会令他不屑与厌恶！",
        "9": "【1】对于他们的付出，一定要表现出感激之意。【2】二型人最讨厌别人拒绝他们的好意，所以如果你想拒绝他们，就必须很清楚地把你的理由、感觉告诉他们，让他们知道真的不需要他去帮你什么，因为这才是你最需要的，也是对你最好的“帮助”。【3】二型人总是将关注放在别人身上，所以你不妨鼓励他们多谈谈自己，并告诉他们你想知道他们的事，多了解他们一些。【4】当你想为他做某件事时，告诉他们这么做会让你觉得快乐，他们便会接受你的付出。【5】当他们只顾着为别人忙碌，或是显得情绪化、心神不宁时，不妨问问他们正在想什么？心情如何？以及此刻有什么需要？",
        "7": "【1】希望他们改变作风、或是思考其它方案最有效的方法便是：告诉他们这样做可能会有助于他们获得更好的结果。【2】如果你喜欢他们，不妨尽量配合他们，因为当你与他们站在同一阵线时，他们也乐于保护你，与你分享他们的成就。【3】如果你有被他们利用或操纵的感觉时，不妨让他们知道你的感受，因为他们有时真的会忽略别人的感受，告诉他们后，他们多半会收敛一些，特别是当他无心伤害你时。【4】过度地批评只会让他们为了讨好你、顺应你，而矫情地做改变。所以要真正改变他们，应该是去爱他们，设法让他们去探索自己真正的感觉。",
        "1": "【1】感觉对他们而言是最重要的，与他们沟通一定要重视他们的感觉。【2】另方面也要让他们知道你的感觉、想法。【3】密切地配合他们，令到他们感觉到你是关心他们，愿意支持他们。【4】如果他们沉浸在某种情绪中难以自拔时，问问他们当下的感受。让他们有机会抒发情绪，是帮助他们走出情绪的最好方法。【5】不要老是以理性来要求他们、评断他们，听听他们的直觉，因为那可能会开启你不同的视野。【6】称赞他们，特别是当他们能发挥自己的特质而有所贡献时，因为他们是极容易有负面情绪，容易否定自我的人。",
        "4": "【1】 他们在面对人群表达自己时往往有困难，所以不要在这方面给他们太大的压力。要表现出亲切的善意，以减轻他们的紧张、焦虑。【2】 要亲切，但不要表现出依赖或过于有压力的亲密，因为他们喜欢与人保持一定的距离，要尊重他们的界线。【3】 要求他们做决定时，请尽量留给他们独处的时间和空间。【4】 当你请求他们某件事时，请记住你表达态度应该是一种请求而非要求。【5】 作为第五型人的伴侣，要增加他们的信任，减轻其焦虑最好的方法是身体的接触（ 例如按摩） ，这对他们而言是胜于语言的沟通。",
        "6": "【1】他们是多疑的，所以很难相信你对他们的赞美。唯有不断的倾听，并愿意支持他们、和他们站在一起，才是取得他们信任最好的方法。【2】保持你的一致性，不要言行不一、变来变去，这样自然会让他对你产生信任。【3】不要讥笑或批评他们的多疑，这会使他们更缺乏自信。【4】说话必须真诚、清楚明白，因为他们很会猜测你的“言外之意”，而做不必要的联想。【5】身为六型人的伴侣，请务必让他们知道你每天的行动，他们不是要控制你、干涉你，只是他必须知道这些才能觉安心。",
        "8": "【1】以一种轻松愉快的方式和他们交谈，是建立彼此好感的第一步，因为他们不喜欢过于严肃、拘谨、无趣的人。【2】倾听他们伟大的梦想和计划，不必马上点出其中不切实际的地方，把它当成是一种分享想法、分享喜悦的方式。【3】如果你要点出他们计划中的一些问题点，请不要用一种高姿态的批评或指示，改用一种建议、提供参考的口吻，他们会比较容易接受。【4】当你提出不同的见解、方案时，他们当下可能会有点反弹，但记住，他们是善于思考的，给他们重新思考的时间，他们自然会判断是否接纳你的想法，或是找时间跟你进一步讨论。【5】如果你是他们的好朋友，看到他们逃避问题时，不妨提醒他们，找时间静下来面对问题，把问题想清楚。",
        "5": "【1】说话尽量说重点，他们才不会不耐烦，并愿意听你继续陈述。【2】你认为你们彼此起了争执、冲突，他却可能觉得这是很过瘾、很有效的沟通模式。所以你要记着，冲突对他们而言是进一步沟通的开始，而非结束。万一你觉得“争吵”太过厉害，感觉不舒服时，不妨直接告诉他们你的感受。【3】他们可以接受直接的批评，但不要取笑或讥讽他们，这会使他们产生敌意，做出攻击的行为。【4】玩弄权谋、操纵他们、说谎，都是他们讨厌的行为，记着跟他们沟通的最好方式是：直接、说重点。",
        "2": "【1】尽量倾听他们，并鼓励他们说出自己的想法。【2】要适时地赞美他们、认同他们，因为他们常常不知道自己的优点、自己的重要性。【3】当他们赞成、或是执行某件事时，事实上有可能只是为了迎合别人，所以你不妨问问他们的想法，听听他们会怎样说。【4】如果你想真正了解他们的想法，不应过于急切、压迫，否则他们会给你一个“你想听到的”答案，所以还是给他们一点空间和时间来回答吧。"

    }

trans = { "偏印":"3", "伤官":"9", "官":"7", "比肩":"1","正印":"4","正财":"6","食神":"8","偏财":"5","劫财":"2"}

class split(object):

    def __init__(self,birth):
        self.birth = birth
    def split(self):
        date = re.split(r"(\D+)",self.birth)
        birth_year = date[0]
        birth_month = date[2]
        birth_day = date[4]
        birth_hour = date[6]
        birth_minute = date[8]

        result = [birth_year,birth_month,birth_day,birth_hour,birth_minute]

        return result

class count(object):

    def __init__(self,dict):
        self.dict = dict

    def counter(self):
        star = re.split(r"(☆)",self.dict)
        counter = Counter(star)
        result = counter["☆"]

        return result


class PassWord(object):

    def __init__(self,pwd):
        self.pwd = pwd

    def PWD(self):

        md = md5()
        md.update(self.pwd.encode(encoding='utf-8'))
        return md.hexdigest()

class Birth(object):

    def __init__(self,y,m,d,h,s,city):
        self.year = y
        self.month = m
        self.day = d
        self.hour = h
        self.minute = s
        self.city = city


    def birth(self):
        true_time = TrueTime(self.year,self.month,self.day,self.hour,self.minute,self.city).truetime()
        res = str(true_time[0]) + "-" + str(true_time[1]) + "-" + str(true_time[2]) + "-" + str(true_time[3])  # 返回 %Y-%m-%d %H
        return res


class profiles(object):
    __advantage = {
        "3": "偏印","9": "伤官","7": "官","1": "比肩","4": "正印","6": "正财","8": "食神","5": "偏财","2": "劫财",
        "a": "劫财","b": "偏印","c": "偏财","d": "官","e": "伤官"}

    __disadvantage = {
        "3": "偏印", "9": "伤官", "7": "官", "1": "比肩", "4": "正印", "6": "正财", "8": "食神", "5": "偏财", "2": "劫财",
        "0": "无"}
    def __init__(self,birth):
        self.char = Charactor()
        self.birth = birth

    def Char(self):
        char = self.char.result(self.birth)

        result = {
            "fe_num":char[1],
            "adv_num":char[2],
            "dis_num":char[5],
            "five_elements" : five_elements[char[1]],
            "advantage" : self.__advantage[char[2]],
            "disadvantage" : self.__disadvantage[char[5]],
            "attention": attention[char[5]]
        }
        return result

if __name__ == '__main__':

    a = Birth(1988,8,6,9,30,"天").birth()
    print(a,type(a))
    b = profiles("1988-8-6-9").Char()
    print(b)
    c = PassWord("zxZ8808063697").PWD()
    print(c)
    d = split("1988-8-6-9:30:5").split()
    print(d)