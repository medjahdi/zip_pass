
import pyzipper

zip_file = input("Enter Your Zip File --> : ")
pass_list = input("Enter Your Password List --> : ")

count = 1

with open(pass_list, rb ) as text:
    for i in text.readlines():
        password = i.strip()
try:
            with pyzipper.AESZipFile(zip_file,  r ) as zf:
                zf.extractall(pwd=password)
 
                data = zf.namelist()[0]
                data_size = zf.getinfo(data).file_size
                print("""*******************\n[+] Password Found! `%s\n `%s\n `%s\n************************"""%
                      (password.decode( utf8 ),data, data_size))
                Break
except:
            number = count
            print("[%s] [-] Password Failed! - %s" % (number,password.decode( utf8 )))
            count+= 1
            pass