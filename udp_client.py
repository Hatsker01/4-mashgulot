#!/usr/bin/env python3
"""
UDP Client with interactive interface
Supports multiple functionalities from the project requirements
"""

import socket
import sys

class UDPClient:
    def __init__(self, host='localhost', port=9876):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def start(self):
        """Start the UDP client"""
        print("UDP Client ishga tushdi!")
        print(f"Server: {self.host}:{self.port}")
        print()
        print("Mavjud buyruqlar:")
        print("- 'salom' - Server bilan salomlashish")
        print("- 'status' - Server holatini tekshirish")
        print("- 'vaqt' - Hozirgi vaqtni olish")
        print("- 'tasodifiy son' - Tasodifiy son olish")
        print("- 'haroratni yuboring' - Sensor ma'lumoti")
        print("- 'menga maqol ayting' - Maqol olish")
        print("- 'ip manzilim qanday?' - IP manzilni olish")
        print("- 'foydalanuvchilar' - Faol foydalanuvchilar")
        print("- 'fayl:filename.txt' - Fayl mavjudligini tekshirish")
        print("- 'id:1' - Ma'lumotlar bazasidan ma'lumot")
        print("- 'tosh/qaychi/qog'oz' - O'yin")
        print("- '5 + 3' - Matematik amal")
        print("- 'json' - JSON formatda ma'lumot")
        print("- 'exit' - Dasturdan chiqish")
        print()
        
        while True:
            try:
                user_input = input("Xabar yuboring: ").strip()
                
                if user_input.lower() == 'exit':
                    print("Dasturdan chiqilmoqda...")
                    break
                
                if not user_input:
                    print("Bo'sh xabar yuborilmaydi!")
                    continue
                
                # Send message to server
                self.socket.sendto(user_input.encode('utf-8'), (self.host, self.port))
                
                # Receive response from server
                data, addr = self.socket.recvfrom(1024)
                server_response = data.decode('utf-8')
                
                print(f"SERVERDAN: {server_response}")
                print()
                
            except KeyboardInterrupt:
                print("\nDasturdan chiqilmoqda...")
                break
            except Exception as e:
                print(f"Xatolik: {e}")
                print("Qayta urinib ko'ring...")
        
        self.socket.close()

def main():
    """Main function to start the client"""
    client = UDPClient()
    try:
        client.start()
    except KeyboardInterrupt:
        print("\nClient to'xtatilmoqda...")

if __name__ == "__main__":
    main()
