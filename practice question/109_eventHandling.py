from time import sleep

async def f1():
    
    sleep(2)
    print('f1')
async def f2():
    # sleep(2)
    print('f2')

from asyncio import run
run(f1())
run(f2())