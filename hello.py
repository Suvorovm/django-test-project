def serverApp (environ,start_response):
    dataFromUser = environ['QUERY_STRING']
    resultList = dataFromUser.replace("?","").replace("/","").strip().split("&")
    start_response("200 OK", [("Content-Type", "text/plain")])
    return resultList


