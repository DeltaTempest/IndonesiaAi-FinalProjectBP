import smtplib
import getpass

def menambahkanEmailBaru():
    gmailPenerima  = str(input("Silahkan masukan email penerima:"))
    with open("receiver.txt", "r") as file:
        emailPenerima = file.read();
        emailPenerimaList = emailPenerima.split("\n")
    
    for email in emailPenerimaList:
        if email == gmailPenerima:
            print("Email telah ada, silahkan masukan email yang lain!")
            menambahkanEmailBaru()
        elif email != gmailPenerima:
            with open("receiver.txt", "a") as file:
                file.write(gmailPenerima + "\n")

def mencariEmail(email):
    print("Mencari email...")
    with open("receiver.txt", "r") as file:
        emailPenerima = file.read()
        listEmailPenerima = emailPenerima.split("\n")
    for emails in listEmailPenerima:
        if emails == email:
            print("Email ketemu!")
            return emails
        
        elif emails != email:
            continue
    print("Tidak menemukan email yang anda cari!")
  
def mengirimEmail(emailPengirim, password, emailPenerima):
    emailTeks = str(input("Silahkan masukan pesan: "))
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo
        server.login(emailPengirim, password)
        print("Login berhasil!")
        server.sendmail(emailPengirim, emailPenerima, emailTeks)
        server.close
        
        print('email sent')
    except Exception as e:
        print("Error: " + e)

gmailUser = str(input("Silahkan masukan email anda:"))
gmailPassword = str(input("Masukan password anda:"))

print("Selamat datang di program pengirim email!")
while True:
    
    randInt = int(input("Apakah anda ingin lakukan?\n\t1. Menambahkan email baru\n\t2. Mencari email pada emailList\n\t3. Keluar\n"))

    if randInt == 1:
        #MENAMBAHKAN EMAIL KE receiver.txt
        menambahkanEmailBaru()
        break
    elif randInt == 2:
        #MENCARI EMAIL DI receiver.txt
        #Cek apakah receiver.txt ada isinya atau tidak
        with open('receiver.txt', 'r') as listReceiver:
            receipentEmail = listReceiver.read()
            penerima = receipentEmail.split("\n")
        if len(penerima) == 0:
            print("receiver.txt kosong! Silahkan masukan email penerima baru!")
            menambahkanEmailBaru()
        #receiver.txt ADA ISINYA DAN MENCARI EMAIL DENGAN METHOD mencariEmail
        elif len(penerima) > 0:
            emailDicari = str(input("Silahkan masukan email yang ingin anda cari: "))
            emailPenerima = mencariEmail(emailDicari)
            mengirimEmail(gmailUser, gmailPassword, emailPenerima)
            break            
    elif randInt == 3:
        break;
    
    else:
        print("Masukan argumen yang tepat!")

print("Program Selesai, terimakasih")
    









 
   
