import requests
from timeit import default_timer
from file_list import files, fetch

def get_data_sync():
	with requests.session() as session:
		for file in files:
			print(fetch(session, file))

if __name__=="__main__":
	start = default_timer()
	get_data_sync()
	elapsed_time = default_timer() - start
	print(f"{elapsed_time} seconds")
