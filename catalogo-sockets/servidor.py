import socket
import json

products = {
    "Apple": {"price": 1.5, "stock": 100},
    "Banana": {"price": 0.5, "stock": 200},
    "Orange": {"price": 0.8, "stock": 150},
}

def handle_request(request):
    try:
        data = json.loads(request)
        action = data["action"]

        if action == "get_by_name":
            name = data["name"]
            product = products.get(name)
            if product:
                return json.dumps({"status": "success", "product": product})
            else:
                return json.dumps({"status": "error", "message": "Product not found"})

        elif action == "get_by_price":
            max_price = data["max_price"]
            filtered = {name: info for name, info in products.items() if info["price"] <= max_price}
            return json.dumps({"status": "success", "products": filtered})

        elif action == "update_stock":
            name = data["name"]
            new_stock = data["new_stock"]
            if name in products:
                products[name]["stock"] = new_stock
                return json.dumps({"status": "success", "message": f"Stock updated for {name}"})
            else:
                return json.dumps({"status": "error", "message": "Product not found"})

        else:
            return json.dumps({"status": "error", "message": "Invalid action"})
    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)})

def start_server():
    host = "localhost"
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server is running on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        request = client_socket.recv(1024).decode()
        response = handle_request(request)
        client_socket.send(response.encode())

        client_socket.close()

if __name__ == "__main__":
    start_server()
