import math

# รับค่าน้ำหนัก (kg)
weight = float(input("ป้อนน้ำหนักของคุณ (kg) : "))

# รับค่าส่วนสูง (cm)
height = float(input("ป้อนส่วนสูงของคุณ (cm) : "))

# แปลงหน่วยส่วนสูงจาก cm เป็น m
height_m = height / 100

# คำนวณค่า BMI ** คือการยกกำลัง
bmi = weight / (height_m ** 2)

# แสดงผลลัพธ์
print("ค่า BMI ของคุณคือ", bmi)

# ตีความค่า BMI
if bmi >= 35:
    print("อยู่ในเกณฑ์อ้วนขั้นที่ 3")
elif bmi >= 30:
    print("อยู่ในเกณฑ์อ้วนขั้นที่ 2")
elif bmi >= 25:
    print("อยู่ในเกณฑ์อ้วนขั้นที่ 1")
elif bmi >= 23:
    print("อยู่ในเกณฑ์น้ำหนักเกิน")
elif bmi >= 18.5:
    print("อยู่ในเกณฑ์ปกติ")
else:
    print("อยู่ในเกณฑ์น้ำหนักต่ำกว่าปกติ")
