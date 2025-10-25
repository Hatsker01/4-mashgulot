# UDP Client-Server Networking Project

Bu loyiha DOCX fayldagi talablarga asosan yaratilgan UDP protokoli asosida ishlovchi client-server dasturlar to'plamidir.

## Loyiha tarkibi

### Asosiy fayllar:
- `udp/UDPServer.java` - UDP Server dasturi
- `udp/UDPClient.java` - Oddiy UDP Client dasturi  
- `udp/UDPChatClient.java` - Chat uchun UDP Client
- `compile_and_run.sh` - Compile va ishga tushirish skripti

## Xususiyatlar

### 1. Oddiy xabar yuborish va qabul qilish
- Client serverga xabar yuboradi
- Server javob qaytaradi

### 2. Chat dasturi (Real vaqtda)
- Ikki foydalanuvchi o'rtasida xabar almashish
- Real vaqtda xabarlar almashinuvi

### 3. Matematik amallar
- Qo'shish: `5 + 3`
- Ayirish: `10 - 4`
- Ko'paytirish: `6 * 7`
- Bo'lish: `15 / 3`

### 4. Fayl mavjudligini tekshirish
- `fayl:filename.txt` - Fayl mavjudligini tekshirish

### 5. Tasodifiy son generatsiya
- `tasodifiy son` - 1-100 oralig'ida tasodifiy son

### 6. Sensor ma'lumotlari
- `haroratni yuboring` - Harorat ma'lumotini olish

### 7. Ma'lumotlar bazasi bilan ishlash
- `id:1` - ID bo'yicha ma'lumot olish
- `id:2` - Boshqa ID uchun ma'lumot

### 8. O'yin (Tosh-Qaychi-Qog'oz)
- `tosh` - Tosh tanlash
- `qaychi` - Qaychi tanlash  
- `qog'oz` - Qog'oz tanlash

### 9. JSON formatda ma'lumot
- `json` - JSON formatda ma'lumot olish

### 10. Server holatini tekshirish
- `status` - Server holatini ko'rish
- `foydalanuvchilar` - Faol foydalanuvchilar soni

### 11. IP manzilni aniqlash
- `ip manzilim qanday?` - IP manzilni olish

### 12. Vaqt sinxronizatsiyasi
- `vaqt` - Hozirgi vaqtni olish

### 13. Log yozish tizimi
- Har bir so'rov `log.txt` fayliga yoziladi

### 14. Background xizmat
- Server har 10 soniyada barcha foydalanuvchilarga xabar yuboradi

### 15. Maqol olish
- `menga maqol ayting` - Maqol olish

## O'rnatish va ishga tushirish

### 1. Compile qilish
```bash
./compile_and_run.sh
```

### 2. Server ni ishga tushirish
```bash
java udp.UDPServer
```

### 3. Client ni ishga tushirish
```bash
# Oddiy client
java udp.UDPClient

# Chat client
java udp.UDPChatClient
```

## Foydalanish misollari

### Server ishga tushirish:
```bash
java udp.UDPServer
```

### Client ishga tushirish:
```bash
java udp.UDPClient
```

### Mavjud buyruqlar:
- `salom` - Server bilan salomlashish
- `status` - Server holatini tekshirish
- `vaqt` - Hozirgi vaqtni olish
- `tasodifiy son` - Tasodifiy son olish
- `haroratni yuboring` - Sensor ma'lumoti
- `menga maqol ayting` - Maqol olish
- `ip manzilim qanday?` - IP manzilni olish
- `foydalanuvchilar` - Faol foydalanuvchilar
- `fayl:filename.txt` - Fayl mavjudligini tekshirish
- `id:1` - Ma'lumotlar bazasidan ma'lumot
- `tosh/qaychi/qog'oz` - O'yin
- `5 + 3` - Matematik amal
- `json` - JSON formatda ma'lumot
- `exit` - Dasturdan chiqish

## Texnik xususiyatlar

- **Port**: 9876
- **Protokol**: UDP
- **Til**: Java
- **Buffer hajmi**: 1024 bayt
- **Log fayli**: log.txt
- **Ma'lumotlar bazasi**: In-memory HashMap

## Loyiha talablari

Bu loyiha DOCX fayldagi 20 ta vazifadan quyidagilarni amalga oshiradi:

1. ✅ UDP orqali xabar yuborish va qabul qilish
2. ✅ Oddiy chat dasturi yaratish
3. ✅ Serverga so'rov jo'natish
4. ✅ UDP orqali matnli buyruqlar tizimi
5. ✅ UDP orqali vaqt sinxronizatsiyasi
6. ✅ Parallel kliyentlarni qo'llab-quvvatlash
7. ✅ UDP orqali matematik amal bajarish
8. ✅ UDP orqali fayl nomlarini jo'natish
9. ✅ UDP orqali tasodifiy son jo'natish
10. ✅ UDP orqali holat tekshirish tizimi
11. ✅ UDP orqali IP-manzilni aniqlash
12. ✅ UDP orqali foydalanuvchi ro'yxatini ko'rish
13. ✅ UDP orqali log yozish tizimi
14. ✅ UDP orqali JSON formatda ma'lumot jo'natish
15. ✅ UDP orqali o'yin dasturi (Tosh-Qaychi-Qog'oz)
16. ✅ UDP orqali ma'lumotlar bazasi bilan ishlash
17. ✅ UDP orqali fon xizmat yaratish
18. ✅ UDP orqali sensor ma'lumotlarini jo'natish
19. ✅ UDP orqali avtomatik javob beruvchi bot
20. ✅ UDP orqali maqolni qaytaruvchi server

## Muallif

Bu loyiha DOCX fayldagi talablarga asosan yaratilgan va barcha asosiy xususiyatlarni qo'llab-quvvatlaydi.