# -*- coding:utf-8 -*-
"""
作者:mengchen
日期:2021.05.24
"""
import requests
import re
import schedule

def daka():
        #打卡地址
        url="https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login"
        #代理头部
        headers={
        'Referer':'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        }
        post_data={
        'uid':'*********',                                                          #学号
        'upw':'********',                                                           #密码
        'smbtn':'%E8%BF%9B%E5%85%A5%E5%81%A5%E5%BA%B7%E7%8A%B6%E5%86%B5%E4%B8%8A%E6%8A%A5%E5%B9%B3%E5%8F%B0',
        'hh28':'722',
        }

        response=requests.post(url,headers=headers,data=post_data)
        html=response.content.decode("utf-8")

        #更新url
        url1=(re.findall('n="(.+?)"}',html))[0]                                        #从上一个页面切割到新的url
        response1=requests.get(url1,headers=headers)
        html1=response1.content.decode("utf-8")
        #print(html1)

        url2=(re.findall('src="(.+?)"',html1))[0]
        response2=requests.get(url2,headers=headers)
        html2=response2.content.decode("utf-8")
        #print(html2)

        ptopid=re.findall('ptopid" value="(.+?)"><',html2)[0]                           #从上一个页面切割得到ptopid
        sid=re.findall('ue="(.+?)"><',html2)[-1]                                        #从上一个页面切割得到sid

        url3="https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb"
        post_data1="day6=b&did=1&door=&men6=a&"+"ptopid={ptopid}&sid={sid}".format(ptopid=ptopid, sid=sid)
        response3=requests.post(url3,headers=headers,data=post_data1)
        html3=response3.content.decode("utf-8")
        #print(html3)

        ptopid1=re.findall('ptopid" value="(.+?)"><',html3)[0]
        sid1=re.findall('ue="(.+?)"><',html3)[-1]
        post_data2="myvs_1=%E5%90%A6&myvs_2=%E5%90%A6&myvs_3=%E5%90%A6&myvs_4=%E5%90%A6&myvs_5=%E5%90%A6&myvs_6=%E5%90%A6&myvs_7=%E5%90%A6&myvs_8=%E5%90%A6&myvs_9=%E5%90%A6&myvs_10=%E5%90%A6&myvs_11=%E5%90%A6&myvs_12=%E5%90%A6&myvs_13a=41&myvs_13b=4101&myvs_13c=%E6%B2%B3%E5%8D%97%E7%9C%81.%E6%96%B0%E4%B9%A1%E5%B8%82.%E5%BB%B6%E6%B4%A5%E5%8E%BF%E4%B8%9C%E5%B1%AF%E9%95%87%E5%A4%A7%E7%8E%8B%E5%BA%84%E6%9D%91325&myvs_14=%E5%90%A6&myvs_14b=&memo22=%E7%94%A8%E6%88%B7%E6%8B%92%E7%BB%9D&did=2&door=&day6=b&men6=a&sheng6=&shi6=&fun3=&jingdu=0.000000&weidu=0.000000&"+"ptopid={ptopid}&sid={sid}".format(ptopid=ptopid1, sid=sid1)
        response4=requests.post(url3,headers=headers,data=post_data2)
        html4 = response4.content.decode("utf-8")
        print(html4)

def Sendmall():
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header

    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "1375669090@qq.com"  # 用户名
    mail_pass = "*********"  # 口令

    sender = '1375669090@qq.com'  ##发邮件账号
    receivers = ['1375669090@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('恭喜你打卡成功!!!!', 'plain', 'utf-8')
    message['From'] = Header("mengchen", 'utf-8')
    message['To'] = Header("other", 'utf-8')

    subject = '恭喜你打卡成功!!!!'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

def main():
        try:
            daka()
            print("打卡成功")
            Sendmall()
        except:
            print("error error error")
            print("打卡失败")

schedule.every().day.at("07:00").do(main()) #定时打卡用
#schedule.every(1).seconds.do(main()) #测试用
while True:
    schedule.run_pending()
