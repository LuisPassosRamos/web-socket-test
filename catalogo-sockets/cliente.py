import socket
import json

def send_request(action, payload):
    host = "localhost"
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    request = json.dumps({"action": action, **payload})
    client_socket.send(request.encode())

    response = client_socket.recv(1024).decode()
    client_socket.close()

    return json.loads(response)

def main():
    print("--- Product Catalog Client ---")
    
    while True:
        print("\nOptions:")
        print("1. Get product by name")
        print("2. Get products by price")
        print("3. Update product stock")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter product name: ")
            response = send_request("get_by_name", {"name": name})
            print(response)

        elif choice == "2":
            max_price = float(input("Enter maximum price: "))
            response = send_request("get_by_price", {"max_price": max_price})
            print(response)

        elif choice == "3":
            name = input("Enter product name: ")
            new_stock = int(input("Enter new stock quantity: "))
            response = send_request("update_stock", {"name": name, "new_stock": new_stock})
            print(response)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
