#!/usr/bin/env python3
"""
Interactive demo client for UDP server
Shows how to use the client interactively
"""

import socket
import sys

def demo_client():
    """Demo the interactive client"""
    print("=== UDP Client Demo ===")
    print("Server bilan bog'lanish...")
    
    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 9876)
    
    try:
        # Test connection
        test_message = "status"
        client_socket.sendto(test_message.encode('utf-8'), server_address)
        data, addr = client_socket.recvfrom(1024)
        response = data.decode('utf-8')
        
        if "Server ishlamoqda" in response:
            print("✅ Server bilan bog'lanish muvaffaqiyatli!")
            print(f"Server javobi: {response}")
            print()
            
            # Interactive demo
            print("=== Interaktiv Demo ===")
            print("Quyidagi buyruqlarni sinab ko'ring:")
            print("- salom")
            print("- vaqt") 
            print("- tasodifiy son")
            print("- 5 + 3")
            print("- tosh")
            print("- json")
            print("- exit (chiqish)")
            print()
            
            while True:
                try:
                    user_input = input("Xabar yuboring: ").strip()
                    
                    if user_input.lower() == 'exit':
                        print("Demo tugadi!")
                        break
                    
                    if not user_input:
                        continue
                    
                    # Send message
                    client_socket.sendto(user_input.encode('utf-8'), server_address)
                    
                    # Receive response
                    data, addr = client_socket.recvfrom(1024)
                    response = data.decode('utf-8')
                    
                    print(f"SERVERDAN: {response}")
                    print()
                    
                except KeyboardInterrupt:
                    print("\nDemo to'xtatildi!")
                    break
                except Exception as e:
                    print(f"Xatolik: {e}")
                    
    except Exception as e:
        print(f"❌ Server bilan bog'lanishda xatolik: {e}")
        print("Iltimos, server ni ishga tushiring:")
        print("python3 udp_server.py")
    
    finally:
        client_socket.close()

if __name__ == "__main__":
    demo_client()
