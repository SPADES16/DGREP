import os
import colorama

colorama.init()

def dg_grep():
	print ("\033[4;92m")
	usm = input("Enter File To Search User In:")
	sd = input("Enter User To Search:")
	for line in open(usm):
		if sd in line:
			os.system('cls')
			print ("\033[4;96m" + "USER DATA FOUND FOR:" + sd + "\n" +"\033[4;92m" + "\n" + line)
			break
		else:
			print ("\033[4;91m" + "NOTHING FOUND ON USER:" + "\033[4;96m" + sd)
				
				
dg_grep()