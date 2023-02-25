import requests

url = "https://slack.com/api/conversations.history" 
token = "xoxb-4500642037156-4806424529904-2C6rYiFizDCnvMU1L3N2E32c"

header={
    "Authorization": "Bearer {}".format(token)
}

payload  = {
    "channel" : "C04EN23AHV1"
}

res = requests.get(url, headers=header, params=payload)

print(res.json())