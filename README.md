# 🐍 Snake Game - Gesture Controlled

A fun **IoT + Machine Learning project** where you control the classic **Snake Game** using **hand gestures**.  
Gestures are captured from an **MPU6050 sensor** connected to an **ESP32**, classified using a **Random Forest model**, and then sent to control the snake in **Pygame**.  

---

## 🚀 Features
- Control the Snake Game with **hand gestures**
- Built with:
  - **ESP32 + MPU6050** for motion sensing  
  - **Random Forest Classifier** for gesture recognition  
  - **Pygame** for the Snake game  
- Keyboard arrow keys as **fallback control**  
- Food **timeout & respawn mechanics**  
- Live **score display**  

---

## 🛠️ Tech Stack
- **Python 3.9+**  
- **Pygame**  
- **scikit-learn**  
- **pandas**  
- **joblib**  
- **pyserial**  

---

## 📂 Project Structure
```
Snake_Game_Gesture_Control/
│── collect.py             # Collect raw gesture data from MPU6050
│── merge_csv.py           # Merge collected CSVs into one dataset
│── accuracy.py            # Train RandomForest & save model
│── atlast.py              # Snake Game with gesture control
│
│── gestures_dataset.csv   # Combined dataset
│── gesture_model.pkl      # Trained ML model
│── up.csv / down.csv /
│   left.csv / right.csv   # Raw gesture data
│
│── README.md              # Project documentation
```

---

## ⚡ Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/Snake_Game_Gesture_Control.git
   cd Snake_Game_Gesture_Control
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Linux/Mac
   venv\Scripts\activate         # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Connect **ESP32 + MPU6050** to your PC (check COM port).  

---

## 🎮 Usage

### 1️⃣ Collect Gesture Data
```bash
python collect.py
# Enter gesture label (up / down / left / right)
```

### 2️⃣ Merge Dataset
```bash
python merge_csv.py
```

### 3️⃣ Train Model
```bash
python accuracy.py
```
➡ Generates `gesture_model.pkl`

### 4️⃣ Play Snake Game
```bash
python atlast.py
```

- Snake moves according to detected gestures  
- Keyboard arrows also work as backup  

---

## 📝 Example
```
Gesture: UP
Snake moves upward ✅

Gesture: LEFT
Snake moves left ✅
```

---

## 🔮 Future Improvements
- Add more gestures (pause, restart)  
- Use **deep learning (CNN/LSTM)** for gesture recognition  
- Wireless control over **Bluetooth/WiFi**  
- Multiplayer gesture-based games  

---

## 👨‍💻 Author
**Varun Kumar**  
📧 [varunkr6302@gmail.com](mailto:varunkr6302@gmail.com)  
🔗 [GitHub Profile](https://github.com/<your-username>)  
