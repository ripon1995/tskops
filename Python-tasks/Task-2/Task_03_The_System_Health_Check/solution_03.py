import json


def process_server_data(json_string):
    try:
        res = json.loads(json_string)
        servers = res["servers"]

        for server in servers:
            print(f"server => {server['name']} & status => {server['status']}")

    except json.JSONDecodeError as e:
        print(f"Error found => {str(e)}")


mock_api = '{"servers": [{"name": "web-01", "status": "up"}, {"name": "db-01", "status": "down"}]}'
process_server_data(mock_api)
