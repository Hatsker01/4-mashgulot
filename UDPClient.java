package udp;

import java.io.*;
import java.net.*;
import java.util.Scanner;

/**
 * UDP Client with interactive interface
 * Supports multiple functionalities from the project requirements
 */
class UDPClient {
    private static final String SERVER_HOST = "localhost";
    private static final int SERVER_PORT = 9876;
    private static final int BUFFER_SIZE = 1024;
    
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        DatagramSocket clientSocket = new DatagramSocket();
        InetAddress serverAddress = InetAddress.getByName(SERVER_HOST);
        
        System.out.println("UDP Client ishga tushdi!");
        System.out.println("Server: " + SERVER_HOST + ":" + SERVER_PORT);
        System.out.println();
        System.out.println("Mavjud buyruqlar:");
        System.out.println("- 'salom' - Server bilan salomlashish");
        System.out.println("- 'status' - Server holatini tekshirish");
        System.out.println("- 'vaqt' - Hozirgi vaqtni olish");
        System.out.println("- 'tasodifiy son' - Tasodifiy son olish");
        System.out.println("- 'haroratni yuboring' - Sensor ma'lumoti");
        System.out.println("- 'menga maqol ayting' - Maqol olish");
        System.out.println("- 'ip manzilim qanday?' - IP manzilni olish");
        System.out.println("- 'foydalanuvchilar' - Faol foydalanuvchilar");
        System.out.println("- 'fayl:filename.txt' - Fayl mavjudligini tekshirish");
        System.out.println("- 'id:1' - Ma'lumotlar bazasidan ma'lumot");
        System.out.println("- 'tosh/qaychi/qog'oz' - O'yin");
        System.out.println("- '5 + 3' - Matematik amal");
        System.out.println("- 'json' - JSON formatda ma'lumot");
        System.out.println("- 'exit' - Dasturdan chiqish");
        System.out.println();
        
        while (true) {
            try {
                System.out.print("Xabar yuboring: ");
                String userInput = scanner.nextLine();
                
                if (userInput.equalsIgnoreCase("exit")) {
                    System.out.println("Dasturdan chiqilmoqda...");
                    break;
                }
                
                if (userInput.trim().isEmpty()) {
                    System.out.println("Bo'sh xabar yuborilmaydi!");
                    continue;
                }
                
                // Send message to server
                byte[] sendData = userInput.getBytes();
                DatagramPacket sendPacket = new DatagramPacket(
                    sendData, sendData.length, serverAddress, SERVER_PORT
                );
                clientSocket.send(sendPacket);
                
                // Receive response from server
                byte[] receiveData = new byte[BUFFER_SIZE];
                DatagramPacket receivePacket = new DatagramPacket(
                    receiveData, receiveData.length
                );
                clientSocket.receive(receivePacket);
                
                String serverResponse = new String(receivePacket.getData()).trim();
                System.out.println("SERVERDAN: " + serverResponse);
                System.out.println();
                
            } catch (Exception e) {
                System.err.println("Xatolik: " + e.getMessage());
                System.out.println("Qayta urinib ko'ring...");
            }
        }
        
        clientSocket.close();
        scanner.close();
    }
}
