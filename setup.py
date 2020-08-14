from os import system

def setup():
    system("sudo apt install python3-tk -y")
    system("sudo apt install python3-pil.imagetk -y")
    system("pip3 install -r requirements.txt")
    system("clear")
    system("python3 main.py")

if __name__ == "__main__":
    try:
        setup()
    except KeyboardInterrupt:
        print("Exiting Setup Program.")
    except EOFError:
        print("Exiting Setup Program.")
