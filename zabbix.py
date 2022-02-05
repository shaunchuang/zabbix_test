import requests
import json

hea = {"Content-Type":"application/json"}
zabbix_data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 0
}


req = requests.get('http://172.16.156.133/zabbix/api_jsonrpc.php',data=json.dumps(zabbix_data),headers=hea)


result = req.json()
print(result)