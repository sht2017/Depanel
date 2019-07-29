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
    return title,author,content1,content2,content3