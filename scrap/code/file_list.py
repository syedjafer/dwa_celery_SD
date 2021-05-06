files = [f"https://genjipress.com/{year}" for year in range(1995, 2000)]
from timeit import default_timer

def fetch(session, url):
	start = default_timer()
	with session.get(url) as response:
		total = default_timer() - start
		data = response.text
		return f"{response.status_code} {url} {len(data)} bytes read {total} seconds"
		  