# coding=utf-8
# Created by sCuby07
# My Team: Cyber Ghost Indonesia
# Ngoding Sendiri Lah Kntl Jangan Recode!
# Yang Recode Semoga Lu Bisa Ngoding Sendiri:)
# ----------------------------------------------------
import os,sys,time,json
from bs4 import BeautifulSoup as parse
from base64 import *
import requests as r
# ------------------------ WARNA ---------------------
G = '\x1b[0;32m'
GL = '\x1b[32;1m'
B = '\x1b[0;36m'
P = '\x1b[35;1m'
BL = '\x1b[36;1m'
BD = '\x1b[34;1m'
R = '\x1b[31;1m'
W = '\x1b[37;1m'
H = '\x1b[30;1m'
Y = '\x1b[33;1m'
YL = '\x1b[1;33m'
# ---------------------- SEBUAH TOOLS YANG BERFUNGSI ----------------
# ------------------------ UNTUK MENDOWNLOAD VIDEO --------------------
# -------------------------FACEBOOK DAN INSTAGRAM. ------------------
def runntek(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10.0 / 100)

def instagram():
	url = raw_input('\nURL : ')
	xxx = raw_input('\nDownload? (y/n) ')
	if 'y' in xxx:
		bra = raw_input('Output : ')
		print('{}\n[!] Loading...'.format(R))
		save = r.get(url).text
		soup = parse(save, 'html.parser')
		love = soup.findAll('script', type='text/javascript')
		for heart in love:
			if 'window._sharedData = ' in heart.text:
				pakboi = heart.text.replace('window._sharedData = ','').replace(';','')
		pakboi = json.loads(pakboi)
		pakboi = pakboi["entry_data"]['PostPage'][0]["graphql"]['shortcode_media']["video_url"]
#		print('{}[!] Sedang Mendownload...'.format(R))
		time.sleep(7)
		pakgerl = r.get(pakboi)
		pants = open(bra, 'wb')
		pants.write(pakgerl.content)
		pants.close
		print('{}[!] Download Succes'.format(GL))
		time.sleep(3)
		print('{}\n[!] Copy File to Internal'.format(R))
		time.sleep(3)
		print('{}[!] Succesfully\n\n\n{}CHECK ON INTERNAL!!!'.format(GL,BL))
		time.sleep(2)
		os.system('cp '+bra+' /sdcard && rm -rf '+bra)

def about_program():
	os.system('clear')
	runntek(b64decode('Ck5hbWUgICAgOiAgSW5zdGFGYWNlClZlcnNpb24gOiAgMS4wCkF1dGhvciAgOiAgc0N1YnkwNwpUZWFtICAgIDogIEN5YmVyIEdob3N0IElEClRoYW5rcyAgOiAgQWxsYWggU1dULCBNYXJrIFp1Y2tlcmJlcmcKCkluZm8gICAgOiAgSW5zdGFGYWNlIGlzIHRvb2wgZG93bmxvYWRpbmcKICAgICAgICAgICBJbnN0YWdyYW0gdmlkZW9zIGFuZCBGYWNlYm9vawoKTm90ZSAgICA6ICBwbGVhc2UgZG8gbm90IHNlbGwgYW5kIGJ1eSB0aGlzIHRvb2wuCiAgICAgICAgICAgdGhpcyB0b29sIGlzIDEwMCUgZnJlZS4KICAgICAgICAgICBJZiB5b3UgZmluZCBzb21lb25lIHdobyB0cmFkZXMgdGhpcyB0b29sCiAgICAgICAgICAgcGxlYXNlIHJlcG9ydCB0byBtZS4KCsKpIDIwMjAgc0N1YnkwNywgQ3liZXIgR2hvc3QgSW5kb25lc2lh'))



def facebook():
	url = raw_input('\nURL : ')
        xxx = raw_input('\nDownload? (y/n) ')
        if 'y' in xxx:
		bra = raw_input('Output : ')
		print('{}\n[!] Loading...'.format(R))
	        save = r.get(url).text
#       	print save
        	sop = parse(save, "html.parser")
        	res = sop.find("script", type="application/ld+json")
	        a = json.loads(res.text)
        	b = a['contentUrl']
		time.sleep(7)
	        c = r.get(b)
	        d = open(bra, 'wb')
	        d.write(c.content)
	        d.close
	        print('{}[!] Download Succes'.format(GL))
                time.sleep(3)
                print('{}\n[!] Copy File to Internal'.format(R))
                time.sleep(3)
                print('{}[!] Succesfully\n\n\n{}CHECK ON INTERNAL!!!'.format(GL,BL))
                time.sleep(2)
                os.system('cp '+bra+' /sdcard && rm -rf '+bra)

def contact():
	os.system('xdg-open https://api.whatsapp.com/send?phone=62895611982226 && python2 main.py')


if __name__ == '__main__':
	os.system('clear')  
	print('''{}
  ___           _        _____    
 |_ _|_ __  ___| |_ __ _|  ___|_ _  ___ ___     
  | || '_ \/ __| __/ _` | |_ / _` |/ __/ _ \   
  | || | | \__ \ || (_| |  _| (_| | (_|  __/   
 |___|_| |_|___/\__\__,_|_|  \__,_|\___\___|{} v1.0{}
	       VIDEOS DOWNLOADER
'''.format(BL,YL,P))
	print('''

{}Commands	Information
{}--------	---------{}
igvid		for download instagram video
fbvid		for download facebook video
about		show about this program
contact		for contact admin
update		update this tool
exit		exit this tool'''.format(BL,P,W))

	nanya = raw_input('\n{}>> {}'.format(BL,W))
	if nanya == 'igvid':
		instagram()
	elif nanya == 'fbvid':
		facebook()
	elif nanya == 'about':
		about_program()
	elif 'contact' in nanya:
		contact()
	elif 'update' in nanya:
		print('update not yet available')
		time.sleep(3)
		os.system('python2 main.py')
	elif nanya == 'exit':
		exit('Bye!')
	else:
		print('{} "{}" command not found'.format(R,nanya))
