import serial
import csv
import time

# -----------------------------
# Change this to your ESP32 COM port
# Example: "COM5" on Windows, "/dev/ttyUSB0" on Linux
PORT = "COM5"
BAUD = 115200

# -----------------------------
gesture_name = input("Enter gesture label (e.g. up, down, left, right): ")
filename = f"{gesture_name}.csv"

# Open Serial
ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)  # wait for connection

print(f"Recording data for gesture: {gesture_name}")
print("Press Ctrl+C to stop...")

# Open CSV file for writing
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ax", "ay", "az", "gx", "gy", "gz", "label"])  # header

    try:
        while True:
            line = ser.readline().decode("utf-8").strip()
            if line:
                try:
                    values = [float(x) for x in line.split(",")]
                    if len(values) == 6:
                        writer.writerow(values + [gesture_name])
                        print(values)
                except:
                    pass
    except KeyboardInterrupt:
        print("\nRecording stopped.")

ser.close()
