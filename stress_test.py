import timeit
import requests

reps = timeit.repeat(lambda : requests.get('http://127.0.0.1:5000/campaigns/42'), repeat=5, number=5000)

print(f'Avg time to execute 5000 campaign requests: {sum(reps) / 5}')