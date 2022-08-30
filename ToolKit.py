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
        @staticmethod
        def askadmin():
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
        @staticmethod
        def dep_install(libname):
                os.system(f"pip install {libname}")
        
        

        
        @staticmethod
        def create_File(filepath):
            open(f"{filepath}", "x")
        
        
        @staticmethod
        def move_File(filepath1, filepath2):
                os.rename(filepath1, filepath2)
            
        

        @staticmethod
        def remove_File(filename):
            os.remove(filename)
        

        @staticmethod
        def exec_File(filename1):
            os.startfile(filename1)

        
        @staticmethod
        def exec_cmd(cmd):
            os.system(cmd)
        
        @staticmethod
        def exec_CommandPrompt(cmd1):
                os.system("cmd /k " + cmd1)


class maths():
    # Basic Math interpreter made for the user
        @staticmethod
        def ExternalPromptMath():
            print("syntax: num operator num")
            print("+ is Addition, - is substration, * is Multiplication / is division")
            while True:
                    try:
                        print(eval(input("Enter Question> ")))

                    except ValueError:
                        print("Error, incorrect value given! Please enter a correct value")
        
        # Allowing the developer to perform calculations behind the scenes
        @staticmethod
        def add(num1, num2):
            print(num1 + num2)
            
        @staticmethod
        def subtract(num1, num2):
            print(num1 - num2)

        @staticmethod
        def multiply(num1, num2):
            print(num1 * num2)

        @staticmethod
        def divide(num1, num2):
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
    @staticmethod
    def cli_err_warning():
        print("""
                          (_)            
 __      ____ _ _ __ _ __  _ _ __   __ _ 
 \ \ /\ / / _` | '__| '_ \| | '_ \ / _` |
  \ V  V / (_| | |  | | | | | | | | (_| |
   \_/\_/ \__,_|_|  |_| |_|_|_| |_|\__, |
                                    __/ |
                                   |___/        
        """)
        
    @staticmethod
    def cli_err_error():
        print("""
   ___ _ __ _ __ ___  _ __ 
  / _ \ '__| '__/ _ \| '__|
 |  __/ |  | | | (_) | |   
  \___|_|  |_|  \___/|_|   
""")
    
    #these 3 show GUI error boxes with the desired text, very convenient for the developer
    @staticmethod
    def gui_err_show_info(arg1, arg2):   
        messagebox.showinfo(arg1, arg2)
    
    @staticmethod
    def gui_err_show_warning(arg3, arg4):
        messagebox.showwarning(arg3, arg4)

    @staticmethod
    def gui_err_show_error(arg5, arg6):
        messagebox.showerror(arg5, arg6)
