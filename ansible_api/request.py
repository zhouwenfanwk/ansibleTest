# pip3 install requests
# urls for request

import requests, demjson

url = 'https://www.1data.work:1255/auth/login-processing'
url1 = 'https://www.1data.work:1255/etl/pipeline/add'

url2_update = 'https://www.1data.work:1255/etl/pipeline/update'

url_getPipList = 'https://www.1data.work:1255/etl/pipeline/page'

data = {
    'username' : 'sa',
    'password' : '0bHqBXIi3'
}

TARGET = {
    'id': '5ea29e58fa7edf4824febb94',
    'userId': '5ea29e58fa7edf4824febb94',
    'phone': '18200000000'
}

# params for request_get
params = {
	'createUser':'',
	'currentPage':1,
	'mainVersion':'true',
	'name':'',
	'pageSize':10,
	'status':'DRAFT',
	'used':'false'
}

# paramas for request_post
data1 = {
    "createUser": "sa",
    "description": "Test",
    "name": "postTest"
}
# target for check
T1 = {
    "status": 300000,
    "message": "管道名称已经存在"
}

T2 = {
    "status": 200,
    "message": "保存管道成功",
    "data": "6010d93421c2d530272b60fb"
}

data_update = {
    "batchSize": "10",
    "clusterId": "5fd9b532d6fa7632b4ff3c24",
    "commitType": 0,
    "description": "",
    "errorStrategy": "discard",
    "esUrl": None,
    "id": "6010d93421c2d530272b60fb",
    "index": None,
    "metricRuleParams": [],
    "name": "testPythonAnsible",
    "previewSource": "CONFIGURED_SOURCE",
    "rememberMe": True,
    "sdcId": "6007e31b19051f5328a23562",
    "showFieldType": True,
    "showHeader": True,
    "testJson": None,
    "timeout": 0,
    "type": None,
    "updateUser": "sa",
    "writeToDestinations": True,
    "originalJson": "{\"cells\":[{\"type\":\"app.FlowchartStart\",\"size\":{\"width\":48,\"height\":48},\"ports\":{\"items\":[{\"group\":\"out\",\"id\":\"bcb11321-9615-477f-893b-27d5ae295830\"}]},\"position\":{\"x\":408,\"y\":120},\"comp\":\"jdbc\",\"id\":\"d7f5c9ca-e895-4722-81cf-74c861c1dc63\",\"z\":1,\"attrs\":{\"body\":{\"fill\":\"#147DA0\"},\"icon\":{\"xlinkHref\":\"\"},\"label\":{\"text\":\"JDBC Query Consumer\"},\"params\":{\"connId\":\"5fabdb1919051f539cf364db\",\"entityType\":1,\"xPos\":\"\",\"yPos\":\"\",\"inputLanes\":[],\"outputLanes\":[],\"entityInstance\":\"jdbcQuery\",\"name\":\"JDBC Query Consumer\",\"connType\":\"mysql\",\"host\":\"gwssi-cdh0106\",\"port\":\"3307\",\"schemaName\":\"caojun\",\"incrMode\":false,\"offsetColume\":\"\",\"initiaOffset\":\"\",\"sql\":\"select XH,YS,RQ from test005\",\"useAuth\":true,\"username\":\"root\",\"password\":\"gwssi123\",\"description\":\"Test\"}}},{\"type\":\"app.Message\",\"size\":{\"width\":368,\"height\":80},\"ports\":{\"items\":[{\"group\":\"in\",\"id\":\"636450a5-18a3-4eb9-852e-8727b3829ccb\"},{\"group\":\"out\",\"attrs\":{\"portLabel\":{\"text\":\"out\"}},\"id\":\"8269d690-e13a-4359-bc8c-984e5d71171c\"}]},\"position\":{\"x\":424,\"y\":248},\"comp\":\"evaluator\",\"id\":\"75bc98ba-c737-4552-9b78-e28063a8da2d\",\"z\":3,\"attrs\":{\"body\":{\"stroke\":\"#E8E8E8\"},\"label\":{\"text\":\"计算器\"},\"description\":{\"text\":\"数据操作描述\"},\"icon\":{\"xlinkHref\":\"\"},\"params\":{\"connId\":\"\",\"entityType\":2,\"xPos\":\"\",\"yPos\":\"\",\"inputLanes\":[],\"outputLanes\":[],\"entityInstance\":\"expressionEvaluator\",\"name\":\"计算器\",\"fieldExpressionList\":[],\"headerExpressionList\":[{\"headerAttribute\":\"\",\"headerExpression\":\"\"}]}}},{\"type\":\"app.Link\",\"labels\":[{\"attrs\":{\"labelText\":{\"text\":\"\"}},\"position\":{\"distance\":0.25}}],\"source\":{\"id\":\"d7f5c9ca-e895-4722-81cf-74c861c1dc63\",\"magnet\":\"portBody\",\"port\":\"bcb11321-9615-477f-893b-27d5ae295830\"},\"target\":{\"id\":\"75bc98ba-c737-4552-9b78-e28063a8da2d\",\"magnet\":\"portBody\",\"port\":\"636450a5-18a3-4eb9-852e-8727b3829ccb\"},\"id\":\"778af189-f69e-4e6b-a64f-fa49d70f8965\",\"z\":4,\"attrs\":{}},{\"type\":\"app.FlowchartEnd\",\"size\":{\"width\":48,\"height\":48},\"ports\":{\"items\":[{\"group\":\"in\",\"id\":\"e94910b7-f208-48e8-93c9-3abf85247a1b\"}]},\"position\":{\"x\":736,\"y\":416},\"comp\":\"mongo_out\",\"compType\":\"mongo\",\"id\":\"28e8b8ed-2322-4f97-a440-ac202c182df8\",\"z\":5,\"attrs\":{\"body\":{\"fill\":\"#3059AA\"},\"icon\":{\"xlinkHref\":\"\"},\"label\":{\"text\":\"MongoDB\"},\"params\":{\"connId\":\"5fed8e4a21c2d54e96312a1e\",\"entityType\":3,\"xPos\":\"\",\"yPos\":\"\",\"inputLanes\":[],\"outputLanes\":[],\"entityInstance\":\"mongodbProducer\",\"name\":\"MongoDB\",\"connType\":\"mongo\",\"connectionString\":\"mongodb://GWSSI-CDH0106:27027\",\"database\":\"etl\",\"collection\":\"wznTest\",\"authType\":\"LDAP\",\"username\":\"gwssi\",\"password\":\"7h2t2N0Ls\",\"uniqueKeyFieldList\":[],\"upsert\":false,\"description\":\"Test\"}}},{\"type\":\"app.Link\",\"labels\":[{\"attrs\":{\"labelText\":{\"text\":\"\"}},\"position\":{\"distance\":0.25}}],\"source\":{\"id\":\"75bc98ba-c737-4552-9b78-e28063a8da2d\",\"magnet\":\"portBody\",\"port\":\"8269d690-e13a-4359-bc8c-984e5d71171c\"},\"target\":{\"id\":\"28e8b8ed-2322-4f97-a440-ac202c182df8\",\"magnet\":\"portBody\",\"port\":\"e94910b7-f208-48e8-93c9-3abf85247a1b\"},\"id\":\"ffe48e75-3a74-4b4b-83c2-beca0b721855\",\"z\":6,\"attrs\":{}}]}",
    "entities": [
        {
            "connId": "5fabdb1919051f539cf364db",
            "entityType": 1,
            "xPos": 408,
            "yPos": 120,
            "inputLanes": [],
            "outputLanes": [
                "75bc98bac73745529b78e28063a8da2d"
            ],
            "entityInstance": "jdbcQuery",
            "name": "JDBC Query Consumer",
            "connType": "mysql",
            "host": "gwssi-cdh0106",
            "port": "3307",
            "schemaName": "caojun",
            "incrMode": False,
            "offsetColume": "",
            "initiaOffset": "",
            "sql": "select XH,YS,RQ from test005",
            "useAuth": True,
            "username": "root",
            "password": "gwssi123",
            "description": "Test"
        },
        {
            "connId": "",
            "entityType": 2,
            "xPos": 424,
            "yPos": 248,
            "inputLanes": [
                "75bc98bac73745529b78e28063a8da2d"
            ],
            "outputLanes": [
                "28e8b8ed23224f97a440ac202c182df8"
            ],
            "entityInstance": "expressionEvaluator",
            "name": "计算器",
            "fieldExpressionList": [],
            "headerExpressionList": [
                {
                    "headerAttribute": "",
                    "headerExpression": ""
                }
            ]
        },
        {
            "connId": "5fed8e4a21c2d54e96312a1e",
            "entityType": 3,
            "xPos": 736,
            "yPos": 416,
            "inputLanes": [
                "28e8b8ed23224f97a440ac202c182df8"
            ],
            "outputLanes": [],
            "entityInstance": "mongodbProducer",
            "name": "MongoDB",
            "connType": "mongo",
            "connectionString": "mongodb://GWSSI-CDH0106:27027",
            "database": "etl",
            "collection": "wznTest",
            "authType": "LDAP",
            "username": "gwssi",
            "password": "7h2t2N0Ls",
            "uniqueKeyFieldList": [],
            "upsert": False,
            "description": "Test"
        }
    ]
}

headers = {
    'cookie' : '',
    'content-type' : 'application/json'
}

# get cookies
def login(url, data, TAR):

    r = py_request_post(url=url, data=data, headers={}, TARGET=TAR)
    headers['cookie'] = 'SESSION=' + requests.utils.dict_from_cookiejar(r.cookies)['SESSION'] + ';Path=/;HttpOnly;'

    return r.text


def py_request_post(url, headers, data, TARGET):

    try:
        r = requests.post(url=url, data=data, headers=headers, verify=False)

    except:
        raise Exception('Connection failed')

    if r.status_code!=200:
        raise Exception(r.text)

    res = r.json()
    for k in TARGET.keys():
        assert res[k] == TARGET[k]

    return r


def py_request_get(url, headers, params, TARGET):

    try:
        r = requests.get(url=url, params=params, headers=headers, verify=False)
    except:
        raise Exception('Connection failed')

    return r.text


# if __name__ == "__main__":

login(url=url, data=data, TAR=TARGET)
# print(py_request_get(url=url_getPipList, params=params, headers=headers,TARGET={}))

print(py_request_post(url=url2_update, headers=headers, data=demjson.encode(data_update), TARGET = T2).text)





