import os
import platform
import socket
import getpass
from colorama import init, Fore, Style
import time

# Initialize colorama for colored output
init()

# Custom banner
def print_banner():
    banner = f"""
{Fore.GREEN}  ╔════════════════════════════════════════════════════╗
  ║             Pakistani Ethical Hacker               ║
  ║                Mr Sabaz Ali Khan                   ║
  ║                                                    ║
  ║          WHOAMI System Information Tool            ║
  ╚════════════════════════════════════════════════════╝{Style.RESET_ALL}
    """
    print(banner)
    print(f"{Fore.CYAN}Developed by: Mr Sabaz Ali Khan{Style.RESET_ALL}\n")

# Function to gather system information
def get_system_info():
    try:
        info = {}
        info['Username'] = getpass.getuser()
        info['Hostname'] = socket.gethostname()
        info['IP Address'] = socket.gethostbyname(socket.gethostname())
        info['Operating System'] = platform.system()
        info['OS Version'] = platform.version()
        info['OS Release'] = platform.release()
        info['Architecture'] = platform.machine()
        info['Processor'] = platform.processor() or "N/A"
        info['Python Version'] = platform.python_version()
        
        # Get current working directory
        info['Current Directory'] = os.getcwd()
        
        # Get system uptime (Linux/Unix only)
        if platform.system() in ["Linux", "Darwin"]:
            with open("/proc/uptime", "r") as f:
                uptime_seconds = float(f.read().split()[0])
                uptime_days = uptime_seconds // (24 * 3600)
                uptime_hours = (uptime_seconds % (24 * 3600)) // 3600
                uptime_minutes = (uptime_seconds % 3600) // 60
                info['Uptime'] = f"{int(uptime_days)} days, {int(uptime_hours)} hours, {int(uptime_minutes)} minutes"
        else:
            info['Uptime'] = "Uptime not supported on this OS"

        return info
    except Exception as e:
        print(f"{Fore.RED}Error gathering system info: {e}{Style.RESET_ALL}")
        return None

# Function to display system information
def display_info(info):
    if info:
        print(f"{Fore.YELLOW}=== System Information ==={Style.RESET_ALL}")
        for key, value in info.items():
            print(f"{Fore.GREEN}{key}: {Fore.WHITE}{value}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Failed to retrieve system information.{Style.RESET_ALL}")

# Main function
def main():
    print_banner()
    print(f"{Fore.CYAN}Fetching system information...{Style.RESET_ALL}")
    time.sleep(1)  # Small delay for effect
    system_info = get_system_info()
    display_info(system_info)
    print(f"\n{Fore.CYAN}Thank you for using the WHOAMI tool by Mr Sabaz Ali Khan!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()