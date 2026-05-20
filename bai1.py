# nhịp tim 135 đáng lẽ phải là đỏ nhưng chương trình chạy lại hiện vàng => sai
# luồng chạy từ trên xuống iưới của if elif else khi mà điều kiện ở if thoả mãn thì sẽ ko chạy xuống elif và else nữa nếu ko thoả mãn thì sẽ xuống elif khác và nếu ko thoả màn thì vẫn viếp tục đến cuối else thì sẽ dừng lại 
#  nguyên nhân red bị bỏ qua và nếu yellow có điều kiện hơn 100 mà 135 thì thoả mãn nên nó vào yellow chứ ko vào red 
print("--- EMERGENCY TRIAGE SYSTEM ---")
heart_rate = int(input("Enter patient's heart rate (bpm): "))

# Hệ thống phân loại ưu tiên
if heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate < 120 and heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")
