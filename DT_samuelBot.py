#!/usr/bin/env python
# -*- coding:utf-8 -*-

import discord
import json
from DrinkShop import runLoki
with open("account.info", encoding="UTF-8") as f:
    accountDICT = json.loads(f.read())

class BotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None

        print("到到來自 {} 的訊息".format(message.author))
        print("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            print("本 bot 被叫到了！")
            msg = message.content.replace("<@!{}> ".format(self.user.id), "")
            if msg == 'ping':
                await message.reply('pong')
            elif msg == 'ping ping':
                await message.reply('pong pong')
            elif msg == '想喝奶茶了':
                await message.reply('別喝啦!!')
            elif msg == '今天晚餐你有頭緒嗎?':
                await message.reply('別吃省錢最快')

            elif msg == '想看貓貓':
                file = discord.File(r"./img/cat.png", filename="cat.png")
                await message.channel.send(file=file)

            elif msg == '想不到晚餐吃什麼':
                file = discord.File(r"./img/first.png", filename="first.png")
                await message.channel.send(file=file)

            elif msg == '聽說明天情人節?':
                file = discord.File(r"./img/dog.png", filename="dog.png")
                await message.channel.send(file=file)

            else:
                # 從這裡開始接上 NLU 模型
                responseSTR = "聽不懂你在說什麼?"
                inputLIST = [msg]
                filterLIST = []
                resultDICT = runLoki(inputLIST, filterLIST)
                print("Result => {}".format(resultDICT))

                if "sweetness" not in resultDICT:
                    resultDICT["sweetness"] = "正常糖"

                if "ice" in resultDICT and "hot" in resultDICT:
                    responseSTR = "請問是要喝熱飲還是冰飲呢?"

                if "ice" not in resultDICT and "hot" not in resultDICT:
                    resultDICT["ice"] = "正常冰"

                if "ice" in resultDICT and "hot" not in resultDICT:
                    responseSTR = "hello~ \n您點的總共是：\n"
                    for k in range(0, len(resultDICT["amount"])):
                        responseSTR = responseSTR + "{} X {} ({}、{})\n".format(resultDICT["item"][k],
                                                                               resultDICT["amount"][k],
                                                                               resultDICT["sweetness"][k], resultDICT["ice"][k])
                    responseSTR = responseSTR + "謝謝您的訂購\n"

                if "hot" in resultDICT and "ice" not in resultDICT:
                    responseSTR = "hello~~ \n您點的總共是：\n"
                    for k in range(0, len(resultDICT["amount"])):
                        responseSTR = responseSTR + "{} X {} ({}、{})\n".format(resultDICT["item"][k],
                                                                               resultDICT["amount"][k],
                                                                               resultDICT["sweetness"][k],
                                                                               resultDICT["hot"][0])
                    responseSTR = responseSTR + "謝謝您的訂購\n"

                if "Nothing" in resultDICT["item"]:
                    responseSTR = "我們沒有販售該產品，請選擇其他飲品"

                await message.reply(responseSTR)

if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])