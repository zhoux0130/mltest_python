import feedparser
import re

def getwordcounts(url,i):
    # 解析url下的文章,rss数据源的格式？？？
    d = feedparser.parse(url)
    print('parsefeed.....')
    wc ={}
    
    for e in d.entries:
        if 'summary' in e: summary = e.summary
        else: summary = e.description
        
        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] +=1
            
            
    return d.feed.title+str(i), wc

def getwords(html):
    # 去除所有的HTML标签
    txt = re.compile(r'<[^>]+>').sub('', html)
    # 利用所有非字母字符拆分单词 
    words = re.compile(r'[^A-Z^a-z]+').split(txt)
    # 转化为小写形式
    return [word.lower() for word in words if word != '']

#以文章为维度，对word进行统计
apcount={}
wordcount= {}
feedlist = [line for line in file('feedlist.txt')]
i=0
for feedurl in feedlist:
    print('执行这个博客url' + feedurl)
    title, wc = getwordcounts(feedurl,i)
    i+=1
    wordcount[title] = wc
    for word,count in wc.items():
        apcount.setdefault(word,0)
        if count >1:
            apcount[word]+=1
            
wordlist = []
for w, bc in apcount.items():
    # 统计一些有代表性的词汇，考察的词占单词总量的上下限
    frac = float(bc)/len(feedlist)
    #if frac > 0.1 and frac < 0.5: 
    wordlist.append(w)
    
out = file('blogdata.txt','w')
out.write('Blog')
for word in wordlist: out.write('\t%s' % word)
out.write('\n')
for blog, wc in wordcount.items():
    out.write(blog)
    for word in wordlist:
        if word in wc: out.write('\t%s' % wc[word])
        else: out.write('\t0')
    out.write('\n')
    
    