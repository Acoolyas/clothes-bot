import openpyxl
def bonus_check(message):
    user_id = message.from_user.id
    wb1 = openpyxl.open("/root/bot/goods.xlsx")
    wb = wb1['bonus']
    sheet = wb
    bonus_len = wb.max_row
    for row in range(2, bonus_len+1):
        if str(wb[row][0].value) == str(user_id):
            return f'У вас {str(wb[row][1].value)} бонусов'
    wb[0][wb.max_row+2].value = '0'
    return f'У вас 0 бонусов'