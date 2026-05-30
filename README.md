# SnapClass

SnapClass is a Streamlit-based automated classroom attendance system. It streamlines the roll-call process for teachers by combining face recognition, voice verification, and dynamic QR code generation.

## 🌟 Key Features

*   **Teacher Dashboard:** Create virtual classrooms and generate unique session QR codes.
*   **Face Recognition:** Capture student images and verify identity using the `dlib` library.
*   **Voice Attendance:** Log attendance using voice biometric processing.
*   **Real-time Processing:** Smooth user interface powered entirely by Streamlit.

## 🛠️ Tech Stack

*   **Frontend & Dashboard:** Streamlit
*   **Face Detection & Recognition:** dlib, OpenCV, face_recognition
*   **Audio Processing:** SpeechRecognition / SoundFile (or your specific voice library)
*   **QR Code Generation:** qrcode

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed. You also need a C++ compiler (like CMake) installed on your system to build the `dlib` library.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd snapclass
   ```

2. **Install system dependencies (Required for dlib):**
   * **Ubuntu/Debian:** `sudo apt-get install build-essential cmake libopenblas-dev libx11-dev`
   * **macOS:** `brew install cmake xquartz`
   * **Windows:** Install Visual Studio with "Desktop development with C++"

3. **Install Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Launch the Streamlit server from your terminal:
```bash
streamlit run app.py
```

## 📋 How It Works

1. **Classroom Creation:** The teacher logs in, creates a class session, and displays the generated QR code on the classroom screen.
2. **Student Scanning:** Students scan the QR code to access the attendance portal on their devices.
3. **Verification:** The portal prompts the student to capture a live selfie (processed via `dlib`) and record a short voice sample.
4. **Logging:** Once both biometrics match the registered database, attendance is marked successfully.

## 📂 Project Structure

```text
├── app.py                 # Main Streamlit application entry point
├── database/              # Stores student profiles, face encodings, and logs
├── utils/
│   ├── face_verify.py     # dlib face recognition logic
│   ├── voice_verify.py    # Voice capturing and verification logic
│   └── qr_generator.py    # QR code generation utilities
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
