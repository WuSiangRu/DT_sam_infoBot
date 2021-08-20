#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for ice

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_ice = True
userDefinedDICT = {"hot": ["常溫", "微溫", "燙", "微燙", "熱", "微熱", "溫"], "ice": ["去冰", "微冰", "少冰", "半冰", "全冰", "微微", "正常冰", "一分冰", "二分冰", "五分冰", "冰塊", "完全去冰", "冰度"], "sweetness": ["無糖", "微糖", "少糖", "半糖", "全糖", "微微", "正常糖", "糖", "一分糖", "二分糖", "五分糖", "八分糖", "甜度"], "原鄉四季": ["四季", "原鄉", "四季茶", "四季春茶", "原鄉茶", "原鄉四季茶", "原鄉四季春茶", "原鄉四季春茶", "四季原鄉"], "極品菁茶": ["極品菁", "菁茶", "極菁", "極菁茶", "菁茶極品"], "烏龍綠茶": ["烏龍綠", "烏", "綠茶烏龍"], "特級綠茶": ["特綠", "綠茶", "綠", "綠茶特級"], "特選普洱": ["特選普洱茶", "普洱", "普洱茶", "特普", "特級普洱茶", "特級普洱"], "翡翠烏龍": ["翡翠烏", "翡翠烏龍茶", "翡翠烏茶", "翡翠烏龍綠", "翡翠烏綠", "翠烏", "翠烏茶", "翡烏", "翡烏茶", "烏龍翡翠"], "錫蘭紅茶": ["錫蘭紅", "紅茶", "錫蘭", "錫蘭茶", "錫茶", "蘭茶", "紅", "紅茶錫蘭"], "嚴選高山茶": ["高山", "高山茶", "嚴選高山"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_ice:
        print("[ice] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一杯][錫蘭紅茶]和[烏龍綠茶]":
        resultDICT["ice"] = ["正常冰", "正常冰"]

    if utterance == "[一杯]大冰[綠][半糖][少冰]":
        if args[3] in userDefinedDICT["ice"]:
            resultDICT["ice"] = args[3]
        elif args[2] in userDefinedDICT["ice"]:
            resultDICT["ice"] = args[2]
        else:
            pass

    if utterance == "[我]要[菁茶][半糖]不要[冰塊]":
        if args[3] in userDefinedDICT["ice"]:
            resultDICT["ice"] = ["去冰"]
        elif args[2] in userDefinedDICT["ice"]:
            resultDICT["ice"] = args[2]
        else:
            pass

    if utterance == "[特選普洱]不要加[糖]跟[冰塊]":
        if args[2] in userDefinedDICT["ice"]:
            resultDICT["ice"] = ["去冰"]
        elif args[1] in userDefinedDICT["ice"]:
            resultDICT["ice"] = ["去冰"]
        else:
            pass

    if utterance == "[綠茶烏龍][三杯][都][少糖][少冰]":
        if args[4] in userDefinedDICT["ice"]:
            resultDICT["ice"] = args[4]
        elif args[3] in userDefinedDICT["ice"]:
            resultDICT["ice"] = args[3]
        else:
            pass

    if utterance == "[錫蘭紅茶][一杯]":
        resultDICT["ice"] = ["正常冰"]

    if utterance == "微微":
        if inputSTR.endswith(utterance):
            resultDICT["ice"] = ["微冰"]
        else:
            pass

    if utterance == "[兩杯][熱]的[錫蘭紅茶][甜度][冰塊][正常]":
        if args[4] in userDefinedDICT["ice"]:
            resultDICT["ice"] = ["全冰", "全冰"]
        elif args[3] in userDefinedDICT["ice"]:
            resultDICT["ice"] = ["全冰", "全冰"]
        else:
            pass

    if utterance == "[一杯][少糖][微冰][四季茶]和[半糖][去冰][烏龍綠]":
        if args[2] in userDefinedDICT["ice"] and args[5] in userDefinedDICT["ice"]:
            resultDICT["ice"] = [args[2], args[5]]
        elif args[1] in userDefinedDICT["ice"] and args[4] in userDefinedDICT["ice"]:
            resultDICT["ice"] = [args[1], args[4]]
        else:
            pass

    if utterance == "[兩杯][甜度][冰塊][正常][烏龍綠]":
        if args[2] in userDefinedDICT["ice"]:
            resultDICT["ice"] = ["正常冰"]
        elif args[1] in userDefinedDICT["ice"]:
            resultDICT["ice"] = ["正常冰"]
        else:
            pass

    if utterance == "[三杯][菁茶][一杯][少糖][微冰][一杯][半糖][去冰][一杯][全糖][正常冰]":
        if args[4] in userDefinedDICT["ice"] and args[7] in userDefinedDICT["ice"] and args[10] in userDefinedDICT["ice"]:
            resultDICT["ice"] = [args[4], args[7], args[10]]
        elif args[3] in userDefinedDICT["ice"] and args[6] in userDefinedDICT["ice"] and args[9] in userDefinedDICT["ice"]:
            resultDICT["ice"] = [args[3], args[6], args[9]]
        else:
            pass

    if utterance == "[我]要[三杯][烏龍綠][都][微糖][微冰]":
        if args[5] in userDefinedDICT["ice"]:
            resultDICT["ice"] = [args[5]]
        elif args[4] in userDefinedDICT["ice"]:
            resultDICT["ice"] = [args[4]]
        else:
            pass

    if utterance == "[兩杯][原鄉茶][都][全糖][去冰]":
        if args[4] in userDefinedDICT["ice"]:
            resultDICT["ice"] = [args[4]]
        elif args[3] in userDefinedDICT["ice"]:
            resultDICT["ice"] = [args[3]]
        else:
            pass

    if utterance == "[兩杯][紅茶][甜度][冰塊][正常]":
        if args[3] in userDefinedDICT["ice"]:
            resultDICT["ice"] = ["正常冰"]
        elif args[2] in userDefinedDICT["ice"]:
            resultDICT["ice"] = ["正常冰"]
        else:
            pass

    if utterance == "[一杯][半糖][微冰][特級普洱]":
        if args[2] in userDefinedDICT["ice"]:
            resultDICT["ice"] = [args[2]]
        elif args[1] in userDefinedDICT["ice"]:
            resultDICT["ice"] = [args[1]]
        else:
            pass

    if utterance == "[一杯][少糖][微冰][原鄉茶]和[一杯][無糖][去冰][嚴選高山]和[一杯][錫蘭茶][少糖][去冰]":
        if args[2] in userDefinedDICT["ice"] and args[6] in userDefinedDICT["ice"] and args[11] in userDefinedDICT[
            "ice"]:
            resultDICT["ice"] = [args[2], args[6], args[11]]
        elif args[1] in userDefinedDICT["ice"] and args[5] in userDefinedDICT["ice"] and args[10] in userDefinedDICT[
            "ice"]:
            resultDICT["ice"] = [args[1], args[5], args[10]]
        else:
            pass

    return resultDICT