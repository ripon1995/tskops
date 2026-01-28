bucket_name = "My Project Backup"
# strip string
bucket_name = bucket_name.strip()
# split and lowercase conversion
bucket_name = bucket_name.lower().split(" ")
# join with hyphen
bucket_name = "-".join(bucket_name)

print(bucket_name)
