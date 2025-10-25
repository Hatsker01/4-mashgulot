#!/bin/bash

# UDP Client-Server Compilation and Execution Script
# This script compiles and runs the UDP networking programs

echo "=== UDP Client-Server Dasturlarini Compile qilish va ishga tushirish ==="
echo

# Create udp package directory if it doesn't exist
mkdir -p udp

# Move Java files to udp package directory
if [ -f "UDPServer.java" ]; then
    mv UDPServer.java udp/
    echo "UDPServer.java -> udp/UDPServer.java"
fi

if [ -f "UDPClient.java" ]; then
    mv UDPClient.java udp/
    echo "UDPClient.java -> udp/UDPClient.java"
fi

if [ -f "UDPChatClient.java" ]; then
    mv UDPChatClient.java udp/
    echo "UDPChatClient.java -> udp/UDPChatClient.java"
fi

echo
echo "=== Compile qilish ==="

# Compile all Java files
javac udp/*.java

if [ $? -eq 0 ]; then
    echo "✅ Barcha fayllar muvaffaqiyatli compile qilindi!"
    echo
    
    echo "=== Dasturlarni ishga tushirish bo'yicha yo'riqnoma ==="
    echo
    echo "1. Server ni ishga tushirish:"
    echo "   java udp.UDPServer"
    echo
    echo "2. Oddiy Client ni ishga tushirish:"
    echo "   java udp.UDPClient"
    echo
    echo "3. Chat Client ni ishga tushirish:"
    echo "   java udp.UDPChatClient"
    echo
    echo "=== Mavjud xizmatlar ==="
    echo "• Oddiy xabar yuborish va qabul qilish"
    echo "• Chat dasturi (real vaqtda)"
    echo "• Matematik amallar (5 + 3)"
    echo "• Fayl mavjudligini tekshirish (fayl:filename.txt)"
    echo "• Tasodifiy son generatsiya"
    echo "• Sensor ma'lumotlari (harorat)"
    echo "• Ma'lumotlar bazasi bilan ishlash (id:1)"
    echo "• O'yin (Tosh-Qaychi-Qog'oz)"
    echo "• JSON formatda ma'lumot"
    echo "• Server holatini tekshirish"
    echo "• IP manzilni aniqlash"
    echo "• Vaqt sinxronizatsiyasi"
    echo "• Log yozish tizimi"
    echo "• Background xizmat"
    echo
    echo "=== Foydalanish ==="
    echo "1. Birinchi terminalda server ni ishga tushiring"
    echo "2. Ikkinchi terminalda client ni ishga tushiring"
    echo "3. Xabarlar yuboring va javoblarni oling"
    echo
    echo "Server ishga tushirish uchun quyidagi buyruqni bajaring:"
    echo "java udp.UDPServer"
    
else
    echo "❌ Compile jarayonida xatolik yuz berdi!"
    echo "Xatoliklarni tekshiring va qayta urinib ko'ring."
fi
