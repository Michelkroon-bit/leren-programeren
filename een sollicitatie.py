MIN_GEWICHT= 90
MAX_GEWICHT= 120
MIN_LENGTE=150 
MAX_LENGTE=220
MIN_PRAKTIJKERVATING_MET_DIEREN_DRESUUR=4
MIN_ERVARING_MET_JONGLEREN=5
MIN_PRAKTIJKERVARING_MET_ACROBATIEK=3

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('+      sollicitatie fromulier "circusdirectuer"     +')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('er wordt u een aantal relevante vragen gesteld...')
print('gelieve die naar eer en geweten in te vullen')
print('als blijkt dat u aan de critica voldoet dan komt u \nin aanmerking voor een serieus sollicitatiegesprek')
print('Ontspan maar blijf wakker , hier komen de vragen')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')





naam=input('wat is uw naam? ')
netto_lichaamslengte = int(input('Wat is uw netto lichaamslengte in hele cm, dus exclusief uw kapsel? '))
lichaamsgewicht=int(input('Wat is uw lichaamsgewicht in hele kg? '))
certificaat= input ('heeft u de certificaat "Overleven met gevaarlijk personeel"? J/N ')
praktijkervaring_met_dieren_dressuur=int(input('hoeveel jaar praktijkervaring heeft u met dieren-dressuur ' ))
ervaring_met_jongleren=int(input( 'hoeveel jaar ervaring heeft u met met jongleren ' ))
praktijkervaring_met_acrobatiek=int(input('hoeveel jaar praktijkervaring heeft u met acrobatiek ' ))
fysieke_sport=int(input('Hoeveel uur (afgerond) per week beoefent u een fysieke sport '))
opruimerig=int(input('Hoe opruimerig schat u uzelf op schaal van 1 (niet) tot 5 (obsessief)? ' ))
vliegbevet=input('Bezit u een vliegbevet? J/N ')
is_de_aarde_plat=input('Is volgens u de aarde plat? ')
ruimte_nodig=int(input('Hoeveel ruimte heeft u nodig om u heen op schaal van 1 (niet) tot 5 (veel)? '))

if naam == '': 
    bool_naam = False
else:
    bool_naam = True

if netto_lichaamslengte >= 150 and netto_lichaamslengte <= 220:
    netto_lichaamslengte=True
else:
    netto_lichaamslengte=False
    
if lichaamsgewicht >= 90 and lichaamsgewicht <= 120:
    lichaamsgewicht=True
else:
    lichaamsgewicht=False
    
if praktijkervaring_met_dieren_dressuur >= 4:
    praktijkervaring_met_dieren_dressuur=True
else:
    praktijkervaring_met_dieren_dressuur=False
    
if ervaring_met_jongleren >=5:
    ervaring_met_jongleren=True
else:
    ervaring_met_jongleren=False
    
if praktijkervaring_met_acrobatiek >=3:
    praktijkervaring_met_acrobatiek=True
else:
    praktijkervaring_met_acrobatiek= False

if certificaat in ["j", "ja" , "JA" , "J", "YES"]:
    certificaat = True
else:
    certificaat = False
    
if vliegbevet in ['j', 'ja', 'J', 'JA' , 'Y',  'YES']:
    vliegbevet=True
else:
    vliegbevet=False

if fysieke_sport >= 1:
    fysieke_sport= True
else:
    fysieke_sport = False

if opruimerig >= 1 and opruimerig  <=5:
    opruimerig = True
else:
    opruimerig = False
    
if is_de_aarde_plat in ["n" , "nee" , "N" , "NEE" , "no" ,"NO"]:
    is_de_aarde_plat = True
else:
    is_de_aarde_plat=False
    
if ruimte_nodig >= 1 and ruimte_nodig <= 5:
    ruimte_nodig=True
else:
    ruimte_nodig=False

if bool_naam and netto_lichaamslengte and lichaamsgewicht and certificaat and praktijkervaring_met_acrobatiek and praktijkervaring_met_dieren_dressuur and ervaring_met_jongleren and fysieke_sport and opruimerig and vliegbevet and is_de_aarde_plat and ruimte_nodig :
    print(f'beste, {naam} \n Proficiat! u komt in aanmerking voor een sollicitatie gesprek, stuur sel uw CV')
else:
    print('u bent niet gecwalificeert voor een gesprek :(')