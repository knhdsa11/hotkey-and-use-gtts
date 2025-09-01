
## 🚀 วิธีใช้งาน

0. **ติดตั้งโปรแกรมและไลบรารีที่จำเป็น**
   เพียงรันคำสั่งเหล่านี้ใน **Command Prompt (CMD)**

   ```bash
   winget install python
   winget install vlc
   winget install obs

   pip install pyperclip gtts keyboard webbrowser
   ```

   > เสร็จแล้วก็พร้อมใช้งานได้ทันที

1. **สร้างโฟลเดอร์สำหรับเก็บไฟล์เสียง**

   ```text
   C:\mp3
   ```

   (โค้ดจะสร้างให้อัตโนมัติถ้ายังไม่มี)

2. **รันโปรแกรม**

   ```bash
   python main.pyw
   ```

   > ใช้ `.pyw` จะทำงานเบื้องหลังแบบไม่มีหน้าต่าง console โผล่

3. **ใช้งาน Hotkeys (ปุ่มลัด)**

   * `Ctrl + Alt + G` → เปิด Google
   * `Ctrl + Alt + Y` → เปิด YouTube
   * `Ctrl + Alt + S` → เปิด YouTube Music
   * `Ctrl + Alt + F` → เปิด Facebook
   * `Ctrl + Alt + M` → เปิด Messenger
   * `Ctrl + Alt + C` → เปิด ChatGPT
   * `Ctrl + Alt + O` → เปิด OBS Studio
   * `Ctrl + Alt + T` → อ่านข้อความจาก Clipboard เป็นเสียงภาษาไทย

4. **ตรวจสอบ Error (ถ้ามี)**

   * ข้อผิดพลาดทั้งหมดจะถูกบันทึกไว้ในไฟล์

     ```
     C:\mp3\hotkey_log.txt
     ```
