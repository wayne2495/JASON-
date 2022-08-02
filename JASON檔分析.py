import sys
import urllib.request as httplib  # 3.x
import json


#
# ######### 由網路下載 JSON 的 字串
# #url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=b3abedf0-aeae-4523-a804-6e807cbad589&rid=bf55b21a-2b7c-4ede-8048-f75420344aed"
# #url="http://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json"
url="https://ws.kinmen.gov.tw/001/Upload/0/relfile/0/0/ac05c8b2-7a86-47e9-8ac1-df4811b0ab41.json"
req = httplib.Request( url,data=None,
    headers={ 'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"})
reponse = httplib.urlopen(req)               # 開啟連線動作
if reponse.code==200:                        # 當連線正常時
    contents=reponse.read()                  # 讀取網頁內容
    contents=contents.decode("utf-8")        # 轉換編碼為 utf-8
    print(contents)
    # 儲存檔案
    with open("data.json", "w", encoding="utf-8") as f:
        f.write(contents)







######### 字串 換成  JSON 的 Dict
obj1= json.loads(contents)
dict3 = {"序號":"7777","民宿編號":"666","中文名稱":"XXXX","地址":"XXXXXXXXX","電話或手機":"18115151","經營者姓名":"古峻瑋","合計總房間數":"10"}
obj1.append(dict3)
# for dict1 in obj1:
#     print("健走步道地點: ",dict1["健走步道地點"])


# print(obj1["retVal"])
# print(obj1["retVal"]["2001"])
# print(obj1["retVal"]["2001"]["sna"])
# print("場站的目前車輛",obj1["retVal"]["2001"]["sbi"])
# for dict2 in obj1["infos"]:
#     print("商家名稱: ",dict2["Name"]," 商家地址: ",dict2["Add"])


    # print("  場地:",obj1["infos"][id]["Name"])



