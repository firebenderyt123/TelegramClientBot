# -*- coding: utf-8 -*-
from telethon import TelegramClient
from telethon import events
from config import *
import asyncio
from asyncio import sleep
from random import randrange
import emoji

client = TelegramClient('Session', api_id, api_hash)
client.start()

emoji_mixes = {
	'heart_mix': [
		['🤍', '❤️'], # white red
		['🤍', '🖤'],  # white black
		['🤍', '🧡'],  # white yellow
		['🤍', '🤎'],  # white brown
		['🤍', '💚'], # white green
		['🤍', '💙'], # white blue
		['🤍', '💜'], # white purple
		['🤍', '💛']  # white gold
	],
	'thx_mix': [
		['◽️', '🥰'],
		['◽️', '☺️'],
		['◽️', '😘'],
		['◽️', '😍'],
		['◽️', '😊'],
		['◽️', '❤️‍🔥']
	],
	'moon_mix': list('🌑🌘🌗🌖🌕🌝🌕🌔🌓🌒🌑🌚')
}

help_message = '''
1. .text - print text
2. /love - love mask
3. /thx - thanks mask
4. /fuck - draw xep
5. /moon - moon animations
'''

heart_mask = '''
000000000
001101100
011111110
011111110
011111110
001111100
000111000
000010000
000000000
'''.strip().split('\n')

xyz = '''
\\\\\\♥️♥️
♥️♥️♥️
 ♥️♥️♥️
      ❤️❤️❤️
         ❤️❤️❤️
           ❤️❤️❤️
            ❤️❤️❤️ 
             ❤️❤️❤️
             ❤️❤️❤️ 
            ❤️❤️❤️
     ❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️     ❤️❤️❤️
      ❤️❤️      ❤️❤️
'''

async def mask_printer(event, mix_arr):
	text_send = ''
	for line in heart_mask:
		text_send += line.replace('0', mix_arr[0][0]).replace('1', mix_arr[0][1]) + '\n'
		await client.edit_message(event.message, text_send)
		await sleep(mask_delay)
	prev_emoji = mix_arr[0][1]
	
	for i in range(1, len(mix_arr)):
		text_send = text_send.replace(prev_emoji, mix_arr[i][1])
		prev_emoji = mix_arr[i][1]
		await client.edit_message(event.message, text_send)
		await sleep(mask_delay)
	
	for sign in text_send:
		if sign == prev_emoji:
			text_send = text_send.replace(prev_emoji, mix_arr[0][1], 1)
			await client.edit_message(event.message, text_send)
			await sleep(mask_delay)

async def mask2_printer(event, mix_arr):
	mix_arr_len = len(mix_arr)
	for n in range(12):
		text_send = ''
		for line in heart_mask:
			for sign in line:
				i = randrange(0, mix_arr_len-1, 1)
				if sign == '0':
					text_send += sign.replace('0', mix_arr[i][0])
				else:
					text_send += sign.replace('1', mix_arr[i][1])
			text_send += '\n'
		await client.edit_message(event.message, text_send)
		await sleep(mask_delay)



@client.on(events.NewMessage(outgoing=True))
async def handler(event):

	if event.text.startswith('/love'): # /love any text
		text = event.text[len('/love'):]
		mix_arr = emoji_mixes['heart_mix']
		await mask_printer(event, mix_arr)

		if text.strip() != '':
			await client.edit_message(event.message, text)
		else:
			await client.edit_message(event.message, '𝙸 ❤️ 𝐔!')

	elif event.text.startswith('/thx'): # /thx any text
		text = event.text[len('/thx'):]
		mix_arr = emoji_mixes['thx_mix']
		await mask2_printer(event, mix_arr)
		
		if text.strip() != '':
			await client.edit_message(event.message, text)
		else:
			i = randrange(0, len(mix_arr)-1, 1)
			text_send = ''
			for line in heart_mask:
				text_send += line.replace('0', mix_arr[i][0]).replace('1', mix_arr[i][1]) + '\n'
			await client.edit_message(event.message, text_send)

	elif event.text.startswith('/moon'): # /moon
		text = event.text[len('/moon'):]
		mix_arr = emoji_mixes['moon_mix']
		for sign in mix_arr:
			await client.edit_message(event.message, sign)
			await sleep(moon_delay)

	elif event.text.startswith('/fuck'): # /moon
		await client.edit_message(event.message, xyz)

	elif event.text.startswith('.'): # .hello world
		text = event.text[len('.'):]
		if len(text) > 127 or text.strip() == '':
			print(f'Don\'t forget about telegram limitations.. I won\'t send it! Text length is {len(text)}')
		else:
			text_send = ''
			for sign in text:
				text_send += sign
				await client.edit_message(event.message, text_send + '░')
				await sleep(print_delay)
			
			await client.edit_message(event.message, text_send)

	elif event.text.startswith('/help'): # help
		await client.edit_message(event.message, help_message)
		await sleep(moon_delay)

client.run_until_disconnected()