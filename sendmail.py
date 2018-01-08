#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

mail_user = 'xuwenhao001@mail.com'    # 发件人邮箱账号
mail_pass = 'test1'              # 发件人邮箱密码
mail_to_list = ["xuwenhao001@deppon.com", "123864643@qq.com"]      # 收件人邮箱账号，我这边发送给自己
mail_host = 'client.mail.com'

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com">这是一个链接</a></p>
"""

def mail( mail_user, mail_pass, mail_to_list,mail_host,mail_msg):
    ret = True
    try:
        msg = MIMEText(mail_msg, 'html', 'utf-8')
        msg['From'] = formataddr(["test@mail.com", mail_user])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["test@mail.com", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP(mail_host, timeout=30)  # 发件人邮箱中的SMTP服务器，端口是25
        #server.set_debuglevel(1)  #用来打开debug信息
        server.login(mail_user, mail_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(mail_user, [to_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()

if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")