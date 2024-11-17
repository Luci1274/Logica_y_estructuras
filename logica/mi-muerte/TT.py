from random import choice

ruleta = open("ruleta.txt","a")
guardado = open("guardado.txt","a")
personas = ["luaciano", "franco", "santino"]
temas = ["arch lix","opensuce","debian"]
contador = 0
while contador != 3:
    persona = choice(personas)
    tema = choice(temas)
    print(persona +","+ tema)
    guardado.write(persona +","+ tema + "\n")
    personas.remove(persona)
    temas.remove(tema)
    contador += 1

