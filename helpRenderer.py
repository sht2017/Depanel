def renderHelp(file):
    with open('./help/'+str(file),'r',encoding="utf-8") as file:
        line=file.readlines()
        title=line[0]
        author=line[1]
        try:
            content1=line[2]
        except:
            content1=''
        try:
            content2=line[3]
        except:
            content2=''
        try:
            content3=line[4]
        except:
            content3=''
        try:
            content4=line[5]
        except:
            content4=''
        try:
            content5=line[6]
        except:
            content5=''
    return title,author,content1,content2,content3,content4,content5