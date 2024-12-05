package com.sistema.catalogo.cliente;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Cliente {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 12345);
             BufferedReader teclado = new BufferedReader(new InputStreamReader(System.in));
             PrintWriter output = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()))) {

            System.out.println("Conectado ao servidor. Digite comandos (consultar <produto>, atualizar <produto> <quantidade>):");

            while (true) {
                System.out.print("> ");
                String comando = teclado.readLine();
                if ("sair".equalsIgnoreCase(comando)) {
                    break;
                }

                output.println(comando);
                String resposta = input.readLine();
                System.out.println("Servidor: " + resposta);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}