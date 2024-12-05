package com.sistema.catalogo.servidor;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.HashMap;
import java.util.Map;

public class Servidor {
    private static Map<String, Produto> catalogo = new HashMap<>();

    public static void main(String[] args) {
        // Inicializa o catálogo
        catalogo.put("Camiseta", new Produto("Camiseta", 50.0, 10));
        catalogo.put("Tenis", new Produto("Tenis", 200.0, 5));
        catalogo.put("Calça", new Produto("Calça", 100.0, 15));

        try (ServerSocket serverSocket = new ServerSocket(12345)) {
            System.out.println("Servidor iniciado na porta 12345...");

            while (true) {
                Socket clienteSocket = serverSocket.accept();
                System.out.println("Cliente conectado: " + clienteSocket.getInetAddress());

                try (BufferedReader input = new BufferedReader(new InputStreamReader(clienteSocket.getInputStream()));
                     PrintWriter output = new PrintWriter(clienteSocket.getOutputStream(), true)) {

                    String comando = input.readLine();
                    String resposta = processarComando(comando);
                    output.println(resposta);
                }

                clienteSocket.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static String processarComando(String comando) {
        String[] partes = comando.split(" ");
        String acao = partes[0];

        switch (acao.toLowerCase()) {
            case "consultar":
                return consultarProduto(partes[1]);
            case "atualizar":
                return atualizarEstoque(partes[1], Integer.parseInt(partes[2]));
            default:
                return "Comando inválido!";
        }
    }

    private static String consultarProduto(String nome) {
        Produto produto = catalogo.get(nome);
        if (produto == null) {
            return "Produto não encontrado!";
        }
        return produto.toString();
    }

    private static String atualizarEstoque(String nome, int quantidade) {
        Produto produto = catalogo.get(nome);
        if (produto == null) {
            return "Produto não encontrado!";
        }
        produto.setQuantidade(quantidade);
        return "Estoque atualizado: " + produto.toString();
    }
}

class Produto {
    private String nome;
    private double preco;
    private int quantidade;

    public Produto(String nome, double preco, int quantidade) {
        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
    }

    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }

    @Override
    public String toString() {
        return String.format("Produto: %s, Preço: %.2f, Quantidade: %d", nome, preco, quantidade);
    }
}
