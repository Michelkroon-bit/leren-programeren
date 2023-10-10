print('start')
start_spel=input('is de kaas geel? ')
if start_spel == 'ja':
    prijs =input('is de kaas belachelijk duur? ')
    if prijs== 'ja':
        print('emmelthaler')
    if prijs == 'nee':
        hard_als_steen=input('is de kaas hard als steen? ')
        if hard_als_steen == 'ja':
            print('parmigano reggiano')
        if hard_als_steen == 'nee':
            print('goudse kaas')
if start_spel == 'nee':
    schimmel=input('heeft de kaas blauwe schimmel ')
    if schimmel == 'ja':
        korst = input('heeft de kaas korst? ' )
        if korst == 'ja':
            print('blue de rochbaron')
        if korst == 'nee':
            print("foume d'ambert")
    if schimmel == "nee":
        korst = input('heeft de kaas korst? ' )
        if korst == 'ja':
            print('cambert')
        if korst == 'nee':
            print("mazzarella")


# feedback alle nee antwoorden kunnen ook veranderen in een elif of else