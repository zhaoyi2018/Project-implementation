# 导入Flask类
from flask import Flask,render_template,request
import numpy as np
import matplotlib.pyplot as plt
names=['wg','zg','lmd','ssd','xh','yz','ts','zb','bj','bz','kf','sh']
datas=[16, 10, 50, 50, 10, 60, 10,10,10,15,12,33]
for i in range(12):
    plt.bar(names[i],datas[i])
plt.rcParams['font.sans-serif']=['SimHei']
plt.show()
# 实例化，可视为固定格式
app = Flask(__name__)

# route()方法用于设定路由；类似spring路由配置
#等价于在方法后写：app.add_url_rule('/', 'helloworld', hello_world)
@app.route('/')
def hello_world():
    return "舆情分析"

@app.route('/login.html')
def login_html():
    return render_template('login.html')


# link="../static/image/bar.png"

# names=['wg','zg','lmd','ssd','xh','yz','ts','zb','bj','bz','kf','sh']
# datas=[16, 10, 50, 50, 10, 60, 10,10,10,15,12,33]

goods_info='''商品名\n商品id\n商品好评率\n店铺'''

# def return_img_stream(img_local_path):
#   import base64
#   img_stream = ''
#   with open(img_local_path, 'rb') as img_f:  #,encoding='utf-8'
#     img_stream = base64.b64encode(img_f.read())
#   return img_stream
#   直接传路径字符串就好了...不比这么麻烦

com_png_path="../static/image/bar.png"
@app.route('/comments.html')
def com_html():
    # img_path = 'C:\\Users\\lenovo\\newproj\\static\\image\\bar.png'
    # img_stream = return_img_stream(img_path)
    return render_template('comments.html',goods_info=goods_info,com_png_path=com_png_path)

sel_com= [
    {'index': '1', 'comments': '''做工质感：外观来看，做工精致，手感特别好，和某果的产品不相上下
音质音效：收到第一时间进行了音效体验，个人感觉低音效果特别好，同样和三代的pro相比，个人感觉胜过pro三代，价格不到三代的三分之一
舒适度：入耳舒适度很好，配合不同尺寸的耳套，可以自由切换
续航能力：接电话可以续航一整天没问题'''},
    {'index': '2', 'comments': '''差评，不建议购买'''},
    {'index': '3', 'comments': '''心心念已经很久了，想小几百买副好点的真无线，这款性价比非常高，昨晚还在老罗直播间领了券。
音质不错，我要求不高，动感模式低音太轰头吃不消啊，均衡模式刚好，做工精致，非常满意'''},
    {'index': '4', 'comments': '''做工质感：做工很好 摸着手感还是不错的 开合盖子有点不怎么舒适 其他很好
音质音效：音效真心可以的  289这个价位 真香  香的很
舒适度：舒服 贼爽 哈哈哈
续航能力：刚刚带上 应该不差吧
其他特色：好看  带上不担心会掉    敲击的话貌似要用点力度'''},
    {'index': '5', 'comments': '''舒适度不好，带着耳朵痛，降噪效果很一般。比较容易掉，本来觉得耳套的问题，刚用一天，准备换个小耳套，结果还没用力，原配耳套就坏了。主要客户说是外力，没有售后服务。想问下，我是刻意撕坏的吗！'''},
    {'index': '6', 'comments': '''做工质感：光亮的白色，做工很精细
音质音效：有立体声效果
舒适度：很容易带，也不容易掉
刚到手，玩几天看看'''},
    {'index': '7', 'comments': '''做工质感：耳机盒钢琴版的质感，耳机看上去也很结实
音质音效：人声无敌，听rap超级爽，低音下沉很完美，轰头的感觉很爽！
舒适度：标准耳帽对于我来说有点大，换了s码耳帽马上舒服了，耳机很轻，戴上去无感！
续航能力：有待测试，反正我听了半小时手机还显示90多电
其他特色：降噪无敌了，可能是我第一次体验降噪耳机，家里开着风扇煮着饭，一打开降噪，明显感觉到风扇声没了，只能听到电视的人声，这降噪真的很可以了'''},
    {'index': '8', 'comments': '''使用了，还是很不错的。音质可以，收到包装简约不花哨，是我喜欢的风格，看着挺结实耐用的，质量非常强硬，听纯音乐的细腻感表达的也很不错，做工也很精细，颜色也很好看。使用是还是很不错的，包装也挺好的，声音也挺清晰的，价格便宜，喜欢，还会继续回购的。好评'''},
    {'index': '9','comments': '''"做工质感：非常温润如玉，摸起来很舒服细腻手感，上手犹如一块璞玉
音质音效：低音下表现很不错，音质在我使用的耳机穿戴设备能排进第一梯队，降噪效果也非常明显舒服。
舒适度：戴起来耳朵并没有胀痛感，佩戴无感很舒服。而且还有适合自己的耳套，调整大小舒适度，达到更好的音质降噪效果。
续航能力：使用了一下午感觉很不错，一小时游戏音乐只掉电百分之八。续航能力非常赞。开启降噪效果续航能力也很不错，足够日常户外一天无压力持续使用。
其他特色：在通话降噪上特别赞，以前跟别人通话尤其有电流声听不清，有了w51通话清晰没有任何噪音。通话全程流畅音质清晰表述内容。"
'''},
    {'index': '10', 'comments': '''"给老公买的，父亲节礼物。个人感觉和苹果没什么差异，音质都很好，质感也不错。降噪效果好，可以开启左右降噪模式，单边降噪适合出行上班。全部降噪后家里适用，真正做到了无干扰，两耳不闻窗外事了，哈哈
老公很满意，总体来讲很赞的一款"
'''},
]

dig_png_path="../static/image/走势图.png"
@app.route('/file.html')
def file_html():
    return render_template('file.html',sel_com=sel_com)
@app.route('/digital_com.html')
def dig_com_html():
    return render_template('digital_com.html',dig_png_path=dig_png_path)


@app.route("/login_request", methods=["post"])
def login_request():
	if request.form["username"]=="admin" and request.form["pwd"]=="123456":
		return render_template("search-1.html", result="登录成功")
	else:
		# 如何实现在单页面内, 时间事件交互
		return render_template("login-c.html", error="登录失败")

@app.route('/rest_test',methods=['POST'])
def hello_world1():
    """
    通过request.json以字典格式获取post的内容
    通过jsonify实现返回json格式
    """
    post_param = request.json
    result_dict = {
        "result_code": 2000,
        "post_param": post_param
    }
    return jsonify(result_dict)

if __name__ == '__main__':
    app.run( debug=True)