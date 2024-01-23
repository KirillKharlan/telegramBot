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
    m_sqlite.cursor.execute(f"CREATE TABLE IF NOT EXISTS {message.from_user.username} (INTEGER PRIMARY KEY,id)")
    m_sqlite.add_column(name_column="burger",type_column="INTEGER",name_table=message.from_user.username)
    m_sqlite.add_column(name_column="hotDog",type_column="INTEGER",name_table=message.from_user.username)
    await message.answer(text="Hello",reply_markup=m_keyboard.create_keyboard([["hot-dog","burger"]]))
    # #await m_image.image("burger.jpg",message,reply_markup=m_keyboard.create_inline_keyboard())
@m_data.dp.message()
async def continue_1(message:aiogram.types.Message):
    print(message) 
    m_sqlite.cursor.execute(f"CREATE TABLE IF NOT EXISTS {message.from_user.username} (INTEGER PRIMARY KEY,id)")
    m_sqlite.add_column(name_column="burger",type_column="INTEGER",name_table=message.from_user.username)
    m_sqlite.add_column(name_column="hotDog",type_column="INTEGER",name_table=message.from_user.username)
    if message.text=="burger":
        await m_image.image("burger.jpg",message,reply_markup=m_keyboard.create_inline_keyboard())
    elif message.text=="hot-dog":
        await m_image.image("hotDog.jpg",message,reply_markup=m_keyboard.create_inline_keyboard())
@m_data.dp.callback_query()
async def call_back(callback:aiogram.types.callback_query.CallbackQuery):
    m_sqlite.cursor.execute(f"CREATE TABLE IF NOT EXISTS {callback.message.chat.username} (INTEGER PRIMARY KEY,id)")
    m_sqlite.add_column(name_column="burger",type_column="INTEGER",name_table=callback.message.chat.username)
    m_sqlite.add_column(name_column="hotDog",type_column="INTEGER",name_table=callback.message.chat.username)
    m_sqlite.add_column(name_column="ok",type_column="INTEGER",name_table=callback.message.chat.username)
    print(callback.message.photo)
    # 8266 - burger  AgACAgIAAxkDAAIBBGWuuJ0oMnJYwIpf95NkRpK35TbWAALt0jEbntNRSQHvDJ-4XD86AQADAgADcwADNAQ
    # 5332 - hot-dog AgACAgIAAxkDAAIBAmWuuIXU9cUzyesDz2PqgdMbKnp8AAL30jEbntNRSWfv-yIKPsJNAQADAgADcwADNAQ
    inline_keyboard =callback.message.reply_markup
    if callback.data== "Accept":
        print(callback.message.photo[0].file_size)
        if callback.message.photo[0].file_size==1320:
            product="burger"
        else:
            product="hotDog"
        count=callback.message.reply_markup.inline_keyboard[0][0].callback_data.split()[1]
        print(product,count)
        m_sqlite.set_value(columns=(product,"ok"),values=(count,count),name_table=callback.message.chat.username)
        m_sqlite.data.commit()
        inline_keyboard.inline_keyboard[0][0].text="Buy"
        inline_keyboard.inline_keyboard[0][0].callback_data="Buy 0"
        del inline_keyboard.inline_keyboard[1]
        await callback.message.edit_reply_markup(reply_markup=inline_keyboard,inline_message_id=callback.inline_message_id)
    if 'Buy' in callback.data:
        count = '1'
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
            count1 = callback.message.reply_markup.inline_keyboard[0][0].callback_data.split(' ')
            print(count)
            if int(count1[-1])>0:
                count = str(int(count1[-1])-1)

            print(type(count))
            
        print('0'==count)
        print(type(inline_keyboard))
        print()
        inline_keyboard.inline_keyboard[0][0].callback_data = f'Buy {count}'
        inline_keyboard.inline_keyboard[0][0].text = f'Buy {count}'
        
        try:
            await callback.message.edit_reply_markup(reply_markup=inline_keyboard,inline_message_id=callback.inline_message_id)
        except:
            print("Telegeram error")
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