from escpos.printer import File
from config import PRINTER_PORT, BARCODE_FILE
from utils import resize_image, generate_barcode

p = File(PRINTER_PORT)


def print_plain(plain):
    try:    
        print_line("-")
        p.text(plain+"\n")
        print_line("-")
        return False, "success"
    except Exception as e:
        print(f"Error printing: {e}")
        return True, e

def print_receipt(message):
    try:
        parts = message.splitlines()
        
        platform = parts[0]
        buyer = parts[1]
        courier = parts[2]
        resi = parts[3]
        items = parts[4:]
        
        p.set(align="center", font="a", width=2, height=2, bold=True)
        p.text("\n{0}\n\n".format(platform).upper())
        print("platform: {0}".format(platform))
        
        p.set(align="center", font="a", width=1, height=1, bold=True)
        p.text("{0}\n".format(buyer))
        print("buyer: {0}".format(buyer))
        generate_barcode(resi)
        resized_img = resize_image(f"{BARCODE_FILE}.png", 360)
        p.image(resized_img)
        # p.set(align="center", font="a", width=1, height=1, bold=False)
        # p.barcode('{B'+resi, "CODE128", function_type="B")
        print("resi: {0}".format(resi))
        
        p.text("\n{0}\n".format(courier).upper())
        print("courier: {0}".format(courier))
        
        for item in items:
            p.text("{0}\n".format(item))
            print(item)
            
        print_line("-")
        return False, "success"    
        
    except Exception as e:
        print(f"Error printing: {e}")
        return True,e
    
def print_line(char="-", width=24):
    line = char * width
    p.set(align="center", font="a", width=1, height=1, bold=True)
    p.text(line + "\n")

def print_ok():
    print_line("-")
    p.set(align="center", font="a", width=1, height=1, bold=True)
    p.text("Sistem OK\n")
    print_line("-")
