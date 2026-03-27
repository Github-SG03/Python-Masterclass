############################################################
# ASYNC PROGRAMMING IN PYTHON (BASIC → ADVANCED)
# Learn async, await, event loop step by step
############################################################

############################################################
# 1. WHAT IS ASYNC PROGRAMMING?
# Async = running multiple tasks WITHOUT waiting (non-blocking)
# Used for I/O tasks (API calls, DB, network)
############################################################

import asyncio
import time


############################################################
# 2. NORMAL (SYNCHRONOUS) FUNCTION
############################################################

def sync_task(name):
    print(f"Start {name}")
    time.sleep(2)  # blocks execution
    print(f"End {name}")


# Example:
# sync_task("Task1")
# sync_task("Task2")
# Takes ~4 seconds total


############################################################
# 3. ASYNC FUNCTION
############################################################

async def async_task(name):
    print(f"Start {name}")
    await asyncio.sleep(2)  # non-blocking sleep
    print(f"End {name}")


############################################################
# 4. RUN ASYNC FUNCTION
############################################################

# asyncio.run(async_task("Task1"))


############################################################
# 5. RUN MULTIPLE TASKS (CONCURRENTLY)
############################################################

async def main():
    task1 = async_task("Task1")
    task2 = async_task("Task2")

    await task1
    await task2


# asyncio.run(main())
# Still sequential (waits one after another)


############################################################
# 6. TRUE CONCURRENCY USING gather()
############################################################

async def main_concurrent():
    await asyncio.gather(
        async_task("Task1"),
        async_task("Task2")
    )


# asyncio.run(main_concurrent())
# Runs both at same time (~2 sec total)


############################################################
# 7. CREATE TASKS (ADVANCED)
############################################################

async def main_tasks():
    t1 = asyncio.create_task(async_task("Task1"))
    t2 = asyncio.create_task(async_task("Task2"))

    await t1
    await t2


# asyncio.run(main_tasks())


############################################################
# 8. RETURN VALUES FROM ASYNC
############################################################

async def get_data():
    await asyncio.sleep(1)
    return "Data received"


async def main_return():
    result = await get_data()
    print(result)


# asyncio.run(main_return())


############################################################
# 9. ASYNC + HTTP REQUEST (REAL USE CASE)
############################################################

# Install: pip install aiohttp

import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main_api():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    data = await fetch_data(url)
    print("\nAPI Data:", data[:100])


# asyncio.run(main_api())


############################################################
# 10. ERROR HANDLING
############################################################

async def error_task():
    try:
        await asyncio.sleep(1)
        raise ValueError("Something went wrong")
    except Exception as e:
        print("Error:", e)


# asyncio.run(error_task())


############################################################
# 11. TIMEOUT HANDLING
############################################################

async def long_task():
    await asyncio.sleep(5)


async def main_timeout():
    try:
        await asyncio.wait_for(long_task(), timeout=2)
    except asyncio.TimeoutError:
        print("Task timed out!")


# asyncio.run(main_timeout())


############################################################
# 12. IMPORTANT CONCEPTS
############################################################

# async → defines async function
# await → waits for async result (non-blocking)
# event loop → runs all async tasks
# gather() → run multiple tasks concurrently
# create_task() → schedule background task


############################################################
# 13. WHEN TO USE ASYNC?
############################################################

# Use async for:
# - API calls
# - Database queries
# - Network operations

# Don't use for:
# - CPU-heavy tasks (use multiprocessing instead)


############################################################
# END NOTE
############################################################

print("\n🎉 Async Programming Learning Completed!")