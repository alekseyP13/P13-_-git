def get_vat(payment, persent=20):
    try:
     vat = payment / 100 * persent
     vat = round(vat, 2)
     return "Sum VAt: {}". format(vat)
    except TypeError:
     return "can`t count.check data!" 


result = get_vat(4500, 15)
print (result)