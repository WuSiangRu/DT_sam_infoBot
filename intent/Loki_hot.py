#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for hot

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_hot = True
userDefinedDICT = {"hot": ["常溫", "微溫", "燙", "微燙", "熱", "微熱", "溫"], "ice": ["去冰", "微冰", "少冰", "半冰", "全冰", "微微", "正常冰", "一分冰", "二分冰", "五分冰", "冰塊", "完全去冰", "冰度"], "sweetness": ["無糖", "微糖", "少糖", "半糖", "全糖", "微微", "正常糖", "糖", "一分糖", "二分糖", "五分糖", "八分糖", "甜度"], "原鄉四季": ["四季", "原鄉", "四季茶", "四季春茶", "原鄉茶", "原鄉四季茶", "原鄉四季春茶", "原鄉四季春茶", "四季原鄉"], "極品菁茶": ["極品菁", "菁茶", "極菁", "極菁茶", "菁茶極品"], "烏龍綠茶": ["烏龍綠", "烏", "綠茶烏龍"], "特級綠茶": ["特綠", "綠茶", "綠", "綠茶特級"], "特選普洱": ["特選普洱茶", "普洱", "普洱茶", "特普", "特級普洱茶", "特級普洱"], "翡翠烏龍": ["翡翠烏", "翡翠烏龍茶", "翡翠烏茶", "翡翠烏龍綠", "翡翠烏綠", "翠烏", "翠烏茶", "翡烏", "翡烏茶", "烏龍翡翠"], "錫蘭紅茶": ["錫蘭紅", "紅茶", "錫蘭", "錫蘭茶", "錫茶", "蘭茶", "紅", "紅茶錫蘭"], "嚴選高山茶": ["高山", "高山茶", "嚴選高山"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_hot:
        print("[hot] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一杯][錫蘭紅茶]和[烏龍綠茶]":
        pass

    if utterance == "[一杯][高山茶][少糖][少冰]":
        pass

    if utterance == "[一杯]大冰[綠][半糖][少冰]":
        pass

    if utterance == "[熱][錫蘭紅茶][一杯]":
        resultDICT["hot"] = args[0]

    if utterance == "[翡翠烏綠][兩杯]":
        pass

    if utterance == "[兩杯][熱]的[錫蘭紅茶][甜度][冰塊][正常]":
        resultDICT["hot"] = [args[1], args[1]]

    if utterance == "[一杯][少糖][微冰][四季茶]和[半糖][去冰][烏龍綠]":
        pass

    if utterance == "[兩杯][甜度][冰塊][正常][烏龍綠]":
        pass

    if utterance == "[三杯][菁茶][一杯][少糖][微冰][一杯][半糖][去冰][一杯][全糖][正常冰]":
        pass

    if utterance == "[兩杯][原鄉茶][都][全糖][去冰]":
        pass

    if utterance == "[兩杯][紅茶][甜度][冰塊][正常]":
        pass

    if utterance == "[一杯][半糖][微冰][特級普洱]":
        pass

    return resultDICT