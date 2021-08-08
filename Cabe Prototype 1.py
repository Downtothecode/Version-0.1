import subprocess
import platform
import socket
import time
import os
import getpass

path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Hello my name is Cabe, I am you're new virtual assistant.") #BOT INFO
while True:
    code = input("<> ")
    if code == "i need help":
        print("Go to this link to get help: https://www.youtube.com/watch?v=xvFZjo5PgG0")

    if code == "who are you":
        print("I'm a virtual assistant called Cabe and I am being worked on by two developers")

#Keep this code, it is not needed to work
    if code == "what is turtle grapics":
        print("Turtle graphics is a popular way for introducing programming to kids. It was part of the original Logo programming language developed by Wally Feurzeig, Seymour Papert and Cynthia Solomon in 1967.")