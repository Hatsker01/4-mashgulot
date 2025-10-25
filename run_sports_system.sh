#!/bin/bash
# Sport natijalari tizimini ishga tushirish skripti

echo "🏆 SPORT NATIJALARI TIZIMI 🏆"
echo "================================"
echo ""

# Fayllarni executable qilish
chmod +x sports_results_server.py
chmod +x sports_results_client.py
chmod +x test_sports_system.py

echo "📋 Mavjud buyruqlar:"
echo "1. Server ni ishga tushirish"
echo "2. Mijoz dasturini ishga tushirish"
echo "3. Test dasturini ishga tushirish"
echo "4. Barcha fayllarni ko'rish"
echo "5. Chiqish"
echo ""

while true; do
    read -p "Tanlovni kiriting (1-5): " choice
    
    case $choice in
        1)
            echo "🚀 Server ishga tushmoqda..."
            echo "⚠️  Server to'xtatish uchun Ctrl+C bosing"
            echo ""
            python3 sports_results_server.py
            ;;
        2)
            echo "📱 Mijoz dasturi ishga tushmoqda..."
            echo "⚠️  Dastur to'xtatish uchun Ctrl+C bosing"
            echo ""
            python3 sports_results_client.py
            ;;
        3)
            echo "🧪 Test dasturi ishga tushmoqda..."
            echo "⚠️  Test to'xtatish uchun Ctrl+C bosing"
            echo ""
            python3 test_sports_system.py
            ;;
        4)
            echo "📁 Fayllar ro'yxati:"
            ls -la *.py | grep sports
            echo ""
            ;;
        5)
            echo "🚪 Chiqilmoqda..."
            exit 0
            ;;
        *)
            echo "❌ Noto'g'ri tanlov! 1-5 orasida tanlang."
            echo ""
            ;;
    esac
done
