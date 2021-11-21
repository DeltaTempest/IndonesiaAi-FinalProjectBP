import smtplib
import getpass

def menambahkanEmailBaru():
    gmailPenerima = str(input("Silahkan masukan email penerima:"))
    with open("receiver.txt", "r") as file:
        emailPenerima = file.read();
        emailPenerimaList = emailPenerima.split("\n")
    
    for email in emailPenerimaList:
        if email == gmailPenerima:
            print("Email telah ada, silahkan masukan email yang lain!")
            return False
        elif email != gmailPenerima:
            with open("receiver.txt", "a") as file:
                file.write(gmailPenerima + "\n")
                print("Email telah ditambahkan")
                break

def mencariEmail(email):
    print("Mencari email...")
    with open("receiver.txt", "r") as file:
        emailPenerima = file.read()
        listEmailPenerima = emailPenerima.split("\n")
    for emails in listEmailPenerima:
        if emails == email:
            
            return emails
        
        elif emails != email:
            continue
    return False
  
def mengirimEmail(emailPengirim, password, emailPenerima):
    emailTeks = str(input("Silahkan masukan pesan: "))
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo
        server.login(emailPengirim, password)
        print("Login berhasil!")
        server.sendmail(emailPengirim, emailPenerima, emailTeks)
        server.close
        
        print('Email terkirim!')
    except Exception as e:
        print("Error: " + e)

def showEmailList():
    with open('receiver.txt', 'r') as file:
        email = file.read()
        emailList = email.split("\n")
    i = 0
    print("List Email tujuan pada receiver.txt")
    for email in emailList:
        if email == "":
            continue
        i+=1
        print(i ,". " + email)
    
    print("")

gmailUser = str(input("Silahkan masukan email anda:"))
gmailPassword = getpass.getpass("Masukan password email: ")



print("Selamat datang di program pengirim email!")
while True:
    
    randInt = int(input("Apakah anda ingin lakukan?\n\t1. Menambahkan email baru\n\t2. Mengirim Email\n\t3. Melihat list email\n\t4. Keluar\n"))

    if randInt == 1:
        #MENAMBAHKAN EMAIL KE receiver.txt
        while True:
            if menambahkanEmailBaru() == False:
                continue
            else:
                break    
        continue
    elif randInt == 2:
        #MENCARI EMAIL DI receiver.txt
        #Cek apakah receiver.txt ada isinya atau tidak
        with open('receiver.txt', 'r') as listReceiver:
            receipentEmail = listReceiver.read()
            penerima = receipentEmail.split("\n")
        
        if len(penerima) == 1:
            print("receiver.txt kosong! Silahkan masukan email penerima baru!")
            menambahkanEmailBaru()
        #receiver.txt ADA ISINYA DAN MENCARI EMAIL DENGAN METHOD mencariEmail
        elif len(penerima) > 1:
            showEmailList()
            while True:
                emailDicari = str(input("Silahkan masukan email tujuan anda: "))
                emailPenerima = mencariEmail(emailDicari)
                
                if emailPenerima == "":
                    print("Tolong Masukan email yang benar!")
                    continue
                if emailPenerima == False:
                    print("Email tidak ditemukan!, Harap masukan email tujuan bukan angka")
                    continue
                else:
                    print("Email ketemu!")
                    mengirimEmail(gmailUser, gmailPassword, emailPenerima)
                    break
            continue
            
                      
    elif randInt == 3:
        showEmailList()
    
    elif randInt == 4:
        break
    else:
        print("Mohon masukan angka yang sesuai")

print("Program Selesai, terimakasih")
    









 
   
