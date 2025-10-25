#!/usr/bin/env python3
"""
Live Sports Results Server
Jonli sport natijalarini ko'rsatish uchun server
"""

import socket
import threading
import time
import random
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

class SportsResultsServer:
    def __init__(self, host='localhost', port=9877):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.connected_clients = {}
        self.running = True
        
        # Sport natijalari ma'lumotlari
        self.sports_data = {
            "futbol": {
                "Real Madrid": {"gollar": 0, "sariq_kartochka": 0, "qizil_kartochka": 0},
                "Barcelona": {"gollar": 0, "sariq_kartochka": 0, "qizil_kartochka": 0}
            },
            "basketbol": {
                "Lakers": {"ochko": 0, "faul": 0},
                "Warriors": {"ochko": 0, "faul": 0}
            },
            "tennis": {
                "Djokovic": {"set": 0, "game": 0},
                "Nadal": {"set": 0, "game": 0}
            }
        }
        
        # Live natijalar tarixi
        self.live_updates = []
        
    def start(self):
        """Server ni ishga tushirish"""
        try:
            self.socket.bind((self.host, self.port))
            print("🏆 SPORT NATIJALARI SERVERI ISHGA TUSHDI! 🏆")
            print(f"📍 Port: {self.port}")
            print("📊 Jonli sport natijalari:")
            print("   ⚽ Futbol: Real Madrid vs Barcelona")
            print("   🏀 Basketbol: Lakers vs Warriors") 
            print("   🎾 Tennis: Djokovic vs Nadal")
            print()
            print("📱 Mijozlar quyidagi buyruqlarni ishlatishi mumkin:")
            print("   - 'futbol' - Futbol natijalari")
            print("   - 'basketbol' - Basketbol natijalari")
            print("   - 'tennis' - Tennis natijalari")
            print("   - 'barcha' - Barcha sport natijalari")
            print("   - 'jonli' - Jonli yangilanishlar")
            print("   - 'statistika' - Umumiy statistika")
            print()
            
            # Jonli yangilanishlar xizmatini ishga tushirish
            self.start_live_updates()
            
            # Asosiy server loop
            while self.running:
                try:
                    data, addr = self.socket.recvfrom(1024)
                    client_message = data.decode('utf-8').strip()
                    
                    # Mijozni ro'yxatga olish
                    client_key = f"{addr[0]}:{addr[1]}"
                    self.connected_clients[client_key] = {
                        'address': addr,
                        'last_activity': time.time()
                    }
                    
                    # Xabarni alohida thread da qayta ishlash
                    threading.Thread(
                        target=self.handle_client_request,
                        args=(client_message, addr),
                        daemon=True
                    ).start()
                    
                except Exception as e:
                    if self.running:
                        print(f"❌ Xatolik: {e}")
                        
        except Exception as e:
            print(f"❌ Server ishga tushirishda xatolik: {e}")
        finally:
            self.socket.close()
    
    def handle_client_request(self, message, addr):
        """Mijoz so'rovini qayta ishlash"""
        try:
            response = self.process_sports_request(message)
            
            # Javobni mijozga yuborish
            self.socket.sendto(response.encode('utf-8'), addr)
            
            print(f"📱 Mijoz: {addr} - {message}")
            print(f"📤 Javob: {response[:100]}...")
            print()
            
        except Exception as e:
            print(f"❌ Mijoz bilan ishlashda xatolik: {e}")
    
    def process_sports_request(self, message):
        """Sport so'rovlarini qayta ishlash"""
        message_lower = message.lower()
        
        if message_lower == 'futbol':
            return self.get_football_results()
        elif message_lower == 'basketbol':
            return self.get_basketball_results()
        elif message_lower == 'tennis':
            return self.get_tennis_results()
        elif message_lower == 'barcha':
            return self.get_all_sports_results()
        elif message_lower == 'jonli':
            return self.get_live_updates()
        elif message_lower == 'statistika':
            return self.get_statistics()
        elif message_lower == 'status':
            return f"🏆 Server ishlamoqda! Faol mijozlar: {len(self.connected_clients)}"
        else:
            return "❓ Noma'lum buyruq! Quyidagilardan birini tanlang: futbol, basketbol, tennis, barcha, jonli, statistika"
    
    def get_football_results(self):
        """Futbol natijalarini olish"""
        real_madrid = self.sports_data["futbol"]["Real Madrid"]
        barcelona = self.sports_data["futbol"]["Barcelona"]
        
        result = f"""⚽ FUTBOL NATIJALARI ⚽
🕐 {datetime.now().strftime('%H:%M:%S')}

🏟️ Real Madrid vs Barcelona
📊 Hisob: {real_madrid['gollar']} - {barcelona['gollar']}

🟨 Sariq kartochkalar:
   Real Madrid: {real_madrid['sariq_kartochka']}
   Barcelona: {barcelona['sariq_kartochka']}

🟥 Qizil kartochkalar:
   Real Madrid: {real_madrid['qizil_kartochka']}
   Barcelona: {barcelona['qizil_kartochka']}"""
        
        return result
    
    def get_basketball_results(self):
        """Basketbol natijalarini olish"""
        lakers = self.sports_data["basketbol"]["Lakers"]
        warriors = self.sports_data["basketbol"]["Warriors"]
        
        result = f"""🏀 BASKETBOL NATIJALARI 🏀
🕐 {datetime.now().strftime('%H:%M:%S')}

🏟️ Lakers vs Warriors
📊 Hisob: {lakers['ochko']} - {warriors['ochko']}

📈 Faullar:
   Lakers: {lakers['faul']}
   Warriors: {warriors['faul']}"""
        
        return result
    
    def get_tennis_results(self):
        """Tennis natijalarini olish"""
        djokovic = self.sports_data["tennis"]["Djokovic"]
        nadal = self.sports_data["tennis"]["Nadal"]
        
        result = f"""🎾 TENNIS NATIJALARI 🎾
🕐 {datetime.now().strftime('%H:%M:%S')}

🏟️ Djokovic vs Nadal
📊 Set: {djokovic['set']} - {nadal['set']}
📊 Game: {djokovic['game']} - {nadal['game']}"""
        
        return result
    
    def get_all_sports_results(self):
        """Barcha sport natijalarini olish"""
        return f"""🏆 BARCHA SPORT NATIJALARI 🏆
🕐 {datetime.now().strftime('%H:%M:%S')}

{self.get_football_results()}

{self.get_basketball_results()}

{self.get_tennis_results()}"""
    
    def get_live_updates(self):
        """Jonli yangilanishlarni olish"""
        if not self.live_updates:
            return "📡 Hozircha jonli yangilanishlar yo'q"
        
        updates_text = "📡 JONLI YANGILANISHLAR 📡\n"
        for update in self.live_updates[-10:]:  # Oxirgi 10 ta yangilanish
            updates_text += f"🕐 {update['time']} - {update['message']}\n"
        
        return updates_text
    
    def get_statistics(self):
        """Umumiy statistika"""
        total_clients = len(self.connected_clients)
        total_updates = len(self.live_updates)
        
        return f"""📊 UMUMIY STATISTIKA 📊
🕐 {datetime.now().strftime('%H:%M:%S')}

👥 Faol mijozlar: {total_clients}
📡 Jonli yangilanishlar: {total_updates}
⚽ Futbol o'yinlari: 1
🏀 Basketbol o'yinlari: 1  
🎾 Tennis o'yinlari: 1

🔄 Server ishlamoqda: {self.running}"""
    
    def start_live_updates(self):
        """Jonli yangilanishlar xizmatini ishga tushirish"""
        def live_update_task():
            while self.running:
                time.sleep(5)  # Har 5 soniyada yangilanish
                
                if self.connected_clients and self.running:
                    # Tasodifiy sport natijalarini yangilash
                    self.update_sports_data()
                    
                    # Barcha mijozlarga yangilanish yuborish
                    self.broadcast_update()
        
        threading.Thread(target=live_update_task, daemon=True).start()
    
    def update_sports_data(self):
        """Sport ma'lumotlarini yangilash"""
        # Futbol yangilanishlari
        if random.random() < 0.3:  # 30% ehtimollik
            team = random.choice(["Real Madrid", "Barcelona"])
            if random.random() < 0.7:
                self.sports_data["futbol"][team]["gollar"] += 1
                self.add_live_update(f"⚽ GOAL! {team} gol urdi!")
            else:
                self.sports_data["futbol"][team]["sariq_kartochka"] += 1
                self.add_live_update(f"🟨 Sariq kartochka! {team}")
        
        # Basketbol yangilanishlari
        if random.random() < 0.4:  # 40% ehtimollik
            team = random.choice(["Lakers", "Warriors"])
            if random.random() < 0.8:
                points = random.choice([2, 3])
                self.sports_data["basketbol"][team]["ochko"] += points
                self.add_live_update(f"🏀 {team} {points} ochko oldi!")
            else:
                self.sports_data["basketbol"][team]["faul"] += 1
                self.add_live_update(f"📈 Faul! {team}")
        
        # Tennis yangilanishlari
        if random.random() < 0.2:  # 20% ehtimollik
            player = random.choice(["Djokovic", "Nadal"])
            if random.random() < 0.6:
                self.sports_data["tennis"][player]["game"] += 1
                self.add_live_update(f"🎾 {player} game oldi!")
            else:
                self.sports_data["tennis"][player]["set"] += 1
                self.add_live_update(f"🎾 {player} set oldi!")
    
    def add_live_update(self, message):
        """Jonli yangilanish qo'shish"""
        update = {
            'time': datetime.now().strftime('%H:%M:%S'),
            'message': message
        }
        self.live_updates.append(update)
        
        # Faqat oxirgi 50 ta yangilanishni saqlash
        if len(self.live_updates) > 50:
            self.live_updates = self.live_updates[-50:]
    
    def broadcast_update(self):
        """Barcha mijozlarga yangilanish yuborish"""
        if not self.live_updates:
            return
        
        latest_update = self.live_updates[-1]
        message = f"📡 JONLI: {latest_update['message']}"
        
        # Faol mijozlarni tekshirish va yangilanish yuborish
        inactive_clients = []
        for client_key, client_info in self.connected_clients.items():
            try:
                self.socket.sendto(message.encode('utf-8'), client_info['address'])
            except:
                inactive_clients.append(client_key)
        
        # Faol bo'lmagan mijozlarni o'chirish
        for client_key in inactive_clients:
            del self.connected_clients[client_key]
    
    def stop(self):
        """Serverni to'xtatish"""
        self.running = False
        self.socket.close()
        print("🛑 Sport natijalari serveri to'xtatildi!")

def main():
    """Asosiy funksiya"""
    server = SportsResultsServer()
    try:
        server.start()
    except KeyboardInterrupt:
        print("\n🛑 Server to'xtatilmoqda...")
        server.stop()

if __name__ == "__main__":
    main()
