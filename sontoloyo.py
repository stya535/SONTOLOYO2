import TERX
from TERX import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
#SALAM SANTUN
#=============
cl = LineClient("stya535@gmail.com","putriku75")
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = cl.getProfile()
lineSettings = cl.getSettings()
mid = cl.getProfile().mid
responsename1 = cl.getProfile().displayName

ki = LineClient("citocitolani@yahoo.com","putriku75")
ki.log("Auth Token : " + str(ki.authToken))
channel1 = LineChannel(ki)
ki.log("Channel Access Token : " + str(channel1.channelAccessToken))
lineProfile = ki.getProfile()
lineSettings = ki.getSettings()
Amid = ki.getProfile().mid
responsename2 = ki.getProfile().displayName

kk = LineClient("manispipit@yahoo.com","putriku75")
kk.log("Auth Token : " + str(kk.authToken))
channel2 = LineChannel(kk)
kk.log("Channel Access Token : " + str(channel2.channelAccessToken))
lineProfile = kk.getProfile()
lineSettings = kk.getSettings()
Bmid = ki.getProfile().mid
responsename3 = ki.getProfile().displayName

kc = LineClient("puputmulani@yahoo.com","putriku75")
kc.log("Auth Token : " + str(kc.authToken))
channel3 = LineChannel(kc)
kc.log("Channel Access Token : " + str(channel3.channelAccessToken))
lineProfile = kc.getProfile()
lineSettings = kc.getSettings()
Cmid = kc.getProfile().mid
responsename4 = kc.getProfile().displayName

km = LineClient("bledekngampar@yahoo.com","putriku75")
km.log("Auth Token : " + str(km.authToken))
channel4 = LineChannel(km)
km.log("Channel Access Token : " + str(channel4.channelAccessToken))
lineProfile = km.getProfile()
lineSettings = km.getSettings()
Dmid = km.getProfile().mid
responsename5 = km.getProfile().displayName

kb = LineClient("gludugngampar@yahoo.com","putriku75")
kb.log("Auth Token : " + str(kb.authToken))
channel5 = LineChannel(kb)
kb.log("Channel Access Token : " + str(channel5.channelAccessToken))
lineProfile = kb.getProfile()
lineSettings = kb.getSettings()
Emid = kb.getProfile().mid
responsename6 = kb.getProfile().displayName

kn = LineClient("dewapetir938@yahoo.com","putriku75")
kn.log("Auth Token : " + str(kn.authToken))
channel6 = LineChannel(kn)
kn.log("Channel Access Token : " + str(channel6.channelAccessToken))
lineProfile = kn.getProfile()
lineSettings = kn.getSettings()
Fmid = kb.getProfile().mid
responsename7 = kn.getProfile().displayName

ko = LineClient("dewikembang38@yahoo.com","putriku75")
ko.log("Auth Token : " + str(ko.authToken))
channel7 = LineChannel(ko)
ko.log("Channel Access Token : " + str(channel7.channelAccessToken))
lineProfile = ko.getProfile()
lineSettings = ko.getSettings()
Gmid = ko.getProfile().mid
responsename8 = kb.getProfile().displayName

kw = LineClient("agajanuar@yahoo.com","putriku75")
kw.log("Auth Token : " + str(kw.authToken))
channel8 = LineChannel(kw)
kw.log("Channel Access Token : " + str(channel8.channelAccessToken))
lineProfile = kw.getProfile()
lineSettings = kw.getSettings()
Hmid = kw.getProfile().mid
responsename9 = kw.getProfile().displayName

ke = LineClient("teguhsumarno152@yahoo.com","putriku75")
ke.log("Auth Token : " + str(ke.authToken))
channel9 = LineChannel(ke)
ke.log("Channel Access Token : " + str(channel9.channelAccessToken))
lineProfile = ke.getProfile()
lineSettings = ke.getSettings()
Imid = ke.getProfile().mid
responsename10 = ke.getProfile().displayName

ky = LineClient("kasems26@yahoo.com","putriku75")
ky.log("Auth Token : " + str(ky.authToken))
channel10 = LineChannel(ky)
ky.log("Channel Access Token : " + str(channel10.channelAccessToken))
lineProfile = ky.getProfile()
lineSettings = ky.getSettings()
Jmid = ky.getProfile().mid
responsename11 = ky.getProfile().displayName

sw = LineClient("manjamanis77@yahoo.com","putriku75")
sw.log("Auth Token : " + str(sw.authToken))
channel11 = LineChannel(sw)
sw.log("Channel Access Token : " + str(channel11.channelAccessToken))
lineProfile = sw.getProfile()
lineSettings = sw.getSettings()
Zmid = sw.getProfile().mid
responsename12 = sw.getProfile().displayName

sx = LineClient("slametputra255@yahoo.com","putriku75")
sx.log("Auth Token : " + str(sx.authToken))
channel12 = LineChannel(sx)
sx.log("Channel Access Token : " + str(channel12.channelAccessToken))
lineProfile = sx.getProfile()
lineSettings = sx.getSettings()
Xmid = sx.getProfile().mid
responsename13 = sx.getProfile().displayName

js = LineClient("smulyani777@yahoo.com","putriku75")
js.log("Auth Token : " + str(js.authToken))
channel13 = LineChannel(js)
js.log("Channel Access Token : " + str(channel13.channelAccessToken))
lineProfile = js.getProfile()
lineSettings = js.getSettings()
JSmid = js.getProfile().mid
responsename14 = js.getProfile().displayName

print("---LOGIN SUCCES---")

poll = LinePoll(cl)
call = cl
creator = ["uf50d888821632d32461e37153ac775c0"]
owner = ["uf50d888821632d32461e37153ac775c0"]
admin = ["uf50d888821632d32461e37153ac775c0"]
staff = ["uf50d888821632d32461e37153ac775c0"]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = km.getProfile().mid
Emid = kb.getProfile().mid
Fmid = kn.getProfile().mid
Gmid = ko.getProfile().mid
Hmid = kw.getProfile().mid
Imid = ke.getProfile().mid
Jmid = ky.getProfile().mid
Zmid = sw.getProfile().mid
Xmid = sx.getProfile().mid
JSmid = js.getProfile().mid
KAC = [cl,ki,kk,kc,km,kb,kn,ko,kw,ke,ky]
ABC = [ki,kk,kc,km,kb,kn,ko,kw,ke,ky]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Zmid,Xmid,JSmid]
Dpk = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []
welcome = []

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = km.getProfile().displayName
responsename5 = kb.getProfile().displayName
responsename6 = kn.getProfile().displayName
responsename7 = ko.getProfile().displayName
responsename8 = kw.getProfile().displayName
responsename9 = ke.getProfile().displayName
responsename10 = ky.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":True,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 5,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoRead':False,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":True,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "protectantijsOn":True,
    "ghostOn":True,
    "mention":"Lagi ngintip yee,,, yaaa...! gabung sini 😊",
    "Respontag":"Apaan tag-teg kalo penting VC aja langsung",
    "welcome":"Selamat datang & semoga betah",
    "comment":"Like like & like ",
    "message":"Terimakasih sudah add saya\n Butuh Selfbot only\n Butuh Selbot dengan asist\n Protect Room/Ivent\n Jaga room/Event\n Songbook smule\n follower smule\n V.I.P Smule\n stiker Line\n Langsung saya Tanya sama bosku yaa\n id Line udo1993 atau castello_bardian\n Thanks yaaa..!\n FI FAMZ BOTZ",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "DAFTAR JONES「{}」\n\n  [ Silahkan pilih ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1
