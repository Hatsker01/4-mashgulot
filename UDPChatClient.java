package udp;

import java.io.*;
import java.net.*;
import java.util.Scanner;

/**
 * UDP Chat Client for real-time messaging
 * Implements chat functionality from project requirements
 */
class UDPChatClient {
    private static final String SERVER_HOST = "localhost";
    private static final int SERVER_PORT = 9876;
    private static final int BUFFER_SIZE = 1024;
    
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        DatagramSocket clientSocket = new DatagramSocket();
        InetAddress serverAddress = InetAddress.getByName(SERVER_HOST);
        
        System.out.println("=== UDP Chat Client ===");
        System.out.println("Server: " + SERVER_HOST + ":" + SERVER_PORT);
        System.out.println("Chat dasturi ishga tushdi!");
        System.out.println("Xabarlarni yuboring (chiqish uchun 'exit' yozing):");
        System.out.println();
        
        // Start listening for messages in a separate thread
        Thread listenerThread = new Thread(() -> {
            while (true) {
                try {
                    byte[] receiveData = new byte[BUFFER_SIZE];
                    DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                    clientSocket.receive(receivePacket);
                    
                    String message = new String(receivePacket.getData()).trim();
                    System.out.println("<< " + message);
                    
                } catch (Exception e) {
                    if (!clientSocket.isClosed()) {
                        System.err.println("Xabar olishda xatolik: " + e.getMessage());
                    }
                    break;
                }
            }
        });
        listenerThread.setDaemon(true);
        listenerThread.start();
        
        // Main chat loop
        while (true) {
            try {
                System.out.print("Siz: ");
                String userInput = scanner.nextLine();
                
                if (userInput.equalsIgnoreCase("exit")) {
                    System.out.println("Chatdan chiqilmoqda...");
                    break;
                }
                
                if (userInput.trim().isEmpty()) {
                    continue;
                }
                
                // Send message to server
                byte[] sendData = userInput.getBytes();
                DatagramPacket sendPacket = new DatagramPacket(
                    sendData, sendData.length, serverAddress, SERVER_PORT
                );
                clientSocket.send(sendPacket);
                
            } catch (Exception e) {
                System.err.println("Xatolik: " + e.getMessage());
            }
        }
        
        clientSocket.close();
        scanner.close();
    }
}
