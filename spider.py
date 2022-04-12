# -*- codeing = utf-8 -*-
# @Time : 2022-01-01 8:11
# @Author : 齐物逍遥游
# @File : spider.py
# @Software: PyCharm


from bs4 import BeautifulSoup        #网页解析，获取数据
import re           #正则表达式，进行文字匹配
import urllib.request,urllib.error         #制定URL,获取网页数据
import xlwt         #进行excel操作
import sqlite3      #进行SQLite操作


# def saveData2DB(datalist, dbpath):
#     pass


def main():
    baseurl = "https://movie.douban.com/top250?start=0"
    #1.爬取网页
    datalist = getDate(baseurl)
    #savepath = "豆瓣电影Top250.xls"  #路径说明：.表示当前文件所在路径下，表示文件系统的路径
    dbpath = "movie.db"
    #3 保存数据
    #saveDate(datalist,savepath)
    saveData2DB(datalist,dbpath)

    #askURL("https://movie.douban.com/top250?start=0")

#制定获取到影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')     #compile:创建正则表达式对象，表示规则（字符串的模式）
#制定获取影片图片链接的规则
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)   #.S表示忽略可能出现的换行符
#影片片名
findtitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#找到影片简介
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)


#爬取网页
def getDate(baseurl):
    datalist = []
    for i  in range(0,10):      #调用获取页面信息的函数，10次
        url = baseurl + str(i*25)
        html= askURL(url)   #保存获取到的网页源码

        #2 逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):     #查找符合要求的字符串，形成列表

            #print(item)   #测试查看电影item的全部信息
            data = []    #保存一部电影的所有信息
            item = str(item)

            #获取到影片详情的链接
            link = re.findall(findLink,item)[0]        #re库通过正则表达式查找指定的字符串
            data.append(link)                          #添加链接

            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)                        #添加图片

            titles = re.findall(findtitle,item)        #片名可能只有中文名，没有外国名
            if(len(titles) == 2):                       #如果片名既有中文又有外国名
                ctitle = titles[0]                      #添加中文名
                data.append(ctitle)
                otitle = titles[1].replace(" / ","")      #添加外文名，并去掉外文名中的“/”
                data.append(otitle)
            else:                                       #如果片名只有中文名
                data.append(titles[0])
                data.append(' ')                        #给外文名留空

            rating = re.findall(findRating,item)[0]      #添加评分
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0]     #添加评价人数
            data.append(judgeNum)

            inq = re.findall(findInq,item)            #添加概述
            if len(inq) != 0:    #如果概述不为空
               inq = inq[0].replace("。","")     #去掉句号
               data.append(inq)
            else:                                #如果概述为空
               data.append(" ")         #留空

            bd = re.findall(findBd,item)[0]
            bd = re.sub('br(\s+)?/>(\s+)?'," ",bd)      #去掉<br/>
            bd = re.sub(' / '," ",bd)     #去掉/
            data.append(bd.strip())     #去掉前后的空格

            datalist.append(data)       #把处理好的一部电影信息放入datalist

    #print(datalist)
    return datalist




#得到指定一个URL的网页内容
def askURL(url):
    head={                     #模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 96.0.4664.110Safari / 537.36",'Cookie': 'gr_user_id=f9a2f2a5-c8ba-498a-b6db-0dedcd7576d4; _vwo_uuid_v2=DCBC21D7118B30090BB6F7CB49D6DE10D|57e97412b8da79a39d18c112959ab506; douban-fav-remind=1; _vwo_uuid_v2=DCBC21D7118B30090BB6F7CB49D6DE10D|57e97412b8da79a39d18c112959ab506; _ga=GA1.2.245646375.1605315347; __gpi=00000000-0000-0000-0000-000000000000&ZG91YmFuLmNvbQ==&Lw==; trc_cookie_storage=taboola%2520global%253Auser-id%3Dba306030-17d2-421e-aae7-43ccb0474696-tuct6b8ac35; __gads=ID=81c101c4b2a4c207-22ab9df5f6cb001c:T=1616570712:RT=1635756355:S=ALNI_MaKGlegSXmlXhn91wJSKq0YWeZ-8Q; bid=e23vUjC00vc; ll="118159"; __yadk_uid=EYyRAS7vcW9mg6z92zugRQAvjlzsLjpJ; viewed="6726127_35275774_26610702_27081766_25919579_1144185_35154591_1067236_2993966_3812574"; __utma=30149280.245646375.1605315347.1641361694.1641361694.1; __utmz=30149280.1641361694.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1641361964%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.717513958.1605487505.1641125023.1641361964.64; __utmb=223695111.0.10.1641361964; __utmz=223695111.1641361964.64.36.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; __utmv=30149280.22558; __utmb=30149280.5.10.1641361694; dbcl2="225585964:nzNvs8w+Wd8"; ck=jbRy; _pk_id.100001.4cf6=ea3d493156bf90ec.1605487505.64.1641366108.1641126221.; __utmc=30149280; __utmc=223695111'

    }
                           #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（我们可以接收什么水平的数据）
    request = urllib.request.Request(url,headers=head)
    huml = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"response"):
            print(e.response)

    return html

#3 保存数据
def saveDate(datalist,savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0) # 创建workbook对象
    sheet =book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)  # 创建工作表
    col = ("电影链接","图片链接","中文名","外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i]) #列名
    for i in range(0,250):
        print("第%d条" %i)
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])


    book.save(savepath)  # 保存数据表

def saveData2DB(datalist,dbpath):
    #print("...")
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            data[index] = '"'+data[index]+'"'
        sql = '''
            insert into movie250(
            info_link,pic_link,cname,ename,score,rated,introduction,info)
            values(%s)'''%",".join(data)
        #print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

def init_db(dbpath):
    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric ,
        rated numeric ,
        introduction text,
        info text
        )
    
    
    ''' #创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":       #当程序执行时
#调用函数
    main()
    #init_db("movietest.db")
    print("爬取完毕！")