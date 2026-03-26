import time

# Simple countdown timer
print("⏰ SIMPLE COUNTDOWN TIMER ⏰")
print("=" * 30)

# Get the number of seconds from user
seconds = int(input("Enter number of seconds to countdown: "))

print(f"\nStarting countdown for {seconds} seconds...\n")

# Countdown loop
while seconds > 0:
    print(f"Time left: {seconds} seconds")
    time.sleep(1)  # Wait for 1 second
    seconds -= 1   # Decrease by 1

print("\n🎉 TIME'S UP! 🎉")
print("⏰ BEEP BEEP BEEP! ⏰")