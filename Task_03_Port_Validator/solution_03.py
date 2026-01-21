port = "8080"
# convert string to int
port_number = int(port)
# check port validity
if port_number >= 1 and port_number <= 65535:
    print("Valid")
else:
    print("Invalid")
