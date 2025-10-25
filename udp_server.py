#!/usr/bin/env python3
"""
UDP Server with multiple functionalities
Implements various features from the project requirements
"""

import socket
import threading
import time
import random
import json
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

class UDPServer:
    def __init__(self, host='localhost', port=9876):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.connected_users = {}
        self.database = {
            "1": "Ahmad Karimov - Dasturchi",
            "2": "Malika Toshmatova - Dizayner", 
            "3": "Javlon Umarov - Menejer",
            "4": "Dilnoza Rahimova - Marketing",
            "5": "Bobur Ismoilov - Texnik"
        }
        self.log_file = "log.txt"
        self.running = True
        
    def start(self):
        """Start the UDP server"""
        try:
            self.socket.bind((self.host, self.port))
            print(f"UDP Server ishga tushdi! Port: {self.port}")
            print("Server turli xil xizmatlarni qo'llab-quvvatlaydi:")
            print("- Oddiy xabar almashish")
            print("- Chat dasturi")
            print("- Matematik amallar")
            print("- Fayl mavjudligini tekshirish")
            print("- Tasodifiy son generatsiya")
            print("- Sensor ma'lumotlari")
            print("- Ma'lumotlar bazasi bilan ishlash")
            print("- Va boshqalar...")
            print()
            
            # Start background service
            self.start_background_service()
            
            # Main server loop
            while self.running:
                try:
                    data, addr = self.socket.recvfrom(1024)
                    client_message = data.decode('utf-8').strip()
                    
                    # Log the request
                    self.log_request(client_message, addr)
                    
                    # Process message in a separate thread
                    threading.Thread(
                        target=self.handle_client,
                        args=(client_message, addr),
                        daemon=True
                    ).start()
                    
                except Exception as e:
                    if self.running:
                        print(f"Xatolik: {e}")
                        
        except Exception as e:
            print(f"Server ishga tushirishda xatolik: {e}")
        finally:
            self.socket.close()
    
    def handle_client(self, message, addr):
        """Handle client message and send response"""
        try:
            # Register user
            user_key = f"{addr[0]}:{addr[1]}"
            self.connected_users[user_key] = addr
            
            # Process message and get response
            response = self.process_message(message, addr)
            
            # Send response back to client
            self.socket.sendto(response.encode('utf-8'), addr)
            
            print(f"Kliyent: {addr} - {message}")
            print(f"Javob: {response}")
            print()
            
        except Exception as e:
            print(f"Kliyent bilan ishlashda xatolik: {e}")
    
    def process_message(self, message, addr):
        """Process incoming messages and return appropriate responses"""
        message_lower = message.lower()
        
        if message_lower in ['salom', 'hello']:
            return "Salom! Xush kelibsiz! Server ishlamoqda."
        
        elif message_lower == 'status':
            return f"Server ishlamoqda. Faol foydalanuvchilar: {len(self.connected_users)}"
        
        elif message_lower == 'ip manzilim qanday?':
            return f"Sizning IP manzilingiz: {addr[0]}"
        
        elif message_lower == 'foydalanuvchilar':
            return f"Faol foydalanuvchilar: {len(self.connected_users)} ta"
        
        elif message_lower == 'vaqt':
            return f"Hozirgi vaqt: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        elif message_lower == 'tasodifiy son':
            random_num = random.randint(1, 100)
            return f"Tasodifiy son (1-100): {random_num}"
        
        elif message_lower == 'haroratni yuboring':
            temperature = random.randint(10, 50)
            return f"Harorat: {temperature}°C"
        
        elif message_lower == 'menga maqol ayting':
            return "Maqol: 'Bilim - kuchdir. Har bir kuni yangi narsa o'rganing.'"
        
        elif message.startswith('fayl:'):
            filename = message[5:].strip()
            if os.path.exists(filename):
                size = os.path.getsize(filename)
                return f"Fayl '{filename}' mavjud. Hajmi: {size} bayt"
            else:
                return f"Fayl '{filename}' topilmadi"
        
        elif message.startswith('id:'):
            id_key = message[3:].strip()
            if id_key in self.database:
                return f"Ma'lumot (ID: {id_key}): {self.database[id_key]}"
            else:
                return f"ID '{id_key}' bo'yicha ma'lumot topilmadi"
        
        elif message_lower in ['tosh', 'qaychi', 'qog\'oz']:
            choices = ['tosh', 'qaychi', 'qog\'oz']
            server_choice = random.choice(choices)
            return self.play_rock_paper_scissors(message_lower, server_choice)
        
        elif any(op in message for op in ['+', '-', '*', '/']):
            return self.calculate_math_expression(message)
        
        elif message_lower == 'json':
            data = {
                "foydalanuvchi": addr[0],
                "vaqt": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "status": "faol"
            }
            return json.dumps(data, ensure_ascii=False)
        
        else:
            # Default response - echo with timestamp
            return f"Sizning xabaringiz: '{message}' - {datetime.now().strftime('%H:%M:%S')}"
    
    def calculate_math_expression(self, expression):
        """Calculate mathematical expressions"""
        try:
            if '+' in expression:
                parts = expression.split('+')
                if len(parts) == 2:
                    a = int(parts[0].strip())
                    b = int(parts[1].strip())
                    return f"Natija: {a + b}"
            elif '-' in expression:
                parts = expression.split('-')
                if len(parts) == 2:
                    a = int(parts[0].strip())
                    b = int(parts[1].strip())
                    return f"Natija: {a - b}"
            elif '*' in expression:
                parts = expression.split('*')
                if len(parts) == 2:
                    a = int(parts[0].strip())
                    b = int(parts[1].strip())
                    return f"Natija: {a * b}"
            elif '/' in expression:
                parts = expression.split('/')
                if len(parts) == 2:
                    a = int(parts[0].strip())
                    b = int(parts[1].strip())
                    if b != 0:
                        return f"Natija: {a / b}"
                    else:
                        return "Xatolik: Nolga bo'lish mumkin emas"
        except Exception as e:
            return f"Xatolik: Noto'g'ri matematik ifoda - {e}"
        
        return "Xatolik: Noto'g'ri format"
    
    def play_rock_paper_scissors(self, client_choice, server_choice):
        """Play Rock-Paper-Scissors game"""
        if client_choice == server_choice:
            return f"Durrang! Siz: {client_choice}, Server: {server_choice}"
        elif ((client_choice == 'tosh' and server_choice == 'qaychi') or
              (client_choice == 'qaychi' and server_choice == 'qog\'oz') or
              (client_choice == 'qog\'oz' and server_choice == 'tosh')):
            return f"Yutdingiz! Siz: {client_choice}, Server: {server_choice}"
        else:
            return f"Yutqazdingiz! Siz: {client_choice}, Server: {server_choice}"
    
    def log_request(self, message, addr):
        """Log requests to file"""
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                f.write(f"{timestamp} - {addr[0]}:{addr[1]} - {message}\n")
        except Exception as e:
            print(f"Log yozishda xatolik: {e}")
    
    def start_background_service(self):
        """Start background service that sends periodic messages"""
        def background_task():
            while self.running:
                time.sleep(10)  # Wait 10 seconds
                if self.connected_users and self.running:
                    message = f"Server xabari: {datetime.now().strftime('%H:%M:%S')}"
                    # Send to all connected users
                    for user_key, addr in list(self.connected_users.items()):
                        try:
                            self.socket.sendto(message.encode('utf-8'), addr)
                        except:
                            # Remove inactive users
                            if user_key in self.connected_users:
                                del self.connected_users[user_key]
        
        threading.Thread(target=background_task, daemon=True).start()
    
    def stop(self):
        """Stop the server"""
        self.running = False
        self.socket.close()

def main():
    """Main function to start the server"""
    server = UDPServer()
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nServer to'xtatilmoqda...")
        server.stop()

if __name__ == "__main__":
    main()
