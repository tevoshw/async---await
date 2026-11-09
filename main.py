import asyncio

def normal():
    return "oi"

async def assincrona():
    return "oi"

print(normal())        # "oi" → executa e devolve o resultado direto
print(assincrona())    # <coroutine object ...> → NÃO executa, devolve um objeto corrotina


# ----------------------------------------------------


import time


async def tarefa(nome):
    print(nome, "começou")
    await asyncio.sleep(1)
    print(nome, "terminou")

async def main():
    await asyncio.gather(tarefa("A"), tarefa("B"))

asyncio.run(main())

# ---------------------------------------------------

async def soma(a, b):
    await asyncio.sleep(1)
    return a + b


async def main():
    r = await asyncio.gather(
                            soma(1, 2), 
                             soma(10, 20), 
                             soma(100, 200)
                            )
    print(r) 


asyncio.run(main())

