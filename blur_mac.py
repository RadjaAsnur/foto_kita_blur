import cv2
import mediapipe as mp
import numpy as np

# 1. IMPOR SESUAI DENGAN NOTEBOOK RESMI GOOGLE
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Fungsi memeriksa apakah posisi jari tegak ke atas
def finger_up(tip_idx, pip_idx, landmarks):
    return landmarks[tip_idx].y < landmarks[pip_idx].y

# Fungsi mendeteksi gestur Peace (Dua Jari)
def is_peace(landmarks):
    index_up = finger_up(8, 6, landmarks)
    middle_up = finger_up(12, 10, landmarks)
    ring_up = finger_up(16, 14, landmarks)
    pinky_up = finger_up(20, 18, landmarks)

    return (
        index_up
        and middle_up
        and not ring_up
        and not pinky_up
    )

# 2. INISIALISASI BERDASARKAN STRUKTUR GOOGLE TASKS API
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')

# Menggunakan mode VIDEO agar optimal memproses frame kamera real-time
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO,
    num_hands=1,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5
)

# Membuka Kamera Laptop
cap = cv2.VideoCapture(0)

# Variabel pembantu untuk memastikan timestamp selalu meningkat (Cara A)
last_timestamp_ms = -1

# Membuat objek detector
with vision.HandLandmarker.create_from_options(options) as detector:
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Konversi frame array ke format objek MediaPipe Image
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        
        # === PERBAIKAN TIMESTAMPS (CARA A) ===
        # Ambil posisi waktu frame saat ini dari properti OpenCV
        current_timestamp_ms = int(cap.get(cv2.CAP_PROP_POS_MSEC))
        
        # Jika webcam mengembalikan nilai 0 atau tidak bergerak, hitung berdasarkan tick count sistem
        if current_timestamp_ms <= 0:
            current_timestamp_ms = int(cv2.getTickCount() / cv2.getTickFrequency() * 1000)
            
        # Validasi krusial: Pastikan timestamp baru LEBIH BESAR dari timestamp sebelumnya
        if current_timestamp_ms <= last_timestamp_ms:
            current_timestamp_ms = last_timestamp_ms + 1
            
        # Simpan timestamp saat ini untuk pengecekan di frame berikutnya
        last_timestamp_ms = current_timestamp_ms
        # =====================================

        # Proses deteksi tangan dari objek detector
        detection_result = detector.detect_for_video(mp_image, current_timestamp_ms)

        peace_detected = False

        # Membaca hasil deteksi koordinat jari tangan
        if detection_result.hand_landmarks:
            for hand_landmarks in detection_result.hand_landmarks:
                if is_peace(hand_landmarks):
                    peace_detected = True
                    break

        # 3. IMPLEMENTASI EFEK BLUR
        if peace_detected:
            frame = cv2.GaussianBlur(frame, (61, 61), 0)

        cv2.imshow("Peace Blur (Tasks API)", frame)

        # Tekan ESC untuk keluar
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
