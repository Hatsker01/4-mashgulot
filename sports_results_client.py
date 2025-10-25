#!/usr/bin/env python3
"""
Live Sports Results Client
Jonli sport natijalarini ko'rish uchun mijoz dasturi
"""

import socket
import threading
import time
from datetime import datetime

class SportsResultsClient:
    def __init__(self, host='localhost', port=9877):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.running = True
        self.connected = False
        
    def start(self):
        """Mijoz dasturini ishga tushirish"""
        print("🏆 SPORT NATIJALARI MIJOZI 🏆")
        print(f"📡 Server: {self.host}:{self.port}")
        print()
        print("📱 Mavjud buyruqlar:")
        print("   ⚽ 'futbol' - Futbol natijalari")
        print("   🏀 'basketbol' - Basketbol natijalari")
        print("   🎾 'tennis' - Tennis natijalari")
        print("   🏆 'barcha' - Barcha sport natijalari")
        print("   📡 'jonli' - Jonli yangilanishlar")
        print("   📊 'statistika' - Umumiy statistika")
        print("   ❓ 'yordam' - Yordam")
        print("   🚪 'chiqish' - Dasturdan chiqish")
        print()
        
        # Server bilan bog'lanish
        if self.connect_to_server():
            # Jonli yangilanishlarni tinglash
            self.start_live_listener()
            
            # Asosiy interaktiv loop
            self.interactive_loop()
        else:
            print("❌ Server bilan bog'lanishda xatolik!")
    
    def connect_to_server(self):
        """Server bilan bog'lanish"""
        try:
            # Test xabari yuborish
            test_message = "status"
            self.socket.sendto(test_message.encode('utf-8'), (self.host, self.port))
            
            # Javobni kutish
            self.socket.settimeout(5)  # 5 soniya timeout
            data, addr = self.socket.recvfrom(1024)
            response = data.decode('utf-8')
            
            if "Server ishlamoqda" in response:
                self.connected = True
                print("✅ Server bilan bog'landi!")
                print(f"📡 Server javobi: {response}")
                print()
                return True
            else:
                print("❌ Server javob bermadi!")
                return False
                
        except Exception as e:
            print(f"❌ Bog'lanishda xatolik: {e}")
            return False
    
    def start_live_listener(self):
        """Jonli yangilanishlarni tinglash"""
        def live_listener():
            while self.running and self.connected:
                try:
                    self.socket.settimeout(1)  # 1 soniya timeout
                    data, addr = self.socket.recvfrom(1024)
                    message = data.decode('utf-8')
                    
                    # Jonli yangilanishlarni ko'rsatish
                    if "📡 JONLI:" in message:
                        print(f"\n🔥 {message}")
                        print("💬 Buyruq kiriting (yordam uchun 'yordam'): ", end="", flush=True)
                    
                except socket.timeout:
                    continue
                except Exception as e:
                    if self.running:
                        print(f"❌ Jonli tinglashda xatolik: {e}")
                    break
        
        threading.Thread(target=live_listener, daemon=True).start()
    
    def interactive_loop(self):
        """Interaktiv foydalanish loop"""
        while self.running and self.connected:
            try:
                user_input = input("💬 Buyruq kiriting: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['chiqish', 'exit', 'quit']:
                    print("🚪 Dasturdan chiqilmoqda...")
                    break
                
                if user_input.lower() == 'yordam':
                    self.show_help()
                    continue
                
                # Serverga so'rov yuborish
                response = self.send_request(user_input)
                if response:
                    print(f"\n📊 SERVERDAN:")
                    print("=" * 50)
                    print(response)
                    print("=" * 50)
                    print()
                
            except KeyboardInterrupt:
                print("\n🚪 Dasturdan chiqilmoqda...")
                break
            except Exception as e:
                print(f"❌ Xatolik: {e}")
        
        self.cleanup()
    
    def send_request(self, message):
        """Serverga so'rov yuborish va javob olish"""
        try:
            # So'rovni yuborish
            self.socket.sendto(message.encode('utf-8'), (self.host, self.port))
            
            # Javobni kutish
            self.socket.settimeout(10)  # 10 soniya timeout
            data, addr = self.socket.recvfrom(1024)
            response = data.decode('utf-8')
            
            return response
            
        except socket.timeout:
            print("⏰ Server javob bermadi! Qayta urinib ko'ring.")
            return None
        except Exception as e:
            print(f"❌ So'rov yuborishda xatolik: {e}")
            return None
    
    def show_help(self):
        """Yordam ma'lumotlarini ko'rsatish"""
        help_text = """
🏆 SPORT NATIJALARI MIJOZI - YORDAM 🏆

📱 Mavjud buyruqlar:
   ⚽ futbol      - Futbol natijalarini ko'rish
   🏀 basketbol   - Basketbol natijalarini ko'rish  
   🎾 tennis      - Tennis natijalarini ko'rish
   🏆 barcha      - Barcha sport natijalarini ko'rish
   📡 jonli       - Jonli yangilanishlarni ko'rish
   📊 statistika  - Umumiy statistika
   ❓ yordam      - Bu yordam sahifasi
   🚪 chiqish     - Dasturdan chiqish

💡 Maslahatlar:
   • Jonli yangilanishlar avtomatik ko'rsatiladi
   • Har 5 soniyada yangi ma'lumotlar keladi
   • 'barcha' buyrug'i barcha sport natijalarini ko'rsatadi
   • 'jonli' buyrug'i oxirgi yangilanishlarni ko'rsatadi

🏆 Qo'llab-quvvatlanadigan sportlar:
   ⚽ Futbol: Real Madrid vs Barcelona
   🏀 Basketbol: Lakers vs Warriors
   🎾 Tennis: Djokovic vs Nadal
"""
        print(help_text)
    
    def cleanup(self):
        """Tozalash ishlari"""
        self.running = False
        self.connected = False
        self.socket.close()
        print("✅ Mijoz dasturi to'xtatildi!")

class AutoSportsClient:
    """Avtomatik sport natijalarini kuzatuvchi mijoz"""
    
    def __init__(self, host='localhost', port=9877):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.running = True
        
    def start_auto_mode(self):
        """Avtomatik rejimni ishga tushirish"""
        print("🤖 AVTOMATIK SPORT NATIJALARI KUZATUVCHISI 🤖")
        print(f"📡 Server: {self.host}:{self.port}")
        print("🔄 Avtomatik rejimda ishlaydi...")
        print("⏹️  To'xtatish uchun Ctrl+C bosing")
        print()
        
        try:
            while self.running:
                # Har 10 soniyada barcha natijalarni so'rash
                response = self.get_all_results()
                if response:
                    print(f"🕐 {datetime.now().strftime('%H:%M:%S')}")
                    print("=" * 60)
                    print(response)
                    print("=" * 60)
                    print()
                
                time.sleep(10)  # 10 soniya kutish
                
        except KeyboardInterrupt:
            print("\n🛑 Avtomatik rejim to'xtatildi!")
        finally:
            self.socket.close()
    
    def get_all_results(self):
        """Barcha natijalarni olish"""
        try:
            self.socket.sendto("barcha".encode('utf-8'), (self.host, self.port))
            self.socket.settimeout(5)
            data, addr = self.socket.recvfrom(1024)
            return data.decode('utf-8')
        except:
            return None

def main():
    """Asosiy funksiya"""
    print("🏆 SPORT NATIJALARI MIJOZI 🏆")
    print("1. Interaktiv rejim")
    print("2. Avtomatik rejim")
    print()
    
    try:
        choice = input("Rejimni tanlang (1/2): ").strip()
        
        if choice == "1":
            client = SportsResultsClient()
            client.start()
        elif choice == "2":
            auto_client = AutoSportsClient()
            auto_client.start_auto_mode()
        else:
            print("❌ Noto'g'ri tanlov!")
            
    except KeyboardInterrupt:
        print("\n🛑 Dastur to'xtatildi!")
    except Exception as e:
        print(f"❌ Xatolik: {e}")

if __name__ == "__main__":
    main()
