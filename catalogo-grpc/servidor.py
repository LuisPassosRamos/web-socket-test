import grpc
from concurrent import futures
import service_pb2
import service_pb2_grpc

class ProductCatalogServicer(service_pb2_grpc.ProductCatalogServicer):
    def __init__(self):
        self.products = {
            "Apple": {"price": 1.5, "stock": 100},
            "Banana": {"price": 0.5, "stock": 200}
        }

    def GetProductByName(self, request, context):
        product = self.products.get(request.name)
        if not product:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Product not found")
            return service_pb2.ProductResponse()
        return service_pb2.ProductResponse(product=service_pb2.Product(
            name=request.name, price=product["price"], stock=product["stock"]))

    def GetProductsByPrice(self, request, context):
        result = [service_pb2.Product(name=name, price=info["price"], stock=info["stock"])
                  for name, info in self.products.items() if info["price"] <= request.max_price]
        return service_pb2.ProductList(products=result)

    def UpdateProductStock(self, request, context):
        if request.name not in self.products:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Product not found")
            return service_pb2.UpdateResponse()
        self.products[request.name]["stock"] = request.new_stock
        return service_pb2.UpdateResponse(message=f"Stock updated for {request.name}")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
service_pb2_grpc.add_ProductCatalogServicer_to_server(ProductCatalogServicer(), server)
server.add_insecure_port("[::]:50051")
print("Server is running on port 50051")
server.start()
server.wait_for_termination()