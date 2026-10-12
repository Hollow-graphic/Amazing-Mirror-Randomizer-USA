#This script randomizes each of the 32 minibosses in the game.
#There four values to set: X/Y, object ID, camera lock data, and difficulty.
#Camera lock data is how close you need to be to the miniboss to start the fight.
#Difficulty is one byte that makes the miniboss slightly faster and have less downtime between attacks/patterns, either a 00 or 01.
import random
import os
import json
from amrShared import *
#==================================================
def randomizeEnemies(romFile,enemiesMode,difficulty):
	print("Randomizing the enemies...")
	enemies = json.load(open('JSON\enemies.json'))
	enemiesKeys = enemies["address"]
 
	enemiesListAdress = []
	enemiesListValue = []
	
	if enemiesMode == "Shuffle Enemies":
		for i in range(len(enemiesKeys)):
			address = enemiesKeys[i]
			value = readValueToRom(romFile, address, 36)
			if value[12] in enemies["listid_basic"]:
				# make every Enemy have speed 8
				# writeValueToRom(romFile, address + 16, 8, 1)
				
				enemiesListAdress.append(address)
				enemiesListValue.append([value[12], value[14]])
		random.shuffle(enemiesListValue)
	else:
		for i in range(len(enemiesKeys)):
			address = enemiesKeys[i]
			value = readValueToRom(romFile, address, 36)
			if value[12] in enemies["listid_basic"]:
				enemiesListAdress.append(address)
				if enemiesMode == "Randomize Enemies":
					enemiesListValue.append([random.choice(enemies["listid_basic"]), value[14]])
				if enemiesMode == "Randomize Enemies Chaos":
					enemiesListValue.append([random.choice(enemies["listid_basic"]), value[14]])

	for i in range(len(enemiesListAdress)):
		print(f"{hex(enemiesListAdress[i])} {hex(readValueToRom(romFile, enemiesListAdress[i] + 12, 1)[0])} > {hex(enemiesListValue[i][0])}")
		#if enemiesListValue[i][0] == 6 and enemiesMode == "Randomize Enemies Choas": #make gordo go FAST!! eheh
		#	writeValueToRom(romFile, enemiesListAdress[i] + 16, 8, 1)
		writeValueToRom(romFile, enemiesListAdress[i] + 12, enemiesListValue[i][0], 1)
		writeValueToRom(romFile, enemiesListAdress[i] + 14, enemiesListValue[i][1], 1)
#==================================================
