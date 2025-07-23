import pywhatkit as kit
import pyautogui
import time

# List of phone numbers in international format
phone_numbers = ["+917588738216","+919907266703"]

# Message to send
message = "automated message send to you using python"

for phone_number in phone_numbers:
    print(f"Sending message to {phone_number}...")

    # Send the message instantly
    kit.sendwhatmsg_instantly(
        phone_no=phone_number,
        message=message,
        wait_time=10,  # Time to wait before sending (seconds)
        tab_close=True,  # Close the tab after sending
        close_time=3     # Time to wait before closing the tab
    )

    time.sleep(1)  # Wait for WhatsApp web to load
    pyautogui.press("enter")  # Press enter to confirm sending if needed

    print("Message was sent")
