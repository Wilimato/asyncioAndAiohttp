'''
Resumen
async def: Define una coroutine.
await: Espera a que una coroutine se complete.
asyncio.run(): Ejecuta la coroutine principal y sólo puede ser llamado una vez.
asyncio.create_task(): Ejecuta coroutines de manera concurrente como tareas.
asyncio.gather(): Ejecuta múltiples coroutines concurrentemente y espera a que todas
'''


import asyncio


async def mi_coroutine():
    print("Hola, asyncio 1!")
    await asyncio.sleep(5)
    print("Adiós, asyncio 1!")


async def otra_coroutine():
    print("Hola, asyncio 2!")
    await asyncio.sleep(1)
    print("Adiós, asyncio 2!")


async def main():
    await asyncio.gather(
        mi_coroutine(),
        otra_coroutine()
    )

asyncio.run(main())

exit()


async def main():
    tarea1 = asyncio.create_task(mi_coroutine())
    tarea2 = asyncio.create_task(otra_coroutine())

    await tarea1
    await tarea2

asyncio.run(main())
