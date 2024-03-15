PI = 3.14
r_vagy_d = input('Kérem adja meg hogy átmérőt vagy sugarat akar megadni (r/d): ')
if r_vagy_d == 'd':
    #atmero = float(input('Kérem adja meg az átmérőt  '))
    sugar  = (float(input('Kérem adja meg a sugarat  ')) / 2)
else:
    sugar  = float(input('Kérem adja meg a sugarat  ')) 
    terulet = round(PI * sugar ** 2, 2)
kerulet = round(2 * PI * sugar, 2)
print(f'A kör területe: {terulet} \n A kör kerülete {kerulet}')



 

