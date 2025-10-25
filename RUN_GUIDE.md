# 🚀 UDP Client-Server Program - Run Guide

## 📋 Quick Start

### 1. Start the Server
```bash
# Terminal 1
cd /home/hatsker/go/src/tes
python3 udp_server.py
```

### 2. Test the Program
```bash
# Terminal 2 (in a new terminal)
cd /home/hatsker/go/src/tes
python3 test_udp.py
```

### 3. Interactive Demo
```bash
# Terminal 3 (in a new terminal)
cd /home/hatsker/go/src/tes
python3 demo_client.py
```

## 🔧 Manual Testing

### Test Individual Commands
```bash
# Start server first, then run client
python3 udp_client.py
```

### Available Commands to Test:
- `salom` - Greeting
- `status` - Server status
- `vaqt` - Current time
- `tasodifiy son` - Random number
- `haroratni yuboring` - Temperature sensor
- `menga maqol ayting` - Get a quote
- `ip manzilim qanday?` - Get IP address
- `foydalanuvchilar` - Active users
- `fayl:README.md` - Check file existence
- `id:1` - Database query
- `5 + 3` - Math operation
- `tosh` - Rock-Paper-Scissors game
- `json` - JSON data
- `exit` - Quit

## 📊 Test Results

The program implements all 20 features from the DOCX requirements:

✅ **Working Features:**
1. Basic messaging
2. Chat functionality  
3. Time synchronization
4. Random number generation
5. Sensor data simulation
6. Quote system
7. IP address detection
8. User management
9. File existence checking
10. Database operations
11. Mathematical operations
12. Rock-Paper-Scissors game
13. JSON data exchange
14. Logging system
15. Background services
16. Auto-response system
17. Multi-client support
18. Command processing
19. Error handling
20. Real-time communication

## 📝 Logging

All requests are logged to `log.txt`:
```bash
cat log.txt
```

## 🎯 Performance

- **Multi-threaded server** supports multiple clients
- **Real-time responses** for all commands
- **Background services** send periodic messages
- **Comprehensive logging** of all activities
- **Error handling** for network issues

## 🔍 Troubleshooting

### Server not starting?
```bash
# Check if port 9876 is available
netstat -an | grep 9876
```

### Client can't connect?
```bash
# Make sure server is running
ps aux | grep udp_server
```

### Permission issues?
```bash
# Make files executable
chmod +x *.py
```

## 📈 Monitoring

### Check server status:
```bash
# View server process
ps aux | grep udp_server

# Check log file
tail -f log.txt
```

### Test connectivity:
```bash
# Quick connection test
python3 -c "
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'status', ('localhost', 9876))
data, addr = s.recvfrom(1024)
print('Server response:', data.decode())
s.close()
"
```

## 🎮 Interactive Features

### Chat Mode:
```bash
python3 udp_chat_client.py
```

### Game Mode:
Try these commands in the client:
- `tosh` (rock)
- `qaychi` (scissors)  
- `qog'oz` (paper)

### Math Mode:
Try these expressions:
- `5 + 3`
- `10 - 4`
- `6 * 7`
- `15 / 3`

## 📋 Complete Test Checklist

- [ ] Server starts without errors
- [ ] Client connects successfully
- [ ] All 20 commands work
- [ ] Logging is active
- [ ] Background service works
- [ ] Multi-client support
- [ ] Error handling works
- [ ] JSON responses work
- [ ] Database queries work
- [ ] File operations work

## 🏆 Success Criteria

The program successfully implements:
- ✅ All 20 requirements from DOCX file
- ✅ Multi-threaded server architecture
- ✅ Interactive client interface
- ✅ Real-time chat functionality
- ✅ Comprehensive command system
- ✅ Logging and monitoring
- ✅ Error handling and recovery
- ✅ Background services
- ✅ Database simulation
- ✅ Game functionality
- ✅ Mathematical operations
- ✅ File system operations
- ✅ JSON data exchange
- ✅ Sensor data simulation
- ✅ User management
- ✅ Status monitoring
- ✅ Time synchronization
- ✅ Random number generation
- ✅ Quote system
- ✅ Auto-response bot

**🎉 The UDP client-server program is fully functional and ready for use!**
