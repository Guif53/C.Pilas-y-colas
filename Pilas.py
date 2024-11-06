from collections import deque
import string
import random

def id_generator(size=6):
    chars=string.ascii_uppercase + string.digits #ascii es las letras en mayus y digits es del 0 al 9 
    return ''.join(random.choice(chars) for _ in range(size))

pila = []
pila.append ("Narnia")
pila.append ("Cuantica")
pila.append ("Omega")

print(pila)

pila.pop() #como es FILO nos quita la ultima de la lista "Omega"
pila.pop()

print(pila)

cola = deque()
lista_gente = ["Beta","Omega","Gamma","Fi","Alfa"]
aforo_max = 3
numero_gente_dentro = 0
gente_dentro = deque()


for persona in lista_gente:
        if persona == "Fi":
            print(f"{persona} no entra aqui")
        else:
            cola.append(persona)
            print(" ".join(cola)) #el .join es para que el deque no aparezca de manera que lo primero que pongas lo sustituya

#gente q va entrando
while numero_gente_dentro < aforo_max:
    entrando = cola.popleft()
    gente_dentro.append(entrando)
    print("Estan dentro: ", ", ".join(gente_dentro), " y estan esperando ", ", ".join(cola), f"{entrando}, está entrando")
    numero_gente_dentro += 1

string_gente_fuera2 = ", ".join(cola)

decuentos_por_no_entrar = 10.00

descuentos = []

for persona_fuera in cola:
    codigo_descuento = id_generator()
    descuento = {"nombre": persona_fuera, "codigo_descuento": codigo_descuento, "importante": decuentos_por_no_entrar}
    descuentos.append(descuento)

print(f"Se han quedado fuera {string_gente_fuera2}")
print(descuentos)