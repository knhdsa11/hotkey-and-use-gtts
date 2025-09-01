โอเคครับ งั้นผมจะสรุปเป็น **วิธีใช้งาน (Usage)** สำหรับใส่ใน GitHub README ให้เลยนะครับ 👇

---

## 🚀 วิธีใช้งาน

1. **ติดตั้ง Python**

   * แนะนำ Python 3.10+
   * ดาวน์โหลดจาก [python.org](https://www.python.org/downloads/)

2. **ติดตั้งไลบรารีที่ต้องใช้**

   ```bash
   pip install gtts pyperclip keyboard
   ```

3. **ติดตั้ง VLC Media Player**

   * ดาวน์โหลดจาก [videolan.org](https://www.videolan.org/vlc/)
   * แก้ไขตัวแปร `VLC_EXE` ในโค้ดให้ตรงกับตำแหน่ง `vlc.exe` ในเครื่องคุณ

     ```python
     VLC_EXE = r"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
     ```

4. **สร้างโฟลเดอร์สำหรับเก็บไฟล์เสียง**

   ```text
   C:\mp3
   ```

   (โค้ดจะสร้างให้อัตโนมัติถ้ายังไม่มี)

5. **รันโปรแกรม**

   ```bash
   python main.pyw
   ```

   > ใช้ `.pyw` จะทำงานเบื้องหลังแบบไม่มีหน้าต่าง console โผล่

6. **ใช้งาน Hotkeys**

   * `Ctrl + Alt + G` → เปิด Google
   * `Ctrl + Alt + Y` → เปิด YouTube
   * `Ctrl + Alt + S` → เปิด YouTube Music
   * `Ctrl + Alt + F` → เปิด Facebook
   * `Ctrl + Alt + M` → เปิด Messenger
   * `Ctrl + Alt + C` → เปิด ChatGPT
   * `Ctrl + Alt + O` → เปิด OBS Studio
   * `Ctrl + Alt + T` → อ่าน Clipboard เป็นเสียงภาษาไทย

7. **ตรวจสอบ Error (ถ้ามี)**

   * ข้อผิดพลาดทั้งหมดจะถูกบันทึกไว้ในไฟล์

     ```
     C:\mp3\hotkey_log.txt
     ```

---

คุณอยากให้ผมจัดให้เป็น **README.md** ไฟล์พร้อมใส่ GitHub ได้เลยมั้ยครับ?
