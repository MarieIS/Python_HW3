vcard_count = int(input('Введите количество видеокарт: '))

if vcard_count > 0:
   vcard_list = []

   for i in range(0, vcard_count):
      vcard_list.append(int(input('Введите информацию о видеокарте в числовой форме: ')))
      if i == 0:
         max_num = vcard_list[0]
      elif vcard_list[i] > max_num:
         max_num = vcard_list[i]
   
   vcard_list_upd = []

   for i in range(0, vcard_count):
      if vcard_list[i] < max_num:
        vcard_list_upd.append(vcard_list[i])

   print(vcard_list_upd)
else:
   print('Введите число, большее нуля')