import grpc
import service_pb2
import service_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = service_pb2_grpc.ProductCatalogStub(channel)

    print("--- GetProductByName ---")
    try:
        response = stub.GetProductByName(service_pb2.ProductRequest(name="Apple"))
        print(f"Name: {response.product.name}, Price: {response.product.price}, Stock: {response.product.stock}")
    except grpc.RpcError as e:
        print(e.details())

    print("--- GetProductsByPrice ---")
    response = stub.GetProductsByPrice(service_pb2.PriceRequest(max_price=1.0))
    for product in response.products:
        print(f"Name: {product.name}, Price: {product.price}, Stock: {product.stock}")

    print("--- UpdateProductStock ---")
    response = stub.UpdateProductStock(service_pb2.UpdateStockRequest(name="Apple", new_stock=150))
    print(response.message)

if __name__ == "__main__":
    run()