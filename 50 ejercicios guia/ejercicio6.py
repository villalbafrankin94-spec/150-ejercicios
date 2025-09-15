edad = int(input("Introduce tu edad: "))
mensaje_edad = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
mensaje_voto = "Puedes votar" if edad >= 18 else "Aún no puedes votar"
print(mensaje_edad)
print(mensaje_voto)
print(f"Tu edad es: {edad} años")