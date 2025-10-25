package udp;

import java.io.*;
import java.net.*;
import java.util.*;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

/**
 * UDP Server with multiple functionalities
 * Implements various features from the project requirements
 */
class UDPServer {
    private static final int PORT = 9876;
    private static final int BUFFER_SIZE = 1024;
    private static final String LOG_FILE = "log.txt";
    
    // Store connected users
    private static Map<String, InetAddress> connectedUsers = new ConcurrentHashMap<>();
    private static Map<String, Integer> userPorts = new ConcurrentHashMap<>();
    
    // Database simulation
    private static Map<String, String> database = new HashMap<>();
    
    // Sensor data simulation
    private static Random random = new Random();
    
    // Scheduled executor for background services
    private static ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(1);
    
    public static void main(String[] args) throws Exception {
        // Initialize database with sample data
        initializeDatabase();
        
        // Start background service
        startBackgroundService();
        
        DatagramSocket serverSocket = new DatagramSocket(PORT);
        byte[] receiveData = new byte[BUFFER_SIZE];
        byte[] sendData = new byte[BUFFER_SIZE];
        
        System.out.println("UDP Server ishga tushdi! Port: " + PORT);
        System.out.println("Server turli xil xizmatlarni qo'llab-quvvatlaydi:");
        System.out.println("- Oddiy xabar almashish");
        System.out.println("- Chat dasturi");
        System.out.println("- Matematik amallar");
        System.out.println("- Fayl mavjudligini tekshirish");
        System.out.println("- Tasodifiy son generatsiya");
        System.out.println("- Sensor ma'lumotlari");
        System.out.println("- Ma'lumotlar bazasi bilan ishlash");
        System.out.println("- Va boshqalar...");
        
        while (true) {
            try {
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                serverSocket.receive(receivePacket);
                
                String clientMessage = new String(receivePacket.getData()).trim();
                InetAddress clientAddress = receivePacket.getAddress();
                int clientPort = receivePacket.getPort();
                
                // Log the request
                logRequest(clientMessage, clientAddress, clientPort);
                
                // Process the message and get response
                String response = processMessage(clientMessage, clientAddress, clientPort);
                
                // Send response back to client
                sendData = response.getBytes();
                DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, clientAddress, clientPort);
                serverSocket.send(sendPacket);
                
                System.out.println("Kliyent: " + clientAddress + ":" + clientPort + " - " + clientMessage);
                System.out.println("Javob: " + response);
                
            } catch (Exception e) {
                System.err.println("Xatolik: " + e.getMessage());
            }
        }
    }
    
    /**
     * Process incoming messages and return appropriate responses
     */
    private static String processMessage(String message, InetAddress clientAddress, int clientPort) {
        String response = "";
        
        // Register user
        String userKey = clientAddress.toString() + ":" + clientPort;
        connectedUsers.put(userKey, clientAddress);
        userPorts.put(userKey, clientPort);
        
        // Process different types of messages
        if (message.equalsIgnoreCase("salom") || message.equalsIgnoreCase("hello")) {
            response = "Salom! Xush kelibsiz! Server ishlamoqda.";
        }
        else if (message.equalsIgnoreCase("status")) {
            response = "Server ishlamoqda. Faol foydalanuvchilar: " + connectedUsers.size();
        }
        else if (message.equalsIgnoreCase("ip manzilim qanday?")) {
            response = "Sizning IP manzilingiz: " + clientAddress.getHostAddress();
        }
        else if (message.equalsIgnoreCase("foydalanuvchilar")) {
            response = "Faol foydalanuvchilar: " + connectedUsers.size() + " ta";
        }
        else if (message.equalsIgnoreCase("vaqt")) {
            response = "Hozirgi vaqt: " + LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
        }
        else if (message.equalsIgnoreCase("tasodifiy son")) {
            int randomNum = random.nextInt(100) + 1;
            response = "Tasodifiy son (1-100): " + randomNum;
        }
        else if (message.equalsIgnoreCase("haroratni yuboring")) {
            int temperature = random.nextInt(40) + 10; // 10-50 degrees
            response = "Harorat: " + temperature + "°C";
        }
        else if (message.equalsIgnoreCase("menga maqol ayting")) {
            response = "Maqol: 'Bilim - kuchdir. Har bir kuni yangi narsa o'rganing.'";
        }
        else if (message.startsWith("fayl:")) {
            String fileName = message.substring(5).trim();
            File file = new File(fileName);
            if (file.exists()) {
                response = "Fayl '" + fileName + "' mavjud. Hajmi: " + file.length() + " bayt";
            } else {
                response = "Fayl '" + fileName + "' topilmadi";
            }
        }
        else if (message.startsWith("id:")) {
            String id = message.substring(3).trim();
            if (database.containsKey(id)) {
                response = "Ma'lumot (ID: " + id + "): " + database.get(id);
            } else {
                response = "ID '" + id + "' bo'yicha ma'lumot topilmadi";
            }
        }
        else if (message.equalsIgnoreCase("tosh") || message.equalsIgnoreCase("qaychi") || message.equalsIgnoreCase("qog'oz")) {
            String[] choices = {"tosh", "qaychi", "qog'oz"};
            String serverChoice = choices[random.nextInt(3)];
            response = playRockPaperScissors(message.toLowerCase(), serverChoice);
        }
        else if (message.contains("+") || message.contains("-") || message.contains("*") || message.contains("/")) {
            response = calculateMathExpression(message);
        }
        else if (message.equalsIgnoreCase("json")) {
            response = "{\"foydalanuvchi\":\"" + clientAddress.getHostAddress() + "\",\"vaqt\":\"" + 
                      LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")) + 
                      "\",\"status\":\"faol\"}";
        }
        else {
            // Default response - echo with timestamp
            response = "Sizning xabaringiz: '" + message + "' - " + 
                      LocalDateTime.now().format(DateTimeFormatter.ofPattern("HH:mm:ss"));
        }
        
        return response;
    }
    
    /**
     * Calculate mathematical expressions
     */
    private static String calculateMathExpression(String expression) {
        try {
            // Simple math expression parser
            if (expression.contains("+")) {
                String[] parts = expression.split("\\+");
                if (parts.length == 2) {
                    int a = Integer.parseInt(parts[0].trim());
                    int b = Integer.parseInt(parts[1].trim());
                    return "Natija: " + (a + b);
                }
            } else if (expression.contains("-")) {
                String[] parts = expression.split("-");
                if (parts.length == 2) {
                    int a = Integer.parseInt(parts[0].trim());
                    int b = Integer.parseInt(parts[1].trim());
                    return "Natija: " + (a - b);
                }
            } else if (expression.contains("*")) {
                String[] parts = expression.split("\\*");
                if (parts.length == 2) {
                    int a = Integer.parseInt(parts[0].trim());
                    int b = Integer.parseInt(parts[1].trim());
                    return "Natija: " + (a * b);
                }
            } else if (expression.contains("/")) {
                String[] parts = expression.split("/");
                if (parts.length == 2) {
                    int a = Integer.parseInt(parts[0].trim());
                    int b = Integer.parseInt(parts[1].trim());
                    if (b != 0) {
                        return "Natija: " + (a / b);
                    } else {
                        return "Xatolik: Nolga bo'lish mumkin emas";
                    }
                }
            }
        } catch (Exception e) {
            return "Xatolik: Noto'g'ri matematik ifoda";
        }
        return "Xatolik: Noto'g'ri format";
    }
    
    /**
     * Play Rock-Paper-Scissors game
     */
    private static String playRockPaperScissors(String clientChoice, String serverChoice) {
        if (clientChoice.equals(serverChoice)) {
            return "Durrang! Siz: " + clientChoice + ", Server: " + serverChoice;
        } else if ((clientChoice.equals("tosh") && serverChoice.equals("qaychi")) ||
                   (clientChoice.equals("qaychi") && serverChoice.equals("qog'oz")) ||
                   (clientChoice.equals("qog'oz") && serverChoice.equals("tosh"))) {
            return "Yutdingiz! Siz: " + clientChoice + ", Server: " + serverChoice;
        } else {
            return "Yutqazdingiz! Siz: " + clientChoice + ", Server: " + serverChoice;
        }
    }
    
    /**
     * Log requests to file
     */
    private static void logRequest(String message, InetAddress clientAddress, int clientPort) {
        try {
            FileWriter writer = new FileWriter(LOG_FILE, true);
            String timestamp = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
            writer.write(timestamp + " - " + clientAddress + ":" + clientPort + " - " + message + "\n");
            writer.close();
        } catch (IOException e) {
            System.err.println("Log yozishda xatolik: " + e.getMessage());
        }
    }
    
    /**
     * Initialize sample database
     */
    private static void initializeDatabase() {
        database.put("1", "Ahmad Karimov - Dasturchi");
        database.put("2", "Malika Toshmatova - Dizayner");
        database.put("3", "Javlon Umarov - Menejer");
        database.put("4", "Dilnoza Rahimova - Marketing");
        database.put("5", "Bobur Ismoilov - Texnik");
    }
    
    /**
     * Start background service that sends periodic messages
     */
    private static void startBackgroundService() {
        scheduler.scheduleAtFixedRate(() -> {
            try {
                // Send periodic messages to all connected users
                if (!connectedUsers.isEmpty()) {
                    String message = "Server xabari: " + LocalDateTime.now().format(DateTimeFormatter.ofPattern("HH:mm:ss"));
                    byte[] data = message.getBytes();
                    
                    for (Map.Entry<String, InetAddress> entry : connectedUsers.entrySet()) {
                        try {
                            DatagramSocket socket = new DatagramSocket();
                            DatagramPacket packet = new DatagramPacket(
                                data, data.length, 
                                entry.getValue(), 
                                userPorts.get(entry.getKey())
                            );
                            socket.send(packet);
                            socket.close();
                        } catch (Exception e) {
                            // Remove inactive users
                            connectedUsers.remove(entry.getKey());
                            userPorts.remove(entry.getKey());
                        }
                    }
                }
            } catch (Exception e) {
                System.err.println("Background service xatoligi: " + e.getMessage());
            }
        }, 10, 10, TimeUnit.SECONDS);
    }
}
