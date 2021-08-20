#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 2.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No Match Intent!"
                }
            ]
        }
"""

from requests import post
from requests import codes
import math
import json
from ArticutAPI import Articut
try:
    from intent import Loki_item
    from intent import Loki_sweetness
    from intent import Loki_hot
    from intent import Loki_ice
except:
    from .intent import Loki_item
    from .intent import Loki_sweetness
    from .intent import Loki_hot
    from .intent import Loki_ice

with open(r"./account.info", encoding="UTF-8") as f:
    accountINFO = json.load(f)
LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = accountINFO["username"]
LOKI_KEY = accountINFO["loki_key"]
Articut_KEY = accountINFO["apikey"]
# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "Connect failed."
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST, filterLIST=[]):
    resultDICT = {}
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # item
                if lokiRst.getIntent(index, resultIndex) == "item":
                    resultDICT = Loki_item.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # sweetness
                if lokiRst.getIntent(index, resultIndex) == "sweetness":
                    resultDICT = Loki_sweetness.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # hot
                if lokiRst.getIntent(index, resultIndex) == "hot":
                    resultDICT = Loki_hot.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # ice
                if lokiRst.getIntent(index, resultIndex) == "ice":
                    resultDICT = Loki_ice.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

import sys
if __name__ == "__main__":
    # item
    # print("[TEST] item")
    # inputLIST = ['普洱微微','錫蘭紅茶大杯','一杯大冰綠半糖少冰','我要菁茶半糖不要冰塊','錫蘭紅茶大杯少糖少冰','一杯錫蘭紅茶和烏龍綠茶','特選普洱不要加糖跟冰塊','兩杯熱的錫蘭紅茶甜度冰塊正常','一杯少糖微冰四季茶和半糖去冰烏龍綠']
    # testLoki(inputLIST, ['item'])
    # print("")

    # sweetness
    # print("[TEST] sweetness")
    # inputLIST = ['微微','錫蘭紅茶一杯','一杯大冰綠半糖少冰','我要菁茶半糖不要冰塊','錫蘭紅茶兩杯少糖少冰','一杯錫蘭紅茶和烏龍綠茶','特選普洱不要加糖跟冰塊']
    # testLoki(inputLIST, ['sweetness'])
    # print("")

    # hot
    # print("[TEST] hot")
    # inputLIST = ['翡翠烏綠兩杯','熱錫蘭紅茶一杯','溫原鄉四季茶一杯','一杯大冰綠半糖少冰','一杯高山茶少糖少冰','一杯錫蘭紅茶和烏龍綠茶']
    # testLoki(inputLIST, ['hot'])
    # print("")

    # ice
    # print("[TEST] ice")
    # inputLIST = ['微微','錫蘭紅茶一杯','一杯大冰綠半糖少冰','我要菁茶半糖不要冰塊','一杯錫蘭紅茶和烏龍綠茶','特選普洱不要加糖跟冰塊','綠茶烏龍三杯都少糖少冰']
    # testLoki(inputLIST, ['ice'])
    # print("")

    # 輸入其它句子試看看
    inputLIST = []
    inputSTR = input("請問您需要什麼飲料?:")
    inputLIST.append(inputSTR)
    print(inputLIST)
    # sys.exit()
    # inputLIST = ["我要三杯烏龍綠一杯少糖微冰一杯半糖去冰一杯無糖半冰"]
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Original_Result => {}".format(resultDICT))

    articut = Articut(username=USERNAME, apikey=Articut_KEY)
    for i in range(len(resultDICT["amount"])):
        # print(i)
        # print(resultDICT["amount"][i])
        Articut_Lv3_Result = articut.parse(resultDICT["amount"][i], level="lv3")
        amount = Articut_Lv3_Result["number"][resultDICT["amount"][i]]
        resultDICT["amount"][i] = amount

    check_temp = 0
    if "hot" in resultDICT.keys():
        check_temp += 1
    if "ice" in resultDICT.keys():
        check_temp += 1
    # print(check_temp)

    if check_temp >= 2:
        print("請問是要喝熱飲還是冰飲呢?")

    elif "Nothing" in resultDICT["item"]:
        print("我們沒有販售該產品喔")

    else:
        print("Result_with_articut_LV3 => {}".format(resultDICT))
        print("您點的總共是:")
        for i in range(len(resultDICT["item"])):
            print(resultDICT["item"][i] + " * " + str(resultDICT["amount"][i]) + " (" + resultDICT["sweetness"][i] + ","
                  + resultDICT["ice"][i] + ")")
            # for j in range(amount):
            #     print("(" + resultDICT["sweetness"][j] + "," + resultDICT["ice"][j] + ")")