# -*- coding: utf-8 -*-
from telethon import TelegramClient
from telethon import events
from config import api_id, api_hash, print_delay, mask_delay, moon_delay
import asyncio  # noqa
from asyncio import sleep
from random import randint, getrandbits
import emoji  # noqa

client = TelegramClient('Session', api_id, api_hash)
client.start()

emoji_mixes = {
    'heart_mix': [
        ['ᅠ   ', '❤️'],  # red
        ['ᅠ   ', '🖤'],   # black
        ['ᅠ   ', '🧡'],   # yellow
        ['ᅠ   ', '🤎'],   # brown
        ['ᅠ   ', '💚'],  # green
        ['ᅠ   ', '💙'],  # blue
        ['ᅠ   ', '💜'],  # purple
        ['ᅠ   ', '💛']   # gold
    ],
    'thx_mix': [
        ['ᅠ   ', '🥰'],
        ['ᅠ   ', '☺️'],
        ['ᅠ   ', '😘'],
        ['ᅠ   ', '😍'],
        ['ᅠ   ', '😊'],
        ['ᅠ   ', '❤️‍🔥']
    ],
    'moon_mix': list('🌑🌘🌗🌖🌕🌝🌕🌔🌓🌒🌑🌚'),
    'dick_mix': ['❄️']
}

help_message = '''
1. .text - print text
2. `/love` - love mask
3. `/thx` - thanks mask
4. `/dick` - draw dick
5. `/pussy` - draw pussy
6. `/moon` - moon animations
7. `/snow` - snow animation
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
ᅠ
      3
    42
    5 1
   6    0
  7   ♥️♥️
 8   ♥️♥️♥️
9      ♥️♥️♥️
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

pussy = '''
ᅠ
        💋
    💋    💋
    💋       💋
💋   💋    💋
💋   💋    💋
💋   💋    💋
💋   💋    💋
   💋  💋  💋
     💋  💋
        💋
'''

snow = '''
☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️
00000000000
00000000000
00000000000
00000000000
00000000000
00000000000
00000000000
⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️
'''


async def mask_printer(event, mix_arr):
    text_send = ''
    for line in heart_mask:
        text_send += line.replace(
            '0', mix_arr[0][0]
        ).replace('1', mix_arr[0][1]) + '\n'
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
                i = randint(0, mix_arr_len-1)
                if sign == '0':
                    text_send += sign.replace('0', mix_arr[i][0])
                else:
                    text_send += sign.replace('1', mix_arr[i][1])
            text_send += '\n'
        await client.edit_message(event.message, text_send)
        await sleep(mask_delay)


async def dick_anim(event, mix_arr, inp_text=''):
    total_nums = 10
    jet_len = 3
    for i in range(-jet_len, total_nums+1):
        text = xyz
        for j in range(i, i+jet_len):
            text = text.replace(str(j), mix_arr[0])
            # print(j, end=', ')
        # print()
        for j in range(total_nums):
            text = text.replace(str(j), '       ')
        await client.edit_message(event.message, text)
        await sleep(mask_delay)
    text = 'В тебя запустили Волшебным хуем! ✨'
    text += xyz
    for i in range(total_nums):
        text = text.replace(str(i), mix_arr[0])
    if inp_text != '':
        text += f'\n{inp_text}'
    else:
        text += '\n☃️ Бросай хуй в тех, кого не хочешь потерять в 2022 году ⛄️'
    await client.edit_message(event.message, text)


@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    if event.text.startswith('/love'):  # /love any text
        text = event.text[len('/love'):]
        mix_arr = emoji_mixes['heart_mix']
        await mask_printer(event, mix_arr)

        if text.strip() != '':
            await client.edit_message(event.message, text)
        else:
            await client.edit_message(event.message, '𝙸 ❤️ 𝐔!')

    elif event.text.startswith('/thx'):  # /thx any text
        text = event.text[len('/thx'):]
        mix_arr = emoji_mixes['thx_mix']
        await mask2_printer(event, mix_arr)
        
        if text.strip() != '':
            await client.edit_message(event.message, text)
        else:
            i = randint(0, len(mix_arr)-1)
            text_send = ''
            for line in heart_mask:
                text_send += line.replace(
                    '0', mix_arr[i][0]
                ).replace('1', mix_arr[i][1]) + '\n'
            await client.edit_message(event.message, text_send)

    elif event.text.startswith('/moon'):  # /moon
        mix_arr = emoji_mixes['moon_mix']
        for sign in mix_arr:
            await client.edit_message(event.message, sign)
            await sleep(moon_delay)

    elif event.text.startswith('/dick'):  # /dick
        text = event.text[len('/dick'):]
        mix_arr = emoji_mixes['dick_mix']
        await dick_anim(event, mix_arr, text.strip())
        # await client.edit_message(event.message, xyz)

    elif event.text.startswith('/pussy'):  # /pussy
        text = 'В вас запустили Волшебной пиздой! ✨'
        text += pussy
        text += '\n⛄️ Запиздячь ею тех, кого не хочешь потерять в 2022 ⛄️'
        await client.edit_message(event.message, text)

    elif event.text.startswith('/snow'):  # /snow
        text = event.text[len('/snow'):]
        splitted = snow.split('\n')[1:-1]
        msg = snow.replace('0', 'ᅠ')
        await client.edit_message(event.message, msg)
        await sleep(mask_delay)

        addon = False
        sn_len = len(splitted[1])
        sn_height = len(splitted)
        # add snows
        for n in range(1, sn_height-1):
            last_msg = msg.split('\n')
            msg = splitted[0] + '\n'
            for _ in last_msg[1:n+1]:
                for i in range(sn_len):
                    val = bool(getrandbits(1))
                    if val == 0:
                        msg += 'ᅠ  '
                        if not addon:
                            msg += ' '
                            addon = True
                        else:
                            addon = False
                    else:
                        msg += '❄️'
                msg += '\n'
            if n < sn_height-2:
                msg += 'ᅠ' * sn_len + '\n' * (sn_height - 2 - n)
            msg += splitted[-1]
            await client.edit_message(event.message, msg)
            await sleep(mask_delay)

    elif event.text.startswith('.'):  # .hello world
        text = event.text[len('.'):]
        if len(text) > 127 or text.strip() == '':
            print('Don\'t forget about telegram limitations..', end=' ')
            print(f'I won\'t send it! Text length is {len(text)}')
        else:
            text_send = ''
            for sign in text:
                text_send += sign
                await client.edit_message(event.message, text_send + '░')
                await sleep(print_delay)
            
            await client.edit_message(event.message, text_send)

    elif event.text.startswith('/help'):  # help
        await client.edit_message(event.message, help_message)
        await sleep(moon_delay)

client.run_until_disconnected()
