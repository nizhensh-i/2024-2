# from flask_mail import Message
# msg = Message('test email',sender='zmc_li@foxmail.com',recipients=['zmc_li@foxmail.com'])
# msg.body = '天晴的一天'
# msg.html = '这是HTML实体'
import os

print(__file__)
print(__name__)

print(os.path.dirname(__file__))
# print(os.path.split(__file__))
print(os.path.join(os.path.dirname(__file__),'abc','ad'))
print(os.path.abspath(os.path.dirname(__file__)))
