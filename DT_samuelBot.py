#!/usr/bin/env python
# -*- coding:utf-8 -*-

import discord
import json

with open("account.info", encoding="utf-8") as f:
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
            if msg == 'ping ping':
                await message.reply('pong pong')
            if msg == '想喝奶茶了':
                await message.reply('別喝啦!!')
            if msg == '今天晚餐你有頭緒嗎?':
                await message.reply('別吃省錢最快')

            if msg == '想看貓貓':
                file = discord.File(r"./img/cat.png", filename="cat.png")
                await message.channel.send(file=file)

            if msg == '想不到晚餐吃什麼':
                file = discord.File(r"./img/first.png", filename="first.png")
                await message.channel.send(file=file)

            if msg == '聽說明天情人節?':
                file = discord.File(r"./img/dog.png", filename="dog.png")
                await message.channel.send(file=file)

if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])