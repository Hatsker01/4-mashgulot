# 🏆 Jonli Sport Natijalari Tizimi

Bu tizim UDP protokoli asosida ishlaydigan jonli sport natijalarini ko'rsatish uchun server va mijoz dasturlarini o'z ichiga oladi.

## 📁 Fayllar

- `sports_results_server.py` - Sport natijalari serveri
- `sports_results_client.py` - Sport natijalari mijoz dasturi
- `test_sports_system.py` - Tizimni test qilish dasturi
- `run_sports_system.sh` - Ishga tushirish skripti

## 🚀 Tez boshlash

### 1. Server ni ishga tushirish
```bash
python3 sports_results_server.py
```

### 2. Mijoz dasturini ishga tushirish
```bash
python3 sports_results_client.py
```

### 3. Skript orqali ishga tushirish
```bash
./run_sports_system.sh
```

## 🏆 Qo'llab-quvvatlanadigan sportlar

### ⚽ Futbol
- **O'yin**: Real Madrid vs Barcelona
- **Ma'lumotlar**: Gollar, sariq kartochkalar, qizil kartochkalar
- **Buyruq**: `futbol`

### 🏀 Basketbol
- **O'yin**: Lakers vs Warriors
- **Ma'lumotlar**: Ochkolar, faullar
- **Buyruq**: `basketbol`

### 🎾 Tennis
- **O'yin**: Djokovic vs Nadal
- **Ma'lumotlar**: Setlar, gamelar
- **Buyruq**: `tennis`

## 📱 Mijoz buyruqlari

| Buyruq | Tavsif |
|--------|--------|
| `futbol` | Futbol natijalarini ko'rish |
| `basketbol` | Basketbol natijalarini ko'rish |
| `tennis` | Tennis natijalarini ko'rish |
| `barcha` | Barcha sport natijalarini ko'rish |
| `jonli` | Jonli yangilanishlarni ko'rish |
| `statistika` | Umumiy statistika |
| `yordam` | Yordam ma'lumotlari |
| `chiqish` | Dasturdan chiqish |

## 🔄 Jonli yangilanishlar

- **Avtomatik yangilanish**: Har 5 soniyada
- **Ehtimollik**: 
  - Futbol: 30% (gollar, kartochkalar)
  - Basketbol: 40% (ochkolar, faullar)
  - Tennis: 20% (setlar, gamelar)

## 🧪 Test qilish

### Avtomatik test
```bash
python3 test_sports_system.py
```

### Qo'lda test
```bash
# Terminal 1 - Server
python3 sports_results_server.py

# Terminal 2 - Mijoz
python3 sports_results_client.py
```

## 📊 Texnik xususiyatlar

- **Protokol**: UDP
- **Port**: 9877
- **Til**: Python 3
- **Threading**: Ko'p mijozlarni qo'llab-quvvatlash
- **Real-time**: Jonli yangilanishlar
- **Logging**: Barcha faoliyat yoziladi

## 🎮 Foydalanish misollari

### 1. Oddiy foydalanish
```bash
# Server ishga tushirish
python3 sports_results_server.py

# Yangi terminalda mijoz
python3 sports_results_client.py
# Keyin: futbol, basketbol, tennis buyruqlarini kiriting
```

### 2. Avtomatik rejim
```bash
python3 sports_results_client.py
# "2" ni tanlang (Avtomatik rejim)
```

### 3. Test rejimi
```bash
# Server ishga tushirish
python3 sports_results_server.py

# Yangi terminalda test
python3 test_sports_system.py
```

## 🔧 Sozlash

### Port o'zgartirish
```python
# Server
server = SportsResultsServer(host='localhost', port=9877)

# Mijoz
client = SportsResultsClient(host='localhost', port=9877)
```

### Yangi sport qo'shish
```python
# sports_results_server.py da
self.sports_data["yangi_sport"] = {
    "Jamoa1": {"ochko": 0},
    "Jamoa2": {"ochko": 0}
}
```

## 📈 Xususiyatlar

### Server xususiyatlari
- ✅ Ko'p mijozlarni qo'llab-quvvatlash
- ✅ Jonli yangilanishlar
- ✅ Avtomatik statistika
- ✅ Thread-safe operatsiyalar
- ✅ Xatoliklarni boshqarish

### Mijoz xususiyatlari
- ✅ Interaktiv interfeys
- ✅ Avtomatik rejim
- ✅ Jonli yangilanishlarni tinglash
- ✅ Yordam tizimi
- ✅ Chiqish imkoniyati

## 🐛 Muammolarni hal qilish

### Server ishga tushmaydi
```bash
# Port bandligini tekshirish
netstat -an | grep 9877

# Boshqa port ishlatish
python3 sports_results_server.py  # Port 9877
```

### Mijoz bog'lanmaydi
```bash
# Server ishlamoqda ekanligini tekshirish
ps aux | grep sports_results_server

# Ping test
ping localhost
```

### Jonli yangilanishlar kelmaydi
- Server ishlamoqda ekanligini tekshirish
- Mijoz to'g'ri portda ekanligini tekshirish
- Firewall sozlamalarini tekshirish

## 📝 Log fayllari

Barcha faoliyat `log.txt` fayliga yoziladi:
```bash
tail -f log.txt  # Jonli loglarni ko'rish
```

## 🏆 Misollar

### Futbol natijasi
```
⚽ FUTBOL NATIJALARI ⚽
🕐 14:30:25

🏟️ Real Madrid vs Barcelona
📊 Hisob: 2 - 1

🟨 Sariq kartochkalar:
   Real Madrid: 2
   Barcelona: 1

🟥 Qizil kartochkalar:
   Real Madrid: 0
   Barcelona: 0
```

### Jonli yangilanish
```
📡 JONLI: ⚽ GOAL! Real Madrid gol urdi!
```

## 🎯 Kelajakdagi yaxshilanishlar

- [ ] Web interfeys qo'shish
- [ ] Ma'lumotlar bazasi integratsiyasi
- [ ] Real sport API bilan bog'lanish
- [ ] Push bildirishnomalar
- [ ] Statistikalar
- [ ] Chat funksiyasi
- [ ] Video stream integratsiyasi

## 📞 Yordam

Muammolar yuzaga kelsa:
1. `test_sports_system.py` ni ishga tushiring
2. Log fayllarini tekshiring
3. Port sozlamalarini tekshiring
4. Firewall qoidalarini tekshiring

---

**🏆 Sport natijalari tizimi tayyor va ishlatishga yaroqli!**
