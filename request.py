import requests
url = 'http://localhost:5000/api'

r = requests.post(url,json={"features": [[-0.37135657, -1.77189864,  1.53502303, -1.44259587, -0.45415004,
        -1.21544181, -0.47434359]]}
)


print(r.json())


