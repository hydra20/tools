import os,sys,time

def jalan(z):
    for e in z +'\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.001)


os.system('clear')
time.sleep(0.1)
print "\033[1;35m"
os.system('figlet Install Tools Hydra NET')
jalan("\033[1;33m="* 53)
time.sleep(1)
print "\033[1;31mAuthor   :"  "\033[1;32mHydra NET"
print "\033[1;31mYoutube  :"  "\033[1;32mHydra NET "
print "\033[1;31mGithub   :" "\033[1;32mhydra20"
print "\033[1;31mInstagram:""\033[1;32mhydranet2020"
jalan ("\033[1;33m="* 53)
time.sleep(1)



print "\033[1;32m[0] " "\033[1;32mUpadte "   " " "\033[1;31mTermux Important  "
time.sleep(0.2)
print "\033[1;32m[1] " "\033[1;32mInstall" " "   "\033[1;31mNgrok "
time.sleep(0.2)
print "\033[1;32m[2] " "\033[1;32mInstall" " "   "\033[1;31mHack Cam Front"
time.sleep(0.2)
print "\033[1;32m[3] " "\033[1;32mInstall" " "   "\033[1;31mtool for encrypt your script"
time.sleep(0.2)
print "\033[1;32m[4] " "\033[1;32mInstall" " "   "\033[1;31mall Pkg Tremux"
time.sleep(0.2)
print "\033[1;32m[5] " "\033[1;32mInstall" " "   "\033[1;31mMetasploirt Automatically "
time.sleep(0.2)
print "\033[1;32m[6] " "\033[1;32m"Update "      "\033[1;31mmy tool"
time.sleep(0.2)
print "\033[1;32m[7] " "\033[1;32mMy Channel In  \033[1;31mYoutube "
time.sleep(0.2)
print "\033[1;32m[8] " "\033[1;32mMy account In \033[1;31mInstagram "
time.sleep(0.2)
print "\033[1;32m[x]\033[1;31m Exit" 
time.sleep (0.2)
choose = raw_input('\033[1;33m[?] choose : ')

if choose == "0":
    os.system('apt update && upgrade -y')
    os.system('apt install python -y')
    os.system('apt install python2 -y')
    os.system('apt install git -y')
    os.system('pip2 install requests mechanize')
    jalan('\033[1;31mThe update was successful')
    time.sleep (1)
    os.system ('python2 tools.py')


elif choose  == "1":
    os.system('git clone https://github.com/hydra20/ngrok')
    os.system('cd ngrok ; mv ngrok $HOME ; cd ..   ') 
    os.system('rm -rf ngrok')
    os.system ('cd $HOME ; chmod +x * ')
    print ('\033[1;31mThe tool was loaded successfully')
    print ('\033[1;37mNow register login in ngrok  website  using Google account and copy your token and paste on the course of the tool at home only') 
    time.sleep (5)
    os.system ('xdg-open https://dashboard.ngrok.com/login') 
    print "\033[1;37m"
    

elif choose == "2":
    os.system('git clone https://github.com/hydra20/cam')
    jalan ('\033[1;31mCloned successfully')
    print "\033[1;37m"
    time.sleep (1)
    os.system ('python2 tools.py')

elif choose == "3":
    os.system('git clone https://github.com/hydra20/encrypt')
    jalan ('\033[1;31mCloned successfully')
    print "\033[1;37m"
    time.sleep (1)
    os.system ('python2 tools.py')

elif choose == "4":
    os.system('git clone https://github.com/hydra20/pkg')
    jalan ('\033[1;31mCloned successfully')
    print "\033[1;37m"
    time.sleep (1)
    os.system ('python2 tools.py')

elif choose == "5":
    os.system('git clone https://github.com/hydra20/meta')
    jalan ('\033[1;31mCloned successfully')
    print "\033[1;37m"
    time.sleep (1)
    os.system ('python2 tools.py')

elif choose == "6":
	os.system('git pull origin master')
	print ("\033[1;32mSuccessfully updated")
	time.sleep (2)
	os.system ('python2 tools.py')
	
elif choose == "7":
    os.system('xdg-open https://www.youtube.com/c/hydranet2')
    os.system ('python2 tools.py')
	
	
elif choose == "8":
    os.system('xdg-open https://www.instagram.com/hydranet2020')
    os.system ('python2 tools.py')
    
elif choose == "x":
	os.system ('exit') 



