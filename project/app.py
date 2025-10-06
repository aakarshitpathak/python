import os
import subprocess

def open_app(app_name):
    '''
    opens an app by its name
    '''
    try:
        # Try to open the app directly if it's in PATH
        subprocess.run(app_name , shell = True, check=True)
        print(f"Opening {app_name}....")
    
    except FileNotFoundError:
        # if the app isnt in PATH , attempt to locate it manually
        desktop_path= os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
        possible_paths=[
            f"C:\Program Files\\{app_name}\\{app_name}.exe",
            f"C:\Program Files (x86)\\{app_name}\\{app_name}.exe",
            os.path.join(desktop_path, f"{app_name}. lnk"), # App shortcut on desktop
            os.path.join(desktop_path, f"{app_name}. exe"), # Excutable file on desktop
        ]
        for path in possible_paths:
            if os.path.exists(path):
                subprocess.run(path, shell=True , check=True)
                print(f"Opening {app_name} from {path}...")
                return
            
        print(f"App '{app_name}' not found. Please check the name or add it to your PATH")
    except Exception as e:
        print(f"An error occured: {e}")

# Main Program
if __name__ == "__main__":
    print ("Welcome to the Dynamic App Launcher! ")
    app_name = input("Enter the name of the app ro open: ").strip()
    open_app(app_name)