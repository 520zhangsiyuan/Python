#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *  
import urllib.request
import urllib.parse
import json
import sys
root = Tk()
root.title("英汉互译")
root.geometry()
root.resizable(True, True)
e = StringVar()
#判断是否是中文
def chinese(uchar):
    str1 = True
    if uchar >= 65 and uchar<=126:
        str1 = False
    return str1
#程序主体
def validateText():
        #进入此方法删除text里的数据
        text.delete(0.0, END)
        word = entry.get()
        if(word !=""):
            data = {}
            count = word.split()
            english = "en"
            china = "zh"
            #中英文表单不同
            if(chinese(ord(word[0]))):
                english = "zh"
                china = "en"
            data['from'] = english
            data['to'] = china
            data['query'] = word
            data['transtype'] = "translang"
            data['simple_means_flag'] = "3"
            data = urllib.parse.urlencode(data).encode('utf-8')
            #发出请求
            response = urllib.request.urlopen('http://fanyi.baidu.com/v2transapi',data)
            respon = urllib.request.Request('http://fanyi.baidu.com/v2transapi',data)
            respon.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0")
            cat = response.read().decode('utf-8')
            #截取想要获取的数据
            word1 = json.loads(cat)
            word3 = word1['trans_result']['data'][0]['dst']
            word4 = ""
            #with open('2.txt','wb') as f:
                #f.write(str(word1).encode('utf-8'))
                        
            for i in word3:
                if(i != '+'):
                    word4 = word4 + i
            text.insert(INSERT,word4)
            if(word1['trans_result'].get('keywords')):
                if(word1['trans_result']['keywords']):
                    if(len(word1['trans_result']['keywords'])>1):
                        text.insert(INSERT,"详细解释：")
                        for i in  word1['trans_result']['keywords']:
                            wor = i['word']
                            word2 =i['means']
                            text.insert(INSERT,"\n\n%s：%s"%(wor,word2))
                    else:
                        word2 = word1['trans_result']['keywords'][0]['means']
                        text.insert(INSERT,"\n\n详细解释：%s"%word2)
        else:
            text.insert(INSERT,"请重新输入！")
def diao(event):
         validateText()
#按钮
def packBtn():
    btnSer = Button(root,text = '翻译',fg = "white", bg = "blue",command=validateText, width=15, height=3)
    btnSer.pack(padx=20, side='left')
    btnQuit = Button(root, text='退出', fg = "white",bg = "blue",command=root.quit, width=15, height=3)
    btnQuit.pack(padx=20, side='right')
#显示文本    
def text():
    text = Text(root)
    text.tag_config("start", background="black",borderwidth = 5, foreground="green")
    text.insert(INSERT, "翻译结果。。。。")
    text.pack()
    return text
#输入框
def input1():
    entry = Entry(root,text="请输入..." ,textvariable=e, validate='focusout',  validatecommand=validateText,width = 80,borderwidth = 5,fg="blue")  
    entry.bind("<Key-Return>",diao)
    entry.pack()
    return entry
entry = input1()
text =  text()
packBtn()
root.mainloop()  

