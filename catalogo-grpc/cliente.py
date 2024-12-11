import grpc
import service_pb2
import service_pb2_grpc

def exibir_menu():
    print("\nCatálogo de Produtos")
    print("1. Buscar produto por nome")
    print("2. Buscar produtos por preço máximo")
    print("3. Atualizar estoque de produto")
    print("4. Sair")
    return input("\nEscolha uma opção: ")

def buscar_por_nome(stub):
    nome = input("Digite o nome do produto: ")
    try:
        response = stub.GetProductByName(service_pb2.ProductRequest(name=nome))
        print(f"\nProduto encontrado:")
        print(f"Nome: {response.product.name}")
        print(f"Preço: R${response.product.price:.2f}")
        print(f"Estoque: {response.product.stock}")
    except grpc.RpcError as e:
        print(f"\nErro: {e.details()}")

def buscar_por_preco(stub):
    try:
        preco_max = float(input("Digite o preço máximo: R$"))
        response = stub.GetProductsByPrice(service_pb2.PriceRequest(max_price=preco_max))
        print("\nProdutos encontrados:")
        for product in response.products:
            print(f"Nome: {product.name}")
            print(f"Preço: R${product.price:.2f}")
            print(f"Estoque: {product.stock}")
            print("-" * 30)
    except ValueError:
        print("\nErro: Digite um valor numérico válido")

def atualizar_estoque(stub):
    nome = input("Digite o nome do produto: ")
    try:
        novo_estoque = int(input("Digite a nova quantidade em estoque: "))
        response = stub.UpdateProductStock(
            service_pb2.UpdateStockRequest(name=nome, new_stock=novo_estoque)
        )
        print(f"\nResposta: {response.message}")
    except ValueError:
        print("\nErro: Digite um número inteiro válido para o estoque")

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = service_pb2_grpc.ProductCatalogStub(channel)

    while True:
        opcao = exibir_menu()
        
        if opcao == "1":
            buscar_por_nome(stub)
        elif opcao == "2":
            buscar_por_preco(stub)
        elif opcao == "3":
            atualizar_estoque(stub)
        elif opcao == "4":
            print("\nEncerrando o programa...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    run()