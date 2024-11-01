
# 🤖 AI Trợ Lý Ảo (VocoBot)

## 📝 Giới thiệu
AI Trợ Lý Ảo là dự án chatbot AI có khả năng nhắn tin và giao tiếp qua giao diện đồ họa, được thiết kế nhằm nghiên cứu xử lý ngôn ngữ tự nhiên và phản hồi giọng nói.

## 📂 Cấu trúc dự án
- **ai_bot.py**: Tập lệnh chính cho logic chatbot.
- **ai_chuc_nang.py**: Các chức năng phụ trợ.
- **train.py**: Đào tạo mô hình dựa trên dữ liệu intents.json.
- **gui_ai_tinker.py**: Giao diện đồ họa người dùng sử dụng tkinter.
- **data.pth**: Trọng số của mô hình sau khi đào tạo.
- **intents.json**: Tập dữ liệu cho các câu hỏi và phản hồi.
- **nltk_utils.py**: Các hàm xử lý ngôn ngữ tự nhiên (NLTK).

## 🚀 Tính năng chính
- Nhắn tin và Giao tiếp bằng giọng nói.
- Học máy: Huấn luyện mô hình sử dụng PyTorch.
- Giao diện đồ họa: Đơn giản, dễ sử dụng.

## 🔧 Công nghệ sử dụng
- **Ngôn ngữ**: Python
- **Xử lý ngôn ngữ tự nhiên**: NLTK, PyTorch
- **Giao diện**: Tkinter

## 📦 Cài đặt
1. **Clone dự án**
   ```bash
   git clone https://github.com/Zeta23D/AI_TRO_LY_AO.git
   cd AI_TRO_LY_AO
   ```

2. **Cài đặt các package phụ thuộc**
   ```bash
   pip install -r requirements.txt
   ```

3. **Huấn luyện mô hình**
   ```bash
   python train.py
   ```

## 📈 Sử dụng
Chạy tập lệnh GUI để khởi động chatbot:
```bash
python gui_ai_tinker.py
```

## 💡 Đóng góp
Đóng góp ý tưởng qua **fork** và pull request để phát triển dự án thêm!
