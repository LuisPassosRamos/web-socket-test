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
    print("")
    
    while True:
        print("1. Buscar produto por nome")
        print("2. Buscar produtos por preço máximo")
        print("3. Atualizar estoque de produto")
        print("4. Sair")
        
        choice = input("\nEscolha uma opção: ")

        if choice == "1":
            name = input("Digite o nome do produto: ")
            response = send_request("get_by_name", {"name": name})
            print(response)

        elif choice == "2":
            max_price = float(input("Digite o valor máximo: "))
            response = send_request("get_by_price", {"max_price": max_price})
            print(response)

        elif choice == "3":
            name = input("Digite o nome do produto: ")
            new_stock = int(input("Digite o novo valor de estoque: "))
            response = send_request("update_stock", {"name": name, "new_stock": new_stock})
            print(response)

        elif choice == "4":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Por favor, tente noamente.")

if __name__ == "__main__":
    main()
