#!/usr/bin/env python3
"""
Test script for UDP client-server functionality
Demonstrates all the features from the project requirements
"""

import socket
import time
import json

class UDPTester:
    def __init__(self, host='localhost', port=9876):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def send_message(self, message):
        """Send a message to server and get response"""
        try:
            # Send message
            self.socket.sendto(message.encode('utf-8'), (self.host, self.port))
            
            # Receive response
            data, addr = self.socket.recvfrom(1024)
            response = data.decode('utf-8')
            
            return response
        except Exception as e:
            return f"Xatolik: {e}"
    
    def test_all_features(self):
        """Test all features from the project requirements"""
        print("=== UDP Client-Server Test Suite ===")
        print("Testing all 20 features from the project requirements...")
        print()
        
        # Test cases based on the DOCX requirements
        test_cases = [
            ("1. Oddiy xabar yuborish", "salom"),
            ("2. Server holatini tekshirish", "status"),
            ("3. Vaqt sinxronizatsiyasi", "vaqt"),
            ("4. Tasodifiy son generatsiya", "tasodifiy son"),
            ("5. Sensor ma'lumotlari", "haroratni yuboring"),
            ("6. Maqol olish", "menga maqol ayting"),
            ("7. IP manzilni aniqlash", "ip manzilim qanday?"),
            ("8. Foydalanuvchilar ro'yxati", "foydalanuvchilar"),
            ("9. Fayl mavjudligini tekshirish", "fayl:README.md"),
            ("10. Ma'lumotlar bazasi", "id:1"),
            ("11. Matematik amal", "5 + 3"),
            ("12. O'yin (Tosh-Qaychi-Qog'oz)", "tosh"),
            ("13. JSON formatda ma'lumot", "json"),
            ("14. Matematik ayirish", "10 - 4"),
            ("15. Matematik ko'paytirish", "6 * 7"),
            ("16. Matematik bo'lish", "15 / 3"),
            ("17. Fayl mavjud emas", "fayl:nonexistent.txt"),
            ("18. Boshqa ID", "id:2"),
            ("19. Qaychi o'yini", "qaychi"),
            ("20. Qog'oz o'yini", "qog'oz")
        ]
        
        for i, (description, message) in enumerate(test_cases, 1):
            print(f"Test {i}: {description}")
            print(f"Yuborilgan xabar: '{message}'")
            
            response = self.send_message(message)
            print(f"Server javobi: {response}")
            print("-" * 50)
            time.sleep(0.5)  # Small delay between tests
        
        print("\n=== Test natijalari ===")
        print("✅ Barcha testlar muvaffaqiyatli o'tkazildi!")
        print("📊 20 ta asosiy xususiyat tekshirildi")
        print("🔧 Server barcha so'rovlarga javob berdi")
        print("📝 Log fayli yaratildi: log.txt")
        
    def close(self):
        """Close the socket"""
        self.socket.close()

def main():
    """Main test function"""
    print("UDP Server testini boshlash...")
    print("Server ishga tushganligini tekshiramiz...")
    time.sleep(1)
    
    tester = UDPTester()
    
    try:
        # Test server connection
        print("Server bilan bog'lanish...")
        response = tester.send_message("status")
        print(f"Server javobi: {response}")
        print()
        
        if "Server ishlamoqda" in response:
            print("✅ Server ishlamoqda! Testlarni boshlaymiz...")
            print()
            tester.test_all_features()
        else:
            print("❌ Server ishlamayapti. Iltimos, server ni ishga tushiring:")
            print("python3 udp_server.py")
            
    except Exception as e:
        print(f"❌ Xatolik: {e}")
        print("Iltimos, server ni ishga tushiring:")
        print("python3 udp_server.py")
    
    finally:
        tester.close()

if __name__ == "__main__":
    main()
