import shutil

source_file = "app.log"

for i in range(1, 6):
    destination = f"app_{i}.log"
    shutil.copy(source_file, destination)
    print(f"Created: {destination}")
