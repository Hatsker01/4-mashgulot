#!/usr/bin/env python3
"""
UDP Chat Client for real-time messaging
Implements chat functionality from project requirements
"""

import socket
import threading
import sys

class UDPChatClient:
    def __init__(self, host='localhost', port=9876):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.running = True
        
    def start(self):
        """Start the UDP chat client"""
        print("=== UDP Chat Client ===")
        print(f"Server: {self.host}:{self.port}")
        print("Chat dasturi ishga tushdi!")
        print("Xabarlarni yuboring (chiqish uchun 'exit' yozing):")
        print()
        
        # Start listening for messages in a separate thread
        listener_thread = threading.Thread(target=self.listen_for_messages, daemon=True)
        listener_thread.start()
        
        # Main chat loop
        while self.running:
            try:
                user_input = input("Siz: ").strip()
                
                if user_input.lower() == 'exit':
                    print("Chatdan chiqilmoqda...")
                    self.running = False
                    break
                
                if not user_input:
                    continue
                
                # Send message to server
                self.socket.sendto(user_input.encode('utf-8'), (self.host, self.port))
                
            except KeyboardInterrupt:
                print("\nChatdan chiqilmoqda...")
                self.running = False
                break
            except Exception as e:
                print(f"Xatolik: {e}")
        
        self.socket.close()
    
    def listen_for_messages(self):
        """Listen for incoming messages from server"""
        while self.running:
            try:
                data, addr = self.socket.recvfrom(1024)
                message = data.decode('utf-8')
                print(f"<< {message}")
            except Exception as e:
                if self.running:
                    print(f"Xabar olishda xatolik: {e}")
                break

def main():
    """Main function to start the chat client"""
    client = UDPChatClient()
    try:
        client.start()
    except KeyboardInterrupt:
        print("\nChat client to'xtatilmoqda...")

if __name__ == "__main__":
    main()
