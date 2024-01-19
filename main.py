import aiogram.filters as filters
import aiogram
import asyncio
import os
import sqlite3
import modules.data as m_data
import modules.sqlite as m_sqlite
import modules.image as m_image
import modules.keyboard as m_keyboard
@m_data.dp.message(filters.CommandStart())
async def start(message:aiogram.types.Message):
    await message.answer(text="Hello",reply_markup=m_keyboard.create_keyboard([["hot-dog","burger"]]))
    # #await m_image.image("burger.jpg",message,reply_markup=m_keyboard.create_inline_keyboard())
@m_data.dp.message()
async def continue_1(message:aiogram.types.Message):
    print(message.text)
    if message.text=="burger":
        await m_image.image("burger.jpg",message,reply_markup=m_keyboard.create_inline_keyboard())
    elif message.text=="hot-dog":
        await m_image.image("hotDog.jpg",message,reply_markup=m_keyboard.create_inline_keyboard())
@m_data.dp.callback_query()
async def call_back(callback:aiogram.types.callback_query.CallbackQuery):
    print(callback.data)
    if 'Buy' in callback.data:
        inline_keyboard =callback.message.reply_markup
        count = '0'
        if 'Buy' != callback.data:
            count = callback.data.split(' ')
            print(count)
            count = str(int(count[-1])+1)
            print(type(count))
        if len(inline_keyboard.inline_keyboard)==1:
            inline_keyboard.inline_keyboard.append(m_keyboard.create_inline_keyboard([['Accept']]).inline_keyboard[0])
        print('0'==count)
        print(type(inline_keyboard))
        print()
        inline_keyboard.inline_keyboard[0][0].callback_data = f'Buy {count}'
        inline_keyboard.inline_keyboard[0][0].text = f'Buy {count}'
        await callback.message.edit_reply_markup(reply_markup=inline_keyboard,inline_message_id=callback.inline_message_id)
    if 'Cancel' in callback.data:
        inline_keyboard =callback.message.reply_markup
        count = '0'
        if 'Buy' != callback.message.reply_markup.inline_keyboard[0][0].callback_data:
            count = callback.message.reply_markup.inline_keyboard[0][0].callback_data.split(' ')
            print(count)
            count = str(int(count[-1])-1)
            print(type(count))
            
        print('0'==count)
        print(type(inline_keyboard))
        print()
        inline_keyboard.inline_keyboard[0][0].callback_data = f'Buy {count}'
        inline_keyboard.inline_keyboard[0][0].text = f'Buy {count}'
        await callback.message.edit_reply_markup(reply_markup=inline_keyboard,inline_message_id=callback.inline_message_id)
    # if len(inline_keyboard)== 1:

    #     # inline_keyboard.append([aiogram.types.InlineKeyboardButton(text="accept",callback_data="accept")])
    #     # inline_keyboard[0][0].callback_data = 'buy 0'
        
    #     print(','.split(str(inline_keyboard)),str(inline_keyboard))#я за водой
    #     print('\n')
    #     print('\n')
    #     print('\n')
async def main():
    await m_data.dp.start_polling(m_data.bot)
asyncio.run(main())
m_sqlite.data.commit()
m_sqlite.data.close()