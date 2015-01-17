print "\nWelcome to The Jargon Translator for \"lol\" (French)"

J = 'rg'

while(True):
	word = raw_input('\nEntrez le mot "lol":\n')
	
	if len(word) > 0 and word.isalpha():
		rem_caps = word.lower()
		if rem_caps == "lol":	
			rem_l = rem_caps[0:2]
			new_word = rem_l + J + rem_caps[1:3]
			print '\nMot en Jargon: ' + new_word
		else:
			print '\nCe mot n\'est pas "LOL" et vous n\'etes pas bien dans votre tete, Veuillez recommencer dumbass'
			continue
			 	
		oui_ou_non = raw_input('\nVoullez vous le reconvertir en francais? "oui" ou "non":\n')
			
		if oui_ou_non == "oui":
			print '\nEt voila!: ' + word
			print '\nAu revoir!'
			break
		else:
			print '\nAu revoir!'
			break	 
			
	else:
		print 'Veuillez reessailler'