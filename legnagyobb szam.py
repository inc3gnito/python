elso_szam = int(input('Kerem az elso szamot!'))
masodik_szam = int(input('Kerem a masodik szamot!'))
harmadik_szam = int(input('Kerem a harmadik szamot!'))
print (f'A megadott szamok: {elso_szam}, {masodik_szam}, {harmadik_szam}')
legnagyobb_szam = elso_szam
if     legnagyobb_szam < masodik_szam:
    legnagyobb_szam = masodik_szam
if      legnagyobb_szam < harmadik_szam:
    legnagyobb_szam = harmadik_szam
    print(f"legnagyobb_szam: {legnagyobb_szam}")
    
