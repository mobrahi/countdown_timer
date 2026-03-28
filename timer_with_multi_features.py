import time
import os
import sys

def clear_screen():
    """Clear the terminal screen"""
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac/Linux
    else:
        os.system('clear')

def countdown_timer_enhanced():
    """Enhanced countdown timer with more features"""
    
    while True:
        clear_screen()
        print("=" * 40)
        print("   ⏰ COUNTDOWN TIMER ⏰")
        print("=" * 40)
        print("\nOptions:")
        print("1. ⏱️  Set custom time")
        print("2. 📝 Use preset times")
        print("3. ❌ Exit")
        
        choice = input("\nChoose an option (1-3): ").strip()
        
        if choice == "1":
            custom_timer()
        elif choice == "2":
            preset_timer()
        elif choice == "3":
            print("\n👋 Goodbye! Thanks for using the timer!")
            time.sleep(1)
            break
        else:
            print("\n❌ Invalid choice! Please try again.")
            time.sleep(1)

def custom_timer():
    """Set a custom timer"""
    clear_screen()
    print("⏱️  CUSTOM TIMER")
    print("=" * 35)
    
    # Get time input
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))
    
    # Calculate total seconds
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    
    if total_seconds <= 0:
        print("\n❌ Please enter a time greater than 0!")
        time.sleep(2)
        return
    
    run_timer(total_seconds, hours, minutes, seconds)

def preset_timer():
    """Choose from preset times"""
    clear_screen()
    print("📝 PRESET TIMES")
    print("=" * 35)
    print("\nCommon presets:")
    print("1. 🍳 1 minute (cooking egg)")
    print("2. 🧘 5 minutes (short break)")
    print("3. ☕ 10 minutes (coffee break)")
    print("4. 🍝 20 minutes (pasta cooking)")
    print("5. 📚 25 minutes (Pomodoro session)")
    print("6. 🎬 30 minutes (TV episode)")
    print("7. ⬅️  Back to main menu")
    
    choice = input("\nChoose a preset (1-7): ").strip()
    
    presets = {
        "1": 60,
        "2": 300,
        "3": 600,
        "4": 1200,
        "5": 1500,
        "6": 1800
    }
    
    if choice == "7":
        return
    elif choice in presets:
        total_seconds = presets[choice]
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        hours = 0
        run_timer(total_seconds, hours, minutes, seconds)
    else:
        print("\n❌ Invalid choice!")
        time.sleep(1)

def run_timer(total_seconds, hours, minutes, seconds):
    """Run the actual countdown timer"""
    clear_screen()
    
    print("🎬 TIMER STARTED! 🎬")
    print("=" * 35)
    
    if hours > 0:
        print(f"Time set: {hours}h {minutes}m {seconds}s")
    else:
        print(f"Time set: {minutes}m {seconds}s")
    
    print("\nPress Ctrl+C to stop early\n")
    
    try:
        while total_seconds > 0:
            # Calculate remaining time
            hrs = total_seconds // 3600
            mins = (total_seconds % 3600) // 60
            secs = total_seconds % 60
            
            # Create display
            if hrs > 0:
                timer_display = f"{hrs:02d}:{mins:02d}:{secs:02d}"
            else:
                timer_display = f"{mins:02d}:{secs:02d}"
            
            # Show progress bar
            progress = create_progress_bar(total_seconds, 
                                          (hours*3600)+(minutes*60)+seconds)
            
            # Print timer (use \r to update same line)
            print(f"⏱️  Time left: {timer_display} {progress}", end='\r')
            
            time.sleep(1)
            total_seconds -= 1
        
        # Timer finished
        timer_finished()
        
    except KeyboardInterrupt:
        print("\n\n⏸️  Timer stopped by user!")
        time.sleep(1)

def create_progress_bar(current, total):
    """Create a visual progress bar"""
    if total == 0:
        return ""
    
    bar_length = 20
    progress = (total - current) / total
    filled_length = int(bar_length * progress)
    
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    percentage = int(progress * 100)
    
    return f"[{bar}] {percentage}%"

def timer_finished():
    """Display timer completion message"""
    print("\n" + "=" * 40)
    print("🎉🎉🎉 TIME'S UP! 🎉🎉🎉")
    print("=" * 40)
    print("\n⏰ *BEEP BEEP BEEP* ⏰")
    print("⏰ *BEEP BEEP BEEP* ⏰")
    print("\n✨ Timer completed! ✨")
    print("=" * 40)
    
    # Try to make a beep sound
    for _ in range(3):
        print('\a', end='', flush=True)
        time.sleep(0.5)
    
    input("\n\nPress Enter to continue...")

# Run the enhanced timer
if __name__ == "__main__":
    countdown_timer_enhanced()