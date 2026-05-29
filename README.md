# Flower Recognition – Nhận diện hoa real-time

Dự án nhận diện hoa real-time qua webcam sử dụng TensorFlow/Keras. Model có thể phân loại 5 loại hoa: Daisy, Dandelion, Rose, Sunflower, Tulip.
## Thực hiện bởi nhóm [HKT] học phần Trí tuệ nhân tạo tại UEH
1. Nguyễn Bảo Hân - 31251027458
2. Trần Thế Đăng Khoa - 31251020280
3. Hoàng Bảo Trân - 31251020280
---

## Cấu trúc project

```
├── flowersrecogmain.py       # Script nhận diện real-time qua webcam
├── flowersrecog.keras        # File model (tải riêng, xem bên dưới)
└── README.md
```

File model (`flowersrecog.keras`) không được lưu trong repo do giới hạn GitHub. Tải về theo hướng dẫn bên dưới.

---

## Tải model về

Model được lưu trên Google Drive: **https://drive.google.com/file/d/1SBdUESOYwN5Cj1W1ASLDXg74zUaNToo4/view?usp=sharing**

Tải file `flowersrecog.keras` về và đặt cùng thư mục với `flowersrecogmain.py`.

---

## Cách chạy

### 1. Clone repo

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2. Cài thư viện

```bash
pip install tensorflow keras opencv-python numpy
```

### 3. Chạy

```bash
python flowersrecogmain.py
```

Đưa hoa vào trước webcam, kết quả hiện trực tiếp trên màn hình. Bấm phím `Q` để thoát.

---

## Hướng dẫn chỉnh sửa

### Thay đường dẫn model

Mở `flowersrecogmain.py`, tìm dòng:

```python
MODEL_PATH = "flowersrecog.keras"
```

Thay bằng đường dẫn đầy đủ nếu để model ở thư mục khác, ví dụ:

```python
MODEL_PATH = "C:/Users/ten/Downloads/flowersrecog.keras"
```

### Điều chỉnh ngưỡng confidence

Mặc định hiện "Chua xac dinh duoc" khi confidence dưới 80%. Tìm dòng:

```python
if confidence < 80:
```

Tăng lên (ví dụ 90) nếu hay nhận diện sai, giảm xuống (ví dụ 60) nếu hay hiện "Chua xac dinh duoc" dù ảnh rõ.

### Thêm loại hoa mới

Nếu train lại model với nhiều loại hoa hơn, cập nhật dict `CLASS_LABELS`:

```python
CLASS_LABELS = {
    0: "Daisy",
    1: "Dandelion",
    2: "Rose",
    3: "Sunflower",
    4: "Tulip",
    5: "TenHoaMoi"   # thêm vào đây
}
```

Thứ tự số phải khớp với thứ tự class lúc train.

---

## Các loại hoa nhận diện được

- Daisy
- Dandelion
- Rose
- Sunflower
- Tulip

---

## Yêu cầu hệ thống

- Python 3.8+
- Webcam
- Windows / macOS / Linux

## Link video DEMO: https://youtu.be/X-3oSJr3_o0
