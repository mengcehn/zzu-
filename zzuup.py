# -*- coding:utf-8 -*-
"""
作者:mengchen
日期:2022/2/23
"""
import requests
import re
import schedule

def daka():
    # 打卡地址
    url = "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login"
    # 代理头部
    headers = {
        'Referer': 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    }
    post_data = {
        'uid': '*********',  # 学号
        'upw': '********',  # 密码
        'smbtn': '%E8%BF%9B%E5%85%A5%E5%81%A5%E5%BA%B7%E7%8A%B6%E5%86%B5%E4%B8%8A%E6%8A%A5%E5%B9%B3%E5%8F%B0',
        'hh28': '688',
    }

    response = requests.post(url, headers=headers, data=post_data)
    html = response.content.decode("utf-8")
    ptopid = re.findall('ptopid=(.+?)&sid=',html)[0]
    url1 = "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb"
    key = {'ptopid': ptopid}
    r = requests.get(url1, params=key)
    html1 = r.content.decode("utf-8")
    print(html1)


def main():
    try:
        daka()
        print("打卡成功")
    except:
        print("error error error")
        print("打卡失败")
schedule.every().day.at("07:00").do(main) #定时打卡用
while True:
    schedule.run_pending()
