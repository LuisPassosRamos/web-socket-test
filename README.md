# Documentação do Código

## **GRPC (gRPC)**

### **Descrição**
O sistema implementado em gRPC consiste em um servidor e um cliente que interagem para gerenciar um catálogo de produtos. As operações disponíveis incluem:
1. Consultar produtos pelo nome.
2. Consultar produtos com preço abaixo de um valor fornecido.
3. Atualizar o estoque de um produto específico.

### **Componentes**
1. **Arquivo `service.proto`**:
   - Define as mensagens e os serviços do gRPC para comunicação cliente-servidor.
   - Gera os arquivos necessários para implementação em Python usando o comando:
     ```
     python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto
     ```

2. **Servidor (`servidor.py`)**:
   - Implementa o catálogo de produtos como um dicionário.
   - Oferece os serviços definidos no arquivo `.proto`.
   - Responde a requisições do cliente.

3. **Cliente (`cliente.py`)**:
   - Envia requisições ao servidor para realizar operações no catálogo de produtos.
   - Recebe e exibe as respostas.

### **Execução**
1. Gere os arquivos gRPC necessários a partir do `.proto`.
2. Inicie o servidor:
   ```
   python server.py
   ```
3. Execute o cliente:
   ```
   python client.py
   ```

### **Benefícios do gRPC**
- Comunicação eficiente e rápida baseada em Protobuf.
- Suporte nativo para múltiplas linguagens.
- Estrutura robusta para sistemas distribuídos.

---

## **SOCKETS**

### **Descrição**
O sistema implementado com sockets usa a troca direta de mensagens em JSON para gerenciar o catálogo de produtos. Ele também inclui um servidor e um cliente com as mesmas funcionalidades oferecidas no sistema gRPC.

### **Componentes**
1. **Servidor (`server.py`)**:
   - Escuta conexões em uma porta específica (5000).
   - Processa mensagens recebidas do cliente para executar as operações solicitadas.
   - Responde ao cliente com o resultado.

2. **Cliente (`client.py`)**:
   - Conecta-se ao servidor na porta 5000.
   - Envia solicitações no formato JSON para realizar operações no catálogo.
   - Exibe as respostas do servidor.

### **Execução**
1. Inicie o servidor:
   ```
   python server.py
   ```
2. Execute o cliente:
   ```
   python client.py
   ```

### **Vantagens dos Sockets**
- Simples e direto, ideal para entender os fundamentos de redes.
- Controle total sobre o protocolo de comunicação.
- Flexibilidade para personalizar mensagens.

---

## **Comparação entre gRPC e Sockets**

| **Aspecto**           | **gRPC**                         | **Sockets**                        |
|-----------------------|----------------------------------|------------------------------------|
| **Facilidade**        | Mais complexo, mas poderoso     | Simples e direto                  |
| **Eficiência**        | Alta (usa Protobuf)             | Média (depende do formato usado)  |
| **Escalabilidade**    | Alta (suporte a várias línguas) | Média (implementação manual)      |
| **Personalização**    | Limitada ao Protobuf            | Total (controle do protocolo)     |

### **Conclusão**
- Use **gRPC** para sistemas distribuídos robustos, especialmente com múltiplas linguagens ou alto desempenho.
- Use **sockets** para sistemas simples ou para aprendizado básico de redes.