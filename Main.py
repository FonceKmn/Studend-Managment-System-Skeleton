from tinydb import TinyDB, Query # import ucun
db = TinyDB('Data.json') # filenin adi yoxdusa yaradir
User = Query() # Querilerin Istifadesi Ucun
import random
import time

#--------------------------------------------Backend------------------------------------------------------------

def yoxlama(i): # Eyni Id yaranmamagi Ucun Yoxlanish
    if db.search(User.Id ==i)!=[]:
        Qebul()
        


def Qebul(): # Telebe qebulu ucun funksiya
    ad = input('Adi daxil edin ')
    soyad = input('Soyadi Daxil edin: ')
    contact = input('Kontakt melumatlarini daxil edin: ')
    steam = input('Hansi kursa qeydiyyat olunur ?: ')
    if ad or soyad or contact or steam =='':
        print('Bosh aana elave olunmushdur diqqetli olun')
        Qebul()
    
    id_rand_6 = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, 6)]) # Random Id yaratmaq ucun
    yoxlama(int(id_rand_6))
    qeydiyyat_tarixi = time.strftime('%c')
    db.insert({'Id': int(id_rand_6),'Ad': ad,'Soyad': soyad,'Kontakt': contact, 'Steam': steam, 'QT': qeydiyyat_tarixi,'Grade1': None, 'Grade2': None,'Grade3': None,'Grade4': None, 'FG': None})

def Goster(): # Data bazadan cagirib ggosterme
    for item in db.all():
        print(item)
    

def Axtar(): # Id- ye gore Telebelerin Axtarishi
    i = int(input('Axtarish ucun Telebenin Id- nomresini qeyd edin: '))
    result = db.search(User.Id ==i)
    print(result)

def Silme(): # Id ye Gore Telebenin bazadan Silinmesi
    i = int(input('Silmek ucun Telebenin Id- nomresini qeyd edin: '))
    print(f'Silinen Telebe: {db.search(User.Id ==i)}')
    db.remove(User.Id ==i)



def Yenile(): # Id-ye gore telebelin melumatlarinin yenilenmesi
    i = int(input('Yenilemek Ucun Telebe Id sini daxil edin: '))
    '''
    print("Ad: ", Students[i].name,end=' ')
    print("Soyad: ", Students[i].surname,end=' ')
    print("Kontakt: ", Students[i].contact,end=' ')
    print("Steam: ",  Students[i].steam,end=' ')
    print("Davamiyet: ", Students[i].gr1,end=' ')
    print("Tapshiriqlar: " , Students[i].gr2,end=' ')
    print("Modul Imtahani: ", Students[i].gr3,end=' ')
    print("Final Imtahan: ", Students[i].gr4,end=' ')
    print('\n')
    
    '''
    print(f'Melumatlari Yenilenecek Telebe: {db.search(User.Id ==i)}')
    print(' 1. Ad \n 2. Soyad \n 3. Kontact \n 4. Kurs \n 5. Davamiyyet \n 6. Tapshiriq \n 7. Modul Imtahani \n 8. Final Imtahan' )
    c = int(input('Yenilemek istediyiniz melumat novunu secin: '))
    match c:
        case 1:
            l = input('Telebenin yeni Adini daxil edin: ')
            db.update({'Ad': l}, User.Id ==i)

        case 2:
            l = input('Telebenin yeni Soyadini daxil edin: ')
            db.update({'Soyad': l}, User.Id ==i)
            
        case 3:
            l = input('Telebenin yeni elaqe novunu qeyd edin: ')
            db.update({'Kontakt': l}, User.Id ==i)

        case 4:
            l = input('Telebenin yeni Kursunu daxil edin: ')
            db.update({'Steam': l}, User.Id ==i)

        case 5:
            l = int(input('Telebenin yeni Davamiyyet qiymetini daxil edin: '))
            db.update({'Grade1': l}, User.Id ==i)
            
        case 6:
            l = int(input('Telebenin yeni Tapshiriq qiymetini daxil edin: '))
            db.update({'Grade2': l}, User.Id ==i)

        case 7:
            l = int(input('Telebenin yeni Modul Imtahani neticesini daxil edin: '))
            db.update({'Grade3': l}, User.Id ==i)
            
        case 8:
            l = int(input('Telebenin yeni Final Imtahan neticesini daxil edin: '))
            db.update({'Grade4': l}, User.Id ==i)



    


        


#----------------------------------------Consol--------------------------------------------------------------

while True:
    print('Student managment System')
    print(' 1. Qebul \n 2. Goster \n 3. Axtar \n 4. Silme \n 5. Yenile \n 6. Cixish' )
    c = int(input('Icra olunmaq ucun uygun emelliyati secin: '))

    match c:
        case 1:
            print('Qebul secenek secilmishdir')
            Qebul()



        case 2:
            print('Goster secenek secilmishdir')
            Goster()



        case 3:
            print('Axtar secilmishdir')
            Axtar()




        case 4:
            print('Silme secilmishdir')
            Silme()



        case 5:
            print('Yenile secilmishdir')
            Yenile()

        case 6:
            print('Cixish Secilib')
            break


        case _:
            print('Xeta bash verdi')


#------------------------------------------Consol--------------------------------------------------------------
