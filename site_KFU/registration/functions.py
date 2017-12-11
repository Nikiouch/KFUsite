import string, random

alphabet = {'а': 'a',	'б': 'b',	'в': 'v',	'г': 'g',	'д': 'd',	'е': 'e',
						'ё': 'yo','ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k',
						'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
						'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
						'ч': 'ch', 'ш': 'sh', 'щ': 'sh', 'ъ': 'y', 'ы': 'y', 'ь': "'",
						'э': 'e', 'ю': 'yu', 'я': 'ya',
						'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E',
						'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K',
						'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
						'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts',
						'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sh', 'Ъ': 'Y', 'Ы': 'Y',
						'Ь': "'", 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',}

def eng_translate(word):
	for i,j in alphabet.items():
		word = word.replace(i, j)
	return word

def GeneratePassword(login):
	password = ""
	for i in range(0, len(login)):
		password += str(ord(login[i]))
	return password