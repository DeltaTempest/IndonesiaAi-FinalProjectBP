import smtplib
import getpass

def menulisEmailBaru():
    gmailPenerima  = str(input("Silahkan masukan email penerima:"))
    with open("receiver.txt", "r") as file:
        emailPenerima = file.read();
        emailPenerimaList = emailPenerima.split("\n")
    
    for email in emailPenerimaList:
        if email == gmailPenerima:
            print("Email telah ada, silahkan masukan email yang lain!")
            menulisEmailBaru()
        elif email != gmailPenerima:
            with open("receiver.txt", "a") as file:
                file.write(gmailPenerima, "\n")
    


print("Selamat datang di program pengirim email!")

gmailUser = str(input("Silahkan masukan email anda:"))
gmailPassword = str(input("Masukan password anda:"))


while True:
    randStr = str(input("Apakah anda ingin menambahkan email baru [y/n]\n"))

    if randStr == "y":
        print(randStr)
    elif randStr == "n":
        with open('receiver.txt', 'r') as listReceiver:
            receipentEmail = listReceiver.read()
            penerima = receipentEmail.split("\n")
        
        if len(penerima) == 0:
            print("receiver.txt kosong! Silahkan masukan email penerima baru!")
            
    else:
        print("Tolong masukan argumen yang tepat!")



    

    









 
   
