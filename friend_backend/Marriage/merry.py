# -*- coding: utf-8 -*-

import time
from friend.files.year_returnnum import Year
from friend.files.charactor_returnnum import Charactor

class Merry(object):

    __five_elements = {
        "1": "水",
        "2": "木",
        "3": "火",
        "4": "土",
        "5": "金",
    }

    __charactor = {
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
        "b": "十神性格：偏印。感情上，偏印有很高的标准， 因此会时常对自己和伴侣相对的苛责。事事追求完美的偏印，很少说出称赞的话，而往往在人际交往中更关注如何把事情做到最好。 在亲密关系中的偏印，往往体现出控制欲比较强，在争吵时寸步不让，愿意自己拿主意。",
        "c": "十神性格：偏财。偏财追求能力，讲求实力，不靠他人，有正义感。有明确而强烈的目标并且富于自信，不愿意受别人控制。感情上，偏财希望把爱人的一切也都扛在自己的肩上，有着英雄主义爱情观的偏财常常为伴侣预设立场，希望同伴按照你的欲望行事。",
        "d": "十神性格：官。感情上，官会把自己看成为颇大、颇重要的，所以有一点点的自恋、自我膨胀。所以官都会把自己最好的一面给友另一半看，甚至极端时，会在另一半面前撒谎，以求“保持”自己在另一半心目中的形象。很多时候，官真正的实力往往没有那么强，因为官的表达有时有一点点夸张。",
        "e": "十神性格：伤官。感情上，伤官渴望别人的爱或良好关系、甘愿迁就他人、以人为本。伤官要别人觉得需要自己、甚至常会忽略自己 。伤官很在意别人的感情和需要，十分热心，愿意付出爱给别人，看到别人满足地接受自己的爱，自己也一样满足。伤官愿意为了自己的伴侣无私的奉献，因此常常扮演两人中给予者的角色，有时甚至因此而失去自我。",
    }

    __coop = {
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
        "d": "事业上，官是个目标感很强的人，办事讲求效率。同时官渴望成就，以自己的成功为荣，为了成功即使牺牲自己的个人生活也在所不惜，官会以一个人取得的成就和相应的社会地位来衡量这个人，掌声、鲜花、金钱、地位，这些和人的价值捆绑在一起，拥有了这些，对官而言也就体现了自己的价值，就拥有了快乐。",
        "e": "事业上，伤官能十分敏锐的判断出别人的需要，并能调整自己的感情去适应他人，甚至放弃自己的需要。亲切友好，待人热情，人们总是可以从伤官这里得到安慰和鼓舞。伤官希望通过帮助别人来得到他人的认可，并感到自己对别人的价值。但是伤官也不容有自己的立场，很容易成为墙头草。",
    }

    __non_charactor = {
        "0": "并没有什么需要过多关注的地方，因为你的整体特质比较平均。一定要切记无论是在沟通还是在事情的处理上都切忌极端即可。",
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

    __attention = {
        "0": "整体特质比较平均，并没有很突出的缺点，但是这也代表了你并没有很突出的优点可以利用。",
        "3": "【1】你必须以理性、合乎逻辑，并且正经的态度和他们沟通，才能获得他们的认同。【2】接着你可以适时表现一些幽默感，缓和他们的严肃僵硬，藉以牵引他们放松心情，放心发挥他们可以有的幽默、并且凡事试着朝正面想。【3】当他们不知为何生气，或是显得很“龟毛”时，我们不必太在意，不必追究他们的态度由来，不必跟之衡突，因为他们的怒气大多不是冲着你来的。它可能只是把无名火，也可能是针对其它跟你完全没相关的事！【4】说话要真诚、直截了当，因为他们十分敏感，加上判断力很佳，对于别人玩弄技俩、背后动机，他了然在心。如果你拐弯抹角只会令他不屑与厌恶！",
        "9": "【1】对于他们的付出，一定要表现出感激之意。【2】二型人最讨厌别人拒绝他们的好意，所以如果你想拒绝他们，就必须很清楚地把你的理由、感觉告诉他们，让他们知道真的不需要他去帮你什么，因为这才是你最需要的，也是对你最好的“帮助”。【3】二型人总是将关注放在别人身上，所以你不妨鼓励他们多谈谈自己，并告诉他们你想知道他们的事，多了解他们一些。【4】当你想为他做某件事时，告诉他们这么做会让你觉得快乐，他们便会接受你的付出。【5】当他们只顾着为别人忙碌，或是显得情绪化、心神不宁时，不妨问问他们正在想什么？心情如何？以及此刻有什么需要？",
        "7": "【1】希望他们改变作风、或是思考其它方案最有效的方法便是：告诉他们这样做可能会有助于他们获得更好的结果。【2】如果你喜欢他们，不妨尽量配合他们，因为当你与他们站在同一阵线时，他们也乐于保护你，与你分享他们的成就。【3】如果你有被他们利用或操纵的感觉时，不妨让他们知道你的感受，因为他们有时真的会忽略别人的感受，告诉他们后，他们多半会收敛一些，特别是当他无心伤害你时。【4】过度地批评只会让他们为了讨好你、顺应你，而矫情地做改变。所以要真正改变他们，应该是去爱他们，设法让他们去探索自己真正的感觉。",
        "1": "【1】感觉对他们而言是最重要的，与他们沟通一定要重视他们的感觉。【2】另方面也要让他们知道你的感觉、想法。【3】密切地配合他们，令到他们感觉到你是关心他们，愿意支持他们。【4】如果他们沉浸在某种情绪中难以自拔时，问问他们当下的感受。让他们有机会抒发情绪，是帮助他们走出情绪的最好方法。【5】不要老是以理性来要求他们、评断他们，听听他们的直觉，因为那可能会开启你不同的视野。【6】称赞他们，特别是当他们能发挥自己的特质而有所贡献时，因为他们是极容易有负面情绪，容易否定自我的人。",
        "4": "【1】 他们在面对人群表达自己时往往有困难，所以不要在这方面给他们太大的压力。要表现出亲切的善意，以减轻他们的紧张、焦虑。【2】 要亲切，但不要表现出依赖或过于有压力的亲密，因为他们喜欢与人保持一定的距离，要尊重他们的界线。【3】 要求他们做决定时，请尽量留给他们独处的时间和空间。【4】 当你请求他们某件事时，请记住你表达态度应该是一种请求而非要求。【5】 作为第五型人的伴侣，要增加他们的信任，减轻其焦虑最好的方法是身体的接触（ 例如按摩） ，这对他们而言是胜于语言的沟通。",
        "6": "【1】他们是多疑的，所以很难相信你对他们的赞美。唯有不断的倾听，并愿意支持他们、和他们站在一起，才是取得他们信任最好的方法。【2】保持你的一致性，不要言行不一、变来变去，这样自然会让他对你产生信任。【3】不要讥笑或批评他们的多疑，这会使他们更缺乏自信。【4】说话必须真诚、清楚明白，因为他们很会猜测你的“言外之意”，而做不必要的联想。【5】身为六型人的伴侣，请务必让他们知道你每天的行动，他们不是要控制你、干涉你，只是他必须知道这些才能觉安心。",
        "8": "【1】以一种轻松愉快的方式和他们交谈，是建立彼此好感的第一步，因为他们不喜欢过于严肃、拘谨、无趣的人。【2】倾听他们伟大的梦想和计划，不必马上点出其中不切实际的地方，把它当成是一种分享想法、分享喜悦的方式。【3】如果你要点出他们计划中的一些问题点，请不要用一种高姿态的批评或指示，改用一种建议、提供参考的口吻，他们会比较容易接受。【4】当你提出不同的见解、方案时，他们当下可能会有点反弹，但记住，他们是善于思考的，给他们重新思考的时间，他们自然会判断是否接纳你的想法，或是找时间跟你进一步讨论。【5】如果你是他们的好朋友，看到他们逃避问题时，不妨提醒他们，找时间静下来面对问题，把问题想清楚。",
        "5": "【1】说话尽量说重点，他们才不会不耐烦，并愿意听你继续陈述。【2】你认为你们彼此起了争执、冲突，他却可能觉得这是很过瘾、很有效的沟通模式。所以你要记着，冲突对他们而言是进一步沟通的开始，而非结束。万一你觉得“争吵”太过厉害，感觉不舒服时，不妨直接告诉他们你的感受。【3】他们可以接受直接的批评，但不要取笑或讥讽他们，这会使他们产生敌意，做出攻击的行为。【4】玩弄权谋、操纵他们、说谎，都是他们讨厌的行为，记着跟他们沟通的最好方式是：直接、说重点。",
        "2": "【1】尽量倾听他们，并鼓励他们说出自己的想法。【2】要适时地赞美他们、认同他们，因为他们常常不知道自己的优点、自己的重要性。【3】当他们赞成、或是执行某件事时，事实上有可能只是为了迎合别人，所以你不妨问问他们的想法，听听他们会怎样说。【4】如果你想真正了解他们的想法，不应过于急切、压迫，否则他们会给你一个“你想听到的”答案，所以还是给他们一点空间和时间来回答吧。",
        "a": "【1】尽量倾听他们，并鼓励他们说出自己的想法。【2】要适时地赞美他们、认同他们，因为他们常常不知道自己的优点、自己的重要性。【3】当他们赞成、或是执行某件事时，事实上有可能只是为了迎合别人，所以你不妨问问他们的想法，听听他们会怎样说。【4】如果你想真正了解他们的想法，不应过于急切、压迫，否则他们会给你一个“你想听到的”答案，所以还是给他们一点空间和时间来回答吧。",
        "b": "【1】 他们在面对人群表达自己时往往有困难，所以不要在这方面给他们太大的压力。要表现出亲切的善意，以减轻他们的紧张、焦虑。【2】 要亲切，但不要表现出依赖或过于有压力的亲密，因为他们喜欢与人保持一定的距离，要尊重他们的界线。【3】 要求他们做决定时，请尽量留给他们独处的时间和空间。【4】 当你请求他们某件事时，请记住你表达态度应该是一种请求而非要求。【5】 作为第五型人的伴侣，要增加他们的信任，减轻其焦虑最好的方法是身体的接触（ 例如按摩） ，这对他们而言是胜于语言的沟通。",
        "c": "【1】说话尽量说重点，他们才不会不耐烦，并愿意听你继续陈述。【2】你认为你们彼此起了争执、冲突，他却可能觉得这是很过瘾、很有效的沟通模式。所以你要记着，冲突对他们而言是进一步沟通的开始，而非结束。万一你觉得“争吵”太过厉害，感觉不舒服时，不妨直接告诉他们你的感受。【3】他们可以接受直接的批评，但不要取笑或讥讽他们，这会使他们产生敌意，做出攻击的行为。【4】玩弄权谋、操纵他们、说谎，都是他们讨厌的行为，记着跟他们沟通的最好方式是：直接、说重点。",
        "d": "【1】希望他们改变作风、或是思考其它方案最有效的方法便是：告诉他们这样做可能会有助于他们获得更好的结果。【2】如果你喜欢他们，不妨尽量配合他们，因为当你与他们站在同一阵线时，他们也乐于保护你，与你分享他们的成就。【3】如果你有被他们利用或操纵的感觉时，不妨让他们知道你的感受，因为他们有时真的会忽略别人的感受，告诉他们后，他们多半会收敛一些，特别是当他无心伤害你时。【4】过度地批评只会让他们为了讨好你、顺应你，而矫情地做改变。所以要真正改变他们，应该是去爱他们，设法让他们去探索自己真正的感觉。",
        "e": "【1】对于他们的付出，一定要表现出感激之意。【2】二型人最讨厌别人拒绝他们的好意，所以如果你想拒绝他们，就必须很清楚地把你的理由、感觉告诉他们，让他们知道真的不需要他去帮你什么，因为这才是你最需要的，也是对你最好的“帮助”。【3】二型人总是将关注放在别人身上，所以你不妨鼓励他们多谈谈自己，并告诉他们你想知道他们的事，多了解他们一些。【4】当你想为他做某件事时，告诉他们这么做会让你觉得快乐，他们便会接受你的付出。【5】当他们只顾着为别人忙碌，或是显得情绪化、心神不宁时，不妨问问他们正在想什么？心情如何？以及此刻有什么需要？",
    }

    __harmony_word = {  #  如果值为1，0为女强，1为男强
        "0":{"0": "五行相合，但是两个人无法对对方产生事业上实质性的帮助。", "1": {"0":"五行相合，女生对男生帮助会更大。","1":"五行相合，男生对女生帮助会更大。"}, "2": "五行相合，且两个人对对方可以产生事业上实质性的帮助。"}, # 比合
        "1":{"0": "五行相合，但是两个人无法对对方产生对事业上实质性的帮助。", "1": {"0":"五行相合，女生对男生帮助会更大。","1":"五行相合，但是男生会相对更多的消耗女生感情"}, "2": "五行相合，且两个人对对方可以产生事业上实质性的帮助。"}, # 女生男
        "2":{"0": "五行相克，但是相克不重，可以不予考虑相克。", "1": {"0":"五行相克，女生相对男生更加强势一些，但也会对男生给予更多帮助。","1":"五行相克，男生相对女生更加强势一些，女生很难管得住男生。"}, "2": "五行相克，可以相互帮助，但女生会占主动，男生相对被动。"}, # 女克男
        "3":{"0": "五行相克，但是相克不重，可以不予考虑相克。", "1": {"0":"五行相克，女生相对女生更加强势一些，男生很难管得住女生。","1":"五行相克，男生相对女生更加强势一些，但也会对女生给予更多帮助。"}, "2": "五行相克，可以相互帮助，但男生会占主动，女生相对被动。"}, # 男克女
        "4":{"0": "五行相合，但是两个人无法对对方产生对事业上实质性的帮助。", "1": {"0":"五行相合，但是女生会相对更多的消耗男生感情","1":"五行相合，男生对女生帮助会更大。"}, "2": "五行相合，且两个人对对方可以产生事业上实质性的帮助。"}, # 男生女
    }  # 0 为 双衰  1 为 1旺1衰  2 为 双旺

    __year_emotion = {
        "男":{
        "0": "感情：☆☆☆☆\n意味着：只能给一个稳定的评价，上一年如何这一年就如何，有对象的不会散，不过没有对象的在这一年也容易在感情上有惊喜。",
        "1": "感情：☆☆☆\n意味着：为了感情你做了很大的努力，表面上风平浪静，但感情之事让你心累，付出总比收获少。",
        "2": "感情：☆☆\n意味着：感情上求而不得。你是想和他好好在一起的，可就是如不了你的愿。",
        "3": "感情：☆\n意味着：不利感情发展。概括来讲就是很糟心，因为这一年你感情不稳定，对感情的关注度很低，即便有对象也很容易分手。",
        "4": "感情：☆☆☆☆☆\n意味着：利于感情发展。很容易有桃花或者是自己喜欢的人。",
        "5": "感情：☆☆☆\n意味着：感情的转折。如果之前没有对象，这一年容易有桃花；如果之前有对象，这一年在感情上不顺利。",
        "6": "感情：☆☆☆☆☆\n意味着：利于感情发展。很容易有桃花或者是自己喜欢的人。",
        "7": "感情：☆☆☆☆\n意味着：感情发展有坎坷。很容易有新桃花，但是并不是两情相悦的人，或者这一年经历过感情的坎坷。",
        "8": "感情：☆☆☆☆\n意味着：利于感情发展。比较容易有桃花，而且还是让自己心动的人。"},
        "女":{
        "0": "感情：☆☆☆☆\n意味着：只能给一个稳定的评价，上一年如何这一年就如何，有对象的不会散，不过没有对象的在这一年也容易在感情上有惊喜。",
        "1": "感情：☆☆☆\n意味着：为了感情你做了很大的努力，表面上风平浪静，但感情之事让你心累，付出总比收获少。",
        "2": "感情：☆☆\n意味着：感情上求而不得。你是想和他好好在一起的，可就是如不了你的愿。",
        "3": "感情：☆\n意味着：不利感情发展。概括来讲就是很糟心，因为这一年你感情不稳定，对感情的关注度很低，即便有对象也很容易分手。",
        "4": "感情：☆☆☆☆☆\n意味着：利于感情发展。很容易有桃花或者是自己喜欢的人。",
        "5": "感情：☆☆☆\n意味着：感情的转折。如果之前没有对象，这一年容易有桃花；如果之前有对象，这一年在感情上不顺利。",
        "6": "感情：☆☆☆☆☆\n意味着：利于感情发展。很容易有桃花或者是自己喜欢的人。",
        "7": "感情：☆☆☆☆\n意味着：感情发展有坎坷。很容易有新桃花，但是并不是两情相悦的人，或者这一年经历过感情的坎坷。",
        "8": "感情：☆☆☆☆\n意味着：利于感情发展。比较容易有桃花，而且还是让自己心动的人。"}
    }

    __year_money = {
        "男": {
        "0": "财运：☆☆☆☆\n意味着：财运平平，相比上一年差不多，所留下的钱还是稳步上涨的。",
        "1": "财运：☆☆☆\n意味着：控制不住想花钱，收入没怎么涨，花销倒是更大了。",
        "2": "财运：☆☆\n意味着：收入上受到了负面影响，挣得少或者有大的开销。",
        "3": "财运：☆\n意味着：不利财运。财运非常暗淡，入不敷出，很难存下钱，也会为财方面的事忧虑。",
        "4": "财运：☆☆☆☆☆\n意味着：利于努力得财。和上一年比起来，财运上好了一些，存下的钱相对变多。",
        "5": "财运：☆☆☆☆☆\n意味着：利于得外财。和上一年比起来，财运上好了一些，尤其是很容易添一些偏财。",
        "6": "财运：☆☆☆☆☆\n意味着：利于努力进财。和上一年比起来，进财更多或者花费更少，存款更多了一些。",
        "7": "财运：☆☆☆☆\n意味着：虽然相比之前有更多进财，但是花费也随之增多。",
        "8": "财运：☆☆☆\n意味着：在整体进项上出现问题，相比之前收入变少，或者花销更大。"},
        "女": {
        "0": "财运：☆☆☆☆\n意味着：财运平平，相比上一年差不多，所留下的钱还是稳步上涨的。",
        "1": "财运：☆☆☆\n意味着：控制不住想花钱，收入没怎么涨，花销倒是更大了。",
        "2": "财运：☆☆\n意味着：收入上受到了负面影响，挣得少或者有大的开销。",
        "3": "财运：☆\n意味着：不利财运。财运非常暗淡，入不敷出，很难存下钱，也会为财方面的事忧虑。",
        "4": "财运：☆☆☆☆☆\n意味着：利于努力得财。和上一年比起来，财运上好了一些，存下的钱相对变多。",
        "5": "财运：☆☆☆☆☆\n意味着：利于得外财。和上一年比起来，财运上好了一些，尤其是很容易添一些偏财。",
        "6": "财运：☆☆☆☆☆\n意味着：利于努力进财。和上一年比起来，进财更多或者花费更少，存款更多了一些。",
        "7": "财运：☆☆☆☆\n意味着：虽然相比之前有更多进财，但是花费也随之增多。",
        "8": "财运：☆☆☆\n意味着：在整体进项上出现问题，相比之前收入变少，或者花销更大。"}
    }

    def __init__(self):

        self.Year = Year()
        self.Char = Charactor()
        self.liunian = int(time.strftime("%Y",time.localtime(time.time())))

    def male(self,male_birth,sex):

        act_sex = 0
        if sex == "男":
            act_sex = 0

        """取男生五行主宰和数字"""
        charac = self.Char.result(male_birth)
        elements = charac[1]
        self.male_elements = self.__five_elements[elements]
        self.male_elements_num = int(elements)
        # print(self.male_elements,self.male_elements_num)

        """取男生主性格"""
        charactor = charac[2]
        self.male_charactor = self.__charactor[charactor]
        self.male_coop_char = self.__coop[charactor]
        self.male_attention = self.__attention[charactor]
        # print(self.male_charactor)

        """取男生缺乏性格"""
        self.non_charactor_male = charac[5]
        # non_charactor_two = charac[6]
        self.male_non_charactor = self.__non_charactor[self.non_charactor_male]

        """取男生主宰强弱"""
        self.male_gods = 0
        gods = charac[7]
        male_gods = int(gods)
        if male_gods >= 4:
            self.male_gods = 1
        else:
            self.male_gods = 0

        """取男生流年感情运势"""
        male_date1 = str(male_birth) + " " + str(act_sex) + " " + str(self.liunian - 2)
        male_date2 = str(male_birth) + " " + str(act_sex) + " " + str(self.liunian - 1)
        male_date3 = str(male_birth) + " " + str(act_sex) + " " + str(self.liunian)
        male_date4 = str(male_birth) + " " + str(act_sex) + " " + str(self.liunian + 1)

        emotion_one = self.Year.result(male_date1)
        emotion_two = self.Year.result(male_date2)
        emotion_three = self.Year.result(male_date3)
        emotion_four = self.Year.result(male_date4)
        self.male_emotion = [int(emotion_one[3]),int(emotion_two[3]),int(emotion_three[3]),int(emotion_four[3])]

        """取男生流年财运"""
        self.male_money = [int(emotion_one[4]),int(emotion_two[4]),int(emotion_three[4]),int(emotion_four[4])]

        return self.male_elements,self.male_elements_num,self.male_charactor,self.male_non_charactor,self.male_gods

    def female(self,female_birth,sex):
        act_sex = 1
        if sex == "女":
            act_sex = 1

        # """取女生真太阳时"""
        # suntime = TrueTime(y,m,d,h,t,c).truetime()
        # year = suntime[0]
        # month = suntime[1]
        # day = suntime[2]
        # hour = suntime[3]

        """取女生五行主宰和数字"""
        charac = self.Char.result(female_birth)
        elements = charac[1]
        self.female_elements = self.__five_elements[elements]
        self.female_elements_num = int(elements)
        # print(self.female_elements,self.female_elements_num)

        """取女生主性格"""
        charactor = charac[2]
        self.female_charactor = self.__charactor[charactor]
        self.female_coop_char = self.__coop[charactor]
        self.female_attention = self.__attention[charactor]
        # print(self.female_charactor)

        """取女生缺乏性格"""
        self.non_charactor_female = charac[5]
        # non_charactor_two = charac[6]
        self.female_non_charactor = self.__non_charactor[self.non_charactor_female]


        """取女生主宰强弱"""
        self.female_gods = 0
        gods = charac[7]
        female_gods = int(gods)
        if female_gods >= 4:
            self.female_gods = 1
        else:
            self.female_gods = 0

        """取女生流年感情运势"""
        female_date1 = str(female_birth) + " " + str(act_sex) + " " + str(self.liunian - 2)
        female_date2 = str(female_birth) + " " + str(act_sex) + " " + str(self.liunian - 1)
        female_date3 = str(female_birth) + " " + str(act_sex) + " " + str(self.liunian)
        female_date4 = str(female_birth) + " " + str(act_sex) + " " + str(self.liunian + 1)

        emotion_one = self.Year.result(female_date1)
        emotion_two = self.Year.result(female_date2)
        emotion_three = self.Year.result(female_date3)
        emotion_four = self.Year.result(female_date4)
        self.female_emotion = [int(emotion_one[3]),int(emotion_two[3]),int(emotion_three[3]),int(emotion_four[3])]
        """取男生流年财运"""
        self.female_money = [int(emotion_one[4]), int(emotion_two[4]), int(emotion_three[4]), int(emotion_four[4])]

        return self.female_elements, self.female_elements_num, self.female_charactor, self.female_non_charactor, self.female_gods

    def Harmony(self):
        assist = self.male_gods + self.female_gods
        harmony = (self.male_elements_num - self.female_elements_num + 5) % 5
        if assist == 1:
            harmony_words = self.__harmony_word[str(harmony)][str(assist)][str(self.male_gods)]
        else:
            harmony_words = self.__harmony_word[str(harmony)][str(assist)]

        harmony_score = int(((int(harmony) + 1)*0.8) * ((int(assist) + 1)*0.2) * 100 // 2.4)

        result = {"harmony_words":harmony_words,"harmony_score":harmony_score}

        return result

    def Charactor(self):

        self.char_result = {"male_char":self.male_charactor,"male_nonchar":self.male_non_charactor,"female_char":self.female_charactor,
                  "female_nonchar":self.female_non_charactor,"male_attention":self.female_attention, "female_attention":self.male_attention}

        return self.char_result

    def emotion(self):  #  男在前，女在后

        """self.liunian是以现在的年份为基础，计算流年"""
        male = {}
        female = {}

        year = [self.liunian-2, self.liunian - 1, self.liunian, self.liunian + 1]

        for (i,j,k) in zip(self.male_emotion,self.female_emotion,year):

            # predict = str(k) + "年," + self.__year_emotion["男"][str(i)] + self.__year_emotion["女"][str(j)]
            male[str(k)] = self.__year_emotion["男"][str(i)]
            female[str(k)] = self.__year_emotion["女"][str(j)]
            # z.append(predict)
        self.emotion_result = {"male_emotion" : male, "female_emotion" : female}
        # return z
        return self.emotion_result

    def cooperation(self):

        male = {}
        female = {}

        year = [self.liunian-2, self.liunian - 1, self.liunian, self.liunian + 1]

        for (i, j, k) in zip(self.male_money, self.female_money, year):
            male[str(k)] = self.__year_emotion["男"][str(i)]
            female[str(k)] = self.__year_emotion["女"][str(j)]
            # z.append(predict)
        self.coop_result = {"male_emotion": male, "female_emotion": female,"male_char":self.male_coop_char,"female_char":self.female_coop_char}
        # return z
        return self.coop_result

    def final(self,male_birth,male_sex,female_birth,female_sex):
        h = Merry()
        h1 = h.male(male_birth,male_sex)
        h2 = h.female(female_birth,female_sex)
        h3 = h.Harmony()

        h5 = h.Charactor()
        h6 = h.cooperation()
        h4 = h.emotion()

        result = {"harmony":h3,"charactor":h5,"emotion":h4,"cooperation":h6}  #  h4,h5在感情标签，h6在事业标签
        return result

if __name__ == '__main__':
    h = Merry()
    h1 = h.final("1988-8-6-9","男","1990-11-3-12","女")
    print(h1)



