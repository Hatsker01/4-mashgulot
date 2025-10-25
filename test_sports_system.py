#!/usr/bin/env python3
"""
Sport natijalari tizimini test qilish uchun dastur
"""

import socket
import time
import threading
from datetime import datetime

def test_server_connection():
    """Server bilan bog'lanishni test qilish"""
    print("🧪 SERVER BOG'LANISHINI TEST QILISH")
    print("=" * 50)
    
    try:
        # Test socket yaratish
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        test_socket.settimeout(5)
        
        # Test xabari yuborish
        test_message = "status"
        test_socket.sendto(test_message.encode('utf-8'), ('localhost', 9877))
        
        # Javobni kutish
        data, addr = test_socket.recvfrom(1024)
        response = data.decode('utf-8')
        
        print(f"✅ Server javobi: {response}")
        test_socket.close()
        return True
        
    except Exception as e:
        print(f"❌ Bog'lanishda xatolik: {e}")
        return False

def test_sports_commands():
    """Sport buyruqlarini test qilish"""
    print("\n🧪 SPORT BUYRUQLARINI TEST QILISH")
    print("=" * 50)
    
    commands = [
        "futbol",
        "basketbol", 
        "tennis",
        "barcha",
        "jonli",
        "statistika"
    ]
    
    try:
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        test_socket.settimeout(3)
        
        for i, command in enumerate(commands, 1):
            print(f"📤 {i}. {command} buyrug'ini yuborish...")
            
            test_socket.sendto(command.encode('utf-8'), ('localhost', 9877))
            data, addr = test_socket.recvfrom(1024)
            response = data.decode('utf-8')
            
            print(f"📥 Javob uzunligi: {len(response)} belgi")
            print(f"📊 Javob: {response[:100]}...")
            print()
            
            time.sleep(1)  # 1 soniya kutish
        
        test_socket.close()
        return True
        
    except Exception as e:
        print(f"❌ Buyruqlarni test qilishda xatolik: {e}")
        return False

def test_live_updates():
    """Jonli yangilanishlarni test qilish"""
    print("\n🧪 JONLI YANGILANISHLARNI TEST QILISH")
    print("=" * 50)
    
    try:
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        test_socket.settimeout(2)
        
        print("📡 10 soniya davomida jonli yangilanishlarni kuzatish...")
        
        for i in range(10):
            try:
                test_socket.sendto("jonli".encode('utf-8'), ('localhost', 9877))
                data, addr = test_socket.recvfrom(1024)
                response = data.decode('utf-8')
                
                if "📡 JONLI YANGILANISHLAR" in response:
                    print(f"✅ {i+1}. Jonli yangilanishlar mavjud")
                else:
                    print(f"📊 {i+1}. Yangilanishlar: {response[:50]}...")
                
            except socket.timeout:
                print(f"⏰ {i+1}. Timeout - yangilanish yo'q")
            
            time.sleep(1)
        
        test_socket.close()
        return True
        
    except Exception as e:
        print(f"❌ Jonli yangilanishlarni test qilishda xatolik: {e}")
        return False

def run_comprehensive_test():
    """Keng qamrovli test"""
    print("🏆 SPORT NATIJALARI TIZIMI - KENG QAMROVLI TEST")
    print("=" * 60)
    print(f"🕐 Test vaqti: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Test natijalari
    tests = [
        ("Server bog'lanishi", test_server_connection),
        ("Sport buyruqlari", test_sports_commands),
        ("Jonli yangilanishlar", test_live_updates)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"🔄 {test_name} testini bajarish...")
        try:
            result = test_func()
            results.append((test_name, result))
            if result:
                print(f"✅ {test_name} - MUVOFFAQIYATLI!")
            else:
                print(f"❌ {test_name} - XATOLIK!")
        except Exception as e:
            print(f"❌ {test_name} - XATOLIK: {e}")
            results.append((test_name, False))
        
        print()
    
    # Umumiy natija
    print("📊 UMUMIY TEST NATIJALARI")
    print("=" * 30)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ MUVOFFAQIYATLI" if result else "❌ XATOLIK"
        print(f"{test_name}: {status}")
    
    print(f"\n🏆 Umumiy natija: {passed}/{total} test muvaffaqiyatli!")
    
    if passed == total:
        print("🎉 Barcha testlar muvaffaqiyatli o'tdi!")
    else:
        print("⚠️  Ba'zi testlarda xatoliklar bor!")

def main():
    """Asosiy funksiya"""
    print("🏆 SPORT NATIJALARI TIZIMI - TEST DASTURI")
    print("=" * 50)
    print()
    print("⚠️  DIQQAT: Test ishga tushishdan oldin serverni ishga tushiring!")
    print("   python3 sports_results_server.py")
    print()
    
    input("Server ishga tushganini tasdiqlang va Enter bosing...")
    print()
    
    try:
        run_comprehensive_test()
    except KeyboardInterrupt:
        print("\n🛑 Test to'xtatildi!")
    except Exception as e:
        print(f"❌ Testda xatolik: {e}")

if __name__ == "__main__":
    main()
