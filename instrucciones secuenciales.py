#Taller 2 python
#Moises Castro 
#5 de noviembre de 2021 


from datetime import date 
hoy=date.today()
print("hoy es el día: ", hoy)

a=int(input("digite el primer numero: "))
b=int(input("digite el segundo numero: "))
c=int(input("digite el tercer numero: "))
x=[a,b,c]
print("el valor maximo es: ", max (x))
print("el valor minimo es: ", min (x))
print("la suma de los 3 numeros es: ", sum(x))
print("")
z=float(input("digite un numero con decimales: "))
redondo=round(z)
print("el valor de ", z, "redondeando es: ", redondo)
print("")
frase=input("digite una oración: ")
print("la frase en mayuscula es: ", frase.upper())
print("la frase en minuscula es: ", frase.lower())
print("la frase con mayuscula inicial es: ", frase.capitalize())
print("la longitud de la frase es: ", len(frase), "caracteres")
print("la frase con mayuscula inicial es: ", frase.title())
print("")
print("FIN DEL PROGRAMA")




