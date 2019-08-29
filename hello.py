def printer(firstArg,SeconArg):
    print("xer")

def serverApp (environ,start_response):
    dataFromUser = environ['QUERY_STRING']
    print(dataFromUser.decode('utf-8'))
    resultList = dataFromUser.decode('utf-8').strip().replace("?","").replace("/","").replace("&"," ").split(" ")
    for i in range(0,len(resultList)):
        resultList[i] =(resultList[i] + '\n').encode("utf-8")
    start_response("200 OK", [("Content-Type", "text/plain")])
    return resultList


myDict = {'QUERY_STRING':"/?a=1&a=2&b=3"}

resultString =  serverApp(myDict,printer)
for i in resultString:
    print(i)