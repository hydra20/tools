import os,sys,time

def jalan(z):
    for e in z +'\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.001)


os.system('clear')
time.sleep(1)
print "\033[1;35m"
os.system('figlet Install Tools Hydra NET')
jalan("\033[1;30m="* 59)
time.sleep(1)
print "\033[1;31mAuthor   :"  "\033[1;32mHydra NET"
print "\033[1;31mYoutube  :"  "\033[1;32mHydra NET "
print "\033[1;31mGithub   :" "\033[1;32mhydra20"
print "\033[1;31mInstagram:""\033[1;32mhydranet2020"
jalan ("\033[1;30m="* 59)
time.sleep(1)

def list():
    print "\033[1;32m[0] " "\033[1;32mUpadte "   " " "\033[1;31mTermux Important  "
    time.sleep(1)
    print "\033[1;32m[1] " "\033[1;32mInstall" " "   "\033[1;31mNgrok "
    time.sleep(1)
    print "\033[1;32m[2] " "\033[1;32mInstall" " "   "\033[1;31mHack Cam Front"
    time.sleep(1)
    print "\033[1;32m[3] " "\033[1;32mInstall" " "   "\033[1;31mtool for encrypt your script"
    time.sleep(1)
    print "\033[1;32m[4] " "\033[1;32mInstall" " "   "\033[1;31mall Pkg Tremux"
    time.sleep(1)
    print "\033[1;32m[5] " "\033[1;32mInstall" " "   "\033[1;31mMetasploirt Automatically "
    time.sleep(1)
    print "\033[1;32m[6] " "\033[1;31mMy Youtube "
    time.sleep(1)
    print "\033[1;32m[7] " "\033[1;31mMy Instagram "
    time.sleep(1)
    list()

choose = raw_input('\033[1;33m[?] choose : ')

if choose == "0":
    os.system('apt update && upgrade -y')
    os.system('apt install python -y')
    os.system('apt install python2 -y')
    os.system('apt install git -y')
    os.system('pip2 install requests mechanize')
    jalan('\033[1;31mThe update was successful')
    list()

elif choose  == "1":
    os.system('git clone https://github.com/hydra20/Ngrok')
    os.system('chmod +x *')
    jalan ('\033[1;31mThe tool was loaded successfully')
    print "\033[1;37m"
    list()

elif choose == "2":
    os.system('git clone https://github.com/hydra20/cam')
    jalan ('\033[1;31mCloned successfully')
    list()

elif choose == "3":
    os.system('git clone https://github.com/hydra20/encrypt')
    jalan ('\033[1;31mCloned successfully')
    print "\033[1;37m"
    list()

elif choose == "4":
    os.system('git clone https://github.com/hydra20/pkg')
    jalan ('\033[1;31mCloned successfully')
    print "\033[1;37m"
    list()

elif choose == "5":
    os.system('git clone https://github.com/hydra20/meta')
    jalan ('\033[1;31mCloned successfully')
    print "\033[1;37m"
    list()

elif choose == "6":
    os.system('xdg-open https://www.youtube.com/c/hydranet2')

elif choose == "7":
    os.system('xdg-open https://www.instagram.com/hydranet2020')



