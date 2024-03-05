from urllib.parse import quote
import os,sys
app=sys.path[0]
fo=[]
for a in os.walk(app):
    for b in a[2]:
        if(b[-3:]in['txt','TXT'])and(a[0].find('档案图')==-1):
            if a[0]not in fo:fo.append(a[0])
fo=[a for a in fo if a!=app]
fo.sort()
for d in fo:
    t='''| TXT文件 | PDF文件 |
| ------- | ------- |\n'''
    lm=[]
    for a in os.walk(d):
        for b in a[2]:
            lm.append([a[0],a[1],b])
    lm.sort(key=lambda x:x[2])
    for a in lm:
        b=a[2]
        if(b[-3:]in['txt','TXT'])and(a[0].find('档案图')==-1):
            t='%s| [%s](%s) | %s |\n'%(t,'.'.join(b.split('.')[:-1]),'%s'%(#'/'.join([quote(c)for c in a[0].replace('%s/'%app,'').replace(app,'').split('/')]),
            quote(b)),'[下载](%s)'%('%s'%(#'/'.join([quote(c)for c in a[0].replace('%s/'%app,'').replace(app,'').split('/')]),
            quote('%s.pdf'%'.'.join(b.split('.')[:-1]))))if os.path.exists('%s/%s.pdf'%(a[0],'.'.join(b.split('.')[:-1])))else'暂无')
    f=open('%s/README.md'%d,'w+');f.write(t);f.close()
