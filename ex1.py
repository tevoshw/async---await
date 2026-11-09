import asyncio
import time
import random

start = time.time()

def classificar(texto):
    time.sleep(1.0)
    sentimento = random.choice(["positivo", "negativo", "neutro"])
    return {"texto": texto, "sentimento": sentimento}



def main():
    textos = ["adorei", "péssimo", "mais ou menos", "incrível", "horrível"]
    resultados = []

    for texto in textos:
        resultados.append(classificar(texto))


    print(f'Resultados: {resultados}')
    print(f'Tempo total: {time.time() - start:.2f} segundos')


main()

# --------------------------------------------


start = time.time()

async def classificar2(texto):
    await asyncio.sleep(1)
    sentimento = random.choice(["positivo", "negativo", "neutro"])
    return {"texto": texto, "sentimento": sentimento}


async def main2():
    textos = ["adorei", "péssimo", "mais ou menos", "incrível", "horrível"]

    resultados = await asyncio.gather(*(classificar2(texto) for texto in textos))
    
    
    print(f'Resultados: {resultados}')
    print(f'Tempo total async: {time.time() - start:.2f} segundos')
    
    
asyncio.run(main2())