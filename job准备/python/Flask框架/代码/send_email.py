from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'zmc_li@foxmail.com'
app.config['MAIL_PASSWORD'] = 'xffugmemxvenbchf'

mail = Mail(app)


@app.route('/hello/a')
def hello():
    send_email()
    return '<h1>hello world</h1>' + '发送了邮件'


def send_email():
    msg = Message('test email', sender='zmc_li@foxmail.com', recipients=['zmc_li@foxmail.com'])
    msg.body = '天晴的一天'
    msg.html = '这是HTML实体'
    with app.app_context():
        mail.send(msg)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7090)
