import time

def countdown_timer():
    """Simple countdown timer with minutes and seconds"""
    
    print("⏰ COUNTDOWN TIMER ⏰")
    print("=" * 35)
    
    # Get minutes and seconds from user
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))
    
    # Calculate total seconds
    total_seconds = (minutes * 60) + seconds
    
    print(f"\n⏱️  Starting countdown: {minutes}m {seconds}s")
    print("Press Ctrl+C to stop early\n")
    
    try:
        while total_seconds > 0:
            # Calculate remaining minutes and seconds
            mins = total_seconds // 60
            secs = total_seconds % 60
            
            # Format display (add leading zeros)
            timer_display = f"{mins:02d}:{secs:02d}"
            print(f"Time left: {timer_display}", end='\r')
            
            time.sleep(1)
            total_seconds -= 1
        
        # Timer finished
        print("\n" + "=" * 35)
        print("🎉 TIME'S UP! 🎉")
        print("⏰ *BEEP BEEP BEEP* ⏰")
        print("=" * 35)
        
        # Optional: Beep sound (works on most systems)
        print('\a')  # ASCII bell character
        
    except KeyboardInterrupt:
        print("\n\n⏸️  Timer stopped by user!")

# Run the timer
countdown_timer()