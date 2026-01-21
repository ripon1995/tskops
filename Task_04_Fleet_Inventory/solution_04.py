servers = ["web01", "db01", "app01", "web02", "web03"]
# get the first and last slice
web_servers = servers[:1] + servers[-1:]
print(web_servers)
