from urllib.parse import quote
import os,sys
app=sys.path[0]
fo=[]
for a in os.walk(app):
    for b in a[2]:
        if(b[-3:]in['txt','TXT'])and(a[0].find('档案图')==-1):
            if a[0]not in fo:fo.append(a[0])
fo.sort()
fo2=[a for a in fo if a.count('/')>app.count('/') and'MD5s'not in a]
fo2.sort()
fo3=[a.split(' ')[1].split('（')[0].split('、')for a in fo2]
fo3.sort()
fo4=[]
for a in fo3:
    fo4.append([])
    for b in a:
        if'上海'in b:ap='上海'
        elif('自然'in b)and('姚文元'not in b):ap='自然'
        elif'毛泽东'in b or '모택동선집'in b:ap='毛泽东'
        elif'国际共产主义运动'in b:ap='共产主义'
        elif'党'in b:ap='党'
        elif'朝鲜'in b:ap='朝鲜'
        elif'军'in b:ap='军'
        elif'列宁'in b:ap='列宁'
        elif'信息'in b:ap='信息'
        elif'其他中央文革小组成员'in b:ap=['王力','关锋']
        elif'经济'in b:ap='经济'
        elif'贡萨罗'in b:ap='贡萨罗'
        elif'周恩来'in b:ap='周恩来'
        elif'华修'in b:ap='华修'
        elif'电影'in b:ap='电影'
        elif'哲学'in b:ap='哲学'
        elif'马列毛'in b:ap=['马克思','恩格斯','列宁','斯大林','毛泽东']
        elif'自学'in b:ap=['自学','自然']
        else:ap=b
        if ap not in fo4[len(fo4)-1]:
            if isinstance(ap,list):
                for c in ap:
                    fo4[len(fo4)-1].append(c)
            else:fo4[len(fo4)-1].append(ap)
fo3=fo4
fo3.sort()
for z in range(len(fo2)):
    fo=[]
    for a in os.walk(app):
        for b in a[2]:
            if(b[-3:]in['txt','TXT'])and(a[0].find('档案图')==-1):
                if a[0]not in fo:fo.append(a[0])
    fo=[a for a in fo if a.find(fo2[z])==-1 and a.find(fo2[z].split('/')[-1:][0])==-1 and a]
    fo.sort()
    fl=fo3[z]
    for d in fo:
        t='''“[%s](%s)”下的复现文件：\n\n| 复现TXT文件 | 复现PDF文件 |
| ------- | ------- |\n'''%(d.replace('%s/'%app,'').replace(app,''),'../%s'%quote(d.replace('%s/'%app,'').replace(app,'')))
        tk=False
        lm=[]
        for a in os.walk(d):
            for b in a[2]:
                if(b[-3:]in['txt','TXT'])and(a[0].find('档案图')==-1):
                    d=False
                    for c in fl:
                        if c in b:d=True;tk=True
                    if d:
                        lm.append([a[0],a[1],b])
        lm.sort(key=lambda x:x[2])
        for a in lm:
            b=a[2]
            t='%s| [%s](%s) | %s |\n'%(t,
                                       '.'.join(b.split('.')[:-1]),
                                       './%s'%(#'/'.join([quote(c)for c in a[0].replace('%s/'%app,'').replace(app,'').split('/')]),
                                       quote(b)),
                                       '[下载](%s)'%('./%s'%(#'/'.join([quote(c)for c in a[0].replace('%s/'%app,'').replace(app,'').split('/')]),
                                       quote('%s.pdf'%'.'.join(b.split('.')[:-1]))))if os.path.exists('%s/%s.pdf'%(a[0],'.'.join(b.split('.')[:-1])))else'暂无')
        if tk:
            if os.path.exists(pa:='%s/README.md'%fo2[z]):
                print(t)
                f=open(pa,'r');i=f.read();f.close()
                i='%s\n%s'%(i,t)
                f=open(pa,'w+');f.write(i);f.close()
