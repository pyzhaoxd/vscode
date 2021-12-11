#同步的概念
#异步的概念

#进程、线程、协程 
# 异步 必须要知道什么是协程，什么是任务task， 什么是可等待对象Awaitable Object， 协程可与i理解为线程的优化，看成一种微线程，它比线程更节省资源、效率、更高的系统调度机制
#常用的协程模块为asynci gevent tornado

import asyncio
import time


# async def main():
#     print('hello')
#     await asyncio.sleep(1)
#     print('world')


# print(f"程序于{time.strftime('%X')}开始运行")
# asyncio.run(main())
# print(f"程序于{time.strftime('%X')}结束运行")

# 以上程序一共花费了1秒


#例二
# async def say_affter(what,delay):
#     print(what)
#     await asyncio.sleep(delay)

# async def main():
#     print(f"程序于{time.strftime('%X')}开始运行")
#     await say_affter('hello',1)
#     await say_affter('word',2)
#     print(f"程序于{time.strftime('%X')}结束运行")


# asyncio.run(main())

#以上程序运行一共花费了3秒


#例三 并行测试

async def say_affter(what,delay):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(say_affter('hello',1))
    task2 = asyncio.create_task(say_affter('world',2))
    print(f"程序于{time.strftime('%X')}开始运行")
    await task1
    await task2
    print(f"程序于{time.strftime('%X')}结束运行")

asyncio.run(main())

#以上程序花费了2秒，实际sleep为3
