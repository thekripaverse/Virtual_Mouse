import screen_brightness_control as sbc

def set_brightness(level):  # level: integer from 0 to 100
    try:
        sbc.set_brightness(level)
    except Exception as e:
        print("Brightness error:", e)
