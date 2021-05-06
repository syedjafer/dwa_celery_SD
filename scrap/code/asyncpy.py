import requests
import asyncio
from timeit import default_timer

from file_list import files, fetch

async def get_data_async():
	with requests.Session() as session:
		loop = asyncio.get_event_loop()
		tasks = [loop.run_in_executor(None, fetch, session, file) for file in files]
		for response in await asyncio.gather(*tasks):
			print(response)

if __name__=="__main__":
	start = default_timer()
	asyncio.run(get_data_async())
	elapsed = default_timer() - start
	print(f"{elapsed} seconds")