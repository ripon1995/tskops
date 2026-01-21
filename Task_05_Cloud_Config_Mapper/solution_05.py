vm = {
    "id": "virtual machine 1",
    "ip": "222.222.222.222",
    "status": "running",
    "region": "asia-west",
}

vm["status"] = "stopped"
vm.update({"instance_type": "t3.large"})

print(vm)
