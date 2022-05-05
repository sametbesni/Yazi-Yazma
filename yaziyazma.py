import sys
import time
def print_slow(text):
	for letter in text :
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.1)

	
print_slow('Python, nesne yönelimli, yorumlamalı,' "\n"
'birimsel ve etkileşimli yüksek seviyeli bir programlama dilidir.' "\n"
'Girintilere dayalı basit söz dizimi, dilin öğrenilmesini ve akılda kalmasını kolaylaştırır')