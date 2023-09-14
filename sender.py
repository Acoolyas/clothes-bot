import openpyxl
import warnings
from aiogram.types.input_media_photo import InputMediaPhoto
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from aiogram.types import FSInputFile
from aiogram.methods import SendPhoto
async def Sender(category, category2, size, msg, ):
    warnings.simplefilter(action='ignore', category=UserWarning)

    wb1 = openpyxl.open("/root/bot/goods.xlsx")
    if category == 'clothes':
        wb = wb1['clothes']
        global good_name, sizes
        #выбираем активный лист
        sheet = wb
        # -  - - - - -- - - - - vocablary - - -- - - - - - - -- - 
        if size == 'XS':
            size_value = 2
        elif size == 'S':
            size_value = 3
        elif size == 'M':
            size_value = 4
        elif size == 'L':
            size_value = 5
        elif size == 'XL':
            size_value = 6
        elif size == '2XL':
            size_value = 7
        # - - - -- - - - -- - - - -- - - -- - - - - -  - - - -- - -- 
        sold_out = 0
        for row in range(3,100):
            good_category = str(sheet[row][1].value)
            sizes = ''
            if good_category == category2:
                if size == 'allsizes':
                    url1 = str(sheet[row][9].value)
                    good_name = str(sheet[row][0].value)
                    if good_name != 'None':
                        sold_out += 1
                    f = open(f'/root/bot/goods/{good_name}/description.txt', 'r')
                    caption_final = f.read().rstrip()
                    f.close()
                    good_price = sheet[row][8].value
                    for i in range(2,8):
                        if str(sheet[row][i].value) == '1':
                            sold_out += 1
                            sizes += str(sheet[2][i].value) + ', '           
                    caption_final = caption_final + '\n\n' + 'Размеры: ' + sizes[:(len(str(sizes))-2)] + '\n' + 'Цена: ' + str(good_price)
                    builder = InlineKeyboardBuilder()
                    builder.add(InlineKeyboardButton(
                        text="Больше фото", url=url1)
                    )
                    builder.add(InlineKeyboardButton(
                        text="Заказать", url='https://t.me/callmehustle')
                    )
                    if sold_out != 0:
                        await msg.answer_photo(photo=FSInputFile(f'/root/bot/goods/{good_name}/1.jpg'), caption = caption_final, reply_markup = builder.as_markup())
                elif size == 'XL/2XL': 
                    if str(sheet[row][6].value) == '1' or str(sheet[row][7].value) == '1':
                        sold_out+=1
                        url1 = str(sheet[row][9].value)
                        good_name = str(sheet[row][0].value)
                        # description opening ----
                        f = open(f'/root/bot/goods/{good_name}/description.txt', 'r')
                        caption_final = f.read().rstrip()
                        f.close()
                            # - - - - -- - - -- - - - -- 
                        good_price = sheet[row][8].value
                        for i in range(2,8):
                            if str(sheet[row][i].value) == '1':
                                sizes += str(sheet[2][i].value) + ', '           
                        caption_final = caption_final + '\n\n' + 'Размеры: ' + sizes[:(len(str(sizes))-2)] + '\n' + 'Цена: ' + str(good_price)
                        builder = InlineKeyboardBuilder()
                        builder.add(InlineKeyboardButton(
                            text="Больше фото", url=url1)
                        )
                        builder.add(InlineKeyboardButton(
                            text="Заказать", url='https://t.me/callmehustle')
                        )
                        if sold_out !=0:
                            await msg.answer_photo(photo=FSInputFile(f'/root/bot/goods/{good_name}/1.jpg'), caption = caption_final, reply_markup = builder.as_markup())
                elif str(sheet[row][size_value].value) == '1':
                    sold_out
                    url1 = str(sheet[row][9].value)
                    good_name = str(sheet[row][0].value)
                    # description opening ----
                    f = open(f'/root/bot/goods/{good_name}/description.txt', 'r')
                    caption_final = f.read().rstrip()
                    f.close()
                        # - - - - -- - - -- - - - -- 
                    good_price = sheet[row][8].value
                    for i in range(2,8):
                        if str(sheet[row][i].value) == '1':
                            sold_out += 1
                            sizes += str(sheet[2][i].value) + ', '           
                    caption_final = caption_final + '\n\n' + 'Размеры: ' + sizes[:(len(str(sizes))-2)] + '\n' + 'Цена: ' + str(good_price)
                        #media_list.append(InputMediaPhoto(type = 'photo', media = FSInputFile(f'./goods/{good_name}/1.jpg'), caption = caption_final))
                        #media_list.append(InputMediaPhoto(type = 'photo', media = FSInputFile(f'./goods/{good_name}/2.jpg')))
                        
                    builder = InlineKeyboardBuilder()
                    builder.add(InlineKeyboardButton(
                        text="Больше фото", url=url1)
                    )
                    builder.add(InlineKeyboardButton(
                        text="Заказать", url='https://t.me/callmehustle')
                    )
                    if sold_out !=0:
                        await msg.answer_photo(photo=FSInputFile(f'/root/bot/goods/{good_name}/1.jpg'), caption = caption_final, reply_markup = builder.as_markup())
        if sold_out == 0:
            await msg.answer('Товаров по запросу нет в наличии.\nДля заказа обращаться к @callmehustle')
        wb = ''
    if category == 'accs':
        sold_out = 0
        wb = wb1['accs']      
        sheet = wb
        for row in range(3,100):
            good_name = str(sheet[row][0].value)
            url1 = str(sheet[row][3].value)
            if good_name != 'None':
                sold_out +=1 
            else:
                return
            sizes = sheet[row][1].value
                        # description opening ----
            f = open(f'/root/bot/goods/{good_name}/description.txt', 'r')
            caption_final = f.read().rstrip()
            f.close()
                        # - - - - -- - - -- - - - -- 
            if sizes == None:
                pass
            else:
                caption_final = caption_final + '\n' + 'Размеры: ' + str(sizes)
                good_price = sheet[row][2].value        
                caption_final = caption_final + '\n' + 'Цена: ' + str(good_price)
                builder = InlineKeyboardBuilder()
                builder.add(InlineKeyboardButton(
                    text="Больше фото", url=url1)
                )
                builder.add(InlineKeyboardButton(
                    text="Заказать", url='https://t.me/callmehustle')
                )
            await msg.answer_photo(photo=FSInputFile(f'/root/bot/goods/{good_name}/1.jpg'), caption = caption_final, reply_markup = builder.as_markup())
        if sold_out == 0:
            await msg.answer('Товаров по запросу нет в наличии.\nДля заказа обращаться к @callmehustle')
    if category == 'shoes':
        sold_out = 0
        wb = wb1['shoes']      
        sheet = wb
        for row in range(3,100):
            url1 = str(sheet[row][3].value)
            good_name = str(sheet[row][0].value)
            if good_name == 'None':
                return
            else:
                sold_out += 1
                sizes = sheet[row][1].value
                        # description opening ----
                f = open(f'/root/bot/goods/{good_name}/description.txt', 'r')
                caption_final = f.read().rstrip()
                f.close()
                            # - - - - -- - - -- - - - -- 
                if sizes == None:
                    pass
                else:
                    caption_final = caption_final + '\n' + 'Размеры: ' + str(sizes)
                    good_price = sheet[row][2].value        
                    caption_final = caption_final + '\n' + 'Цена: ' + str(good_price)
                    builder = InlineKeyboardBuilder()
                    builder.add(InlineKeyboardButton(
                        text="Больше фото", url=url1)
                    )
                    builder.add(InlineKeyboardButton(
                        text="Заказать", url='https://t.me/callmehustle')
                    )
                    
                await msg.answer_photo(photo=FSInputFile(f'/root/bot/goods/{good_name}/1.jpg'), caption = caption_final, reply_markup = builder.as_markup())
        if sold_out == 0:
            await msg.answer('Товаров по запросу нет в наличии.\nДля заказа обращаться к @callmehustle')
    if category == 'inprocess':
        sold_out = 0
        wb = wb1['inprocess']      
        sheet = wb
        for row in range(3,100):
            url1 = str(sheet[row][3].value)
            good_name = str(sheet[row][0].value)
            if good_name == 'None':
                pass
            else:
                sizes = sheet[row][1].value
                            # description opening ----
                f = open(f'/root/bot/goods_inprocess/{good_name}/description.txt', 'r')
                caption_final = f.read().rstrip()
                f.close()
                            # - - - - -- - - -- - - - -- 
                if sizes == None:
                    pass
                else:
                    caption_final = caption_final + '\n' + 'Размеры: ' + str(sizes)
                    good_price = sheet[row][2].value        
                    builder = InlineKeyboardBuilder()
                    builder.add(InlineKeyboardButton(
                        text="Внести предоплату", url='https://t.me/callmehustle')
                    )
            await msg.answer_photo(photo=FSInputFile(f'/root/bot/goods_inprocess/{good_name}/1.jpg'), caption = caption_final, reply_markup = builder.as_markup())