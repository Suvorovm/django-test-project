def serverApp (environ,start_response):
    dataFromUser = environ['QUERY_STRING'] 
    resultList = dataFromUser.strip().replace("?","").replace("/","").replace("&"," ").split(" ")
    for i in range(0,len(resultList)):
        resultList[i] =(resultList[i] + '\n').encode("utf-8")
    start_response("200 OK", [("Content-Type", "text/plain")])
    return resultList
