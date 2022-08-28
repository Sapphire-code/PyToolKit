#|#############################################################################|#
#|                         <COPYRIGHT> <SapphireKR> <2022>                     |#
#|=============================================================================|#
#|                 THIS IS FULLY OWNED AND WRITTEN BY SapphireKR               |#
#|       I don't want to disclose my name so I go as "Sapphire" online         |#
#|=============================================================================|#                                                  
#|=============================================================================|#
#|        this is a python toolkit was made with multipurpose apps in mind     |#
#|          this toolkit just makes some stuff easier for the developer        |#
#|              Please read info.txt to learn all the features you get.        |#
#|                                   GOODLUCK!                                 |#
#|#############################################################################|#

# Importing required libraries
from importlib.resources import path
import os
import sys
import platform
import time
from time import strftime
import subprocess
import ctypes
from tkinter import * 
from tkinter import messagebox
#Hiding tkinter root window.
root = Tk()
root.geometry("1x1")
w = Label(root, text ='empty', font = "50")
root.withdraw()
w.pack()
systeminformation = platform.uname()

ask_for_admin = 'asadmin'

# this class allows the developer to do things like ask for privilages, access the file system, execute files and more
class System():
        # This asks the user for admin privalages
        def askadmin(self):
                try:
                    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                
                except:
                    print("Error, Permission Denied.")





        # waits for developer to call variables, then provides the details to the developer
        #When called the variables run a functions by using the platform library, which then fetches the values and stores them in the variable.
        os = systeminformation.system
        computer_name = systeminformation.node
        os_version = systeminformation.release
        os_build = systeminformation.version
        cpu_architechture = systeminformation.machine
        processor = systeminformation.processor

        
        
        # this can be used so if your program has dependencies you can easily use this funtion to install required libraries for your program!
        # Always make sure you have the users permission to install the dependencies/libraries
        # also make sure the libraries you are using are safe to use
        def dep_install(self, libname):
                os.system(f"pip install {libname}")
        
        

        
        def create_File(self, filepath):
            open(f"{filepath}", "x")
        
        
        def move_File(self, filepath1, filepath2):
                os.rename(filepath1, filepath2)
            
        

        def remove_File(self, filename):
            os.remove(filename)
        

        def exec_File(self, filename1):
            os.startfile(filename1)

        
        def exec_cmd(self, cmd):
            os.system(cmd)
        
        def exec_CommandPrompt(self, cmd1):
                os.system("cmd /k " + cmd1)


class maths():
    # Basic Math interpreter made for the user
        def ExternalPromptMath(self):
            print("syntax: num operator num")
            print("+ is Addition, - is substration, * is Multiplication / is division")
            while True:
                    try:
                        print(eval(input(">>>")))

                    except ValueError:
                        print("Error, incorrect value given! Please enter a correct value")
        
        # Allowing the developer to perform calculations behind the scenes
        def add(self, num1, num2):
            print(num1 + num2)
            
        def subtract(self, num1, num2):
            print(num1 - num2)

        def multiply(self, num1, num2):
            print(num1 * num2)

        def divide(self, num1, num2):
            print(num1 / num2)
#This class is currently useless and isn't properly capable yet. functions are broken/don't work properly.
# to use this class uncomment the lines below to use it. be warned however that they might not work as you expect.
#class network():
#    def start_netsh(self):
#        try:
#            os.startfile("C:\\Windows\\System32\\netsh.exe")
#       except FileNotFoundError:
#            print("Error, netsh.exe was not found")
#            input("Press Enter To Exit...")
#            exit()
    

# using netsh to get wifi passwords on the system
#    def explorenet_PromptCli(self):
#        os.system("cls")
#        os.system("netsh wlan show profiles")
#        wifi = input("Which Wifi's password do you want?: ")
#        os.system('netsh wlan show profiles name="' + wifi + '" key=clear')
#        input("Press Enter To Exit...")
    
#    def downloadnet(self, folderPath):
#        print("this function requires admin privilages please make sure you have admin")
#        os.system(f"netsh wlan export profile folder={folderPath} key=clear")



class errors():
    def cli_err(self):
        print("""'
'##:::::'##::::'###::::'########::'##::: ##:'####:'##::: ##::'######:::
##:'##: ##:::'## ##::: ##.... ##: ###:: ##:. ##:: ###:: ##:'##... ##::
##: ##: ##::'##:. ##:: ##:::: ##: ####: ##:: ##:: ####: ##: ##:::..:::
##: ##: ##:'##:::. ##: ########:: ## ## ##:: ##:: ## ## ##: ##::'####:
##: ##: ##: #########: ##.. ##::: ##. ####:: ##:: ##. ####: ##::: ##::
##: ##: ##: ##.... ##: ##::. ##:: ##:. ###:: ##:: ##:. ###: ##::: ##::
. ###. ###:: ##:::: ##: ##:::. ##: ##::. ##:'####: ##::. ##:. ######:::
:...::...:::..:::::..::..:::::..::..::::..::....::..::::..:::......::::       
        """)
    
    #these 3 show GUI error boxes with the desired text, very convenient for the developer
    def gui_err_showinfo(self, arg1, arg2):   
        messagebox.showinfo(arg1, arg2)
    
    def gui_err_showwarning(self, arg3, arg4):
        messagebox.showwarning(arg3, arg4)

    def gui_err_showerror(self, arg5, arg6):
        messagebox.showerror(arg5, arg6)
