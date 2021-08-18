print("\nPROGRAM PERHITUNGAN TEMPERATUR\n")

celsius = float(input("Masukan nilai temperatur dalam celcius: "))

print("Suhu dalam celcius: ",celsius,"C")


# Reamur
reamur = (4/5) * celsius

print("Suhu dalam reamur: ",reamur,"R")
#Fahrenheit
fahrenheit = ((9/5) * celsius) + 32

print("Suhu dalam fahrenheit: ",fahrenheit,"F")
#Kelvin
kelvin = celsius + 273

print("Suhu dalam kelvin: ",kelvin,"K")

print("\nTUGAS DARI KELAS TERBUKA\n")

fahrenheit = float(input("Masukan nilai temperatur dalam fahrenheit: "))

print("Suhu dalam fahrenheit: ",fahrenheit,"F")



#Kelvin
kelvin = ((fahrenheit - 32) * 5/9) + 273

print("Suhu dalam kelvin: ",kelvin,"K")



kelvin = float(input("Masukan nilai temperatur dalam kelvin: "))

print("Suhu dalam kelvin: ",kelvin,"K")



# Fahrenheit
fahrenheit = ((kelvin - 273) * 9/5) + 32

print("Suhu dalam fahrenheit: ",fahrenheit,"F")
