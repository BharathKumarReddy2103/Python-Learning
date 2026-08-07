server = {
    "name": "web01",
    "status": "Running"
}

server.update({
    "status": "Stopped",
    "region": "ap-south-1"
})

print(server)