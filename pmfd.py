#!/usr/bin/env python3
import subprocess
import os
import sys

def main():

    if os.geteuid() != 0:
        print("Error: Please run the program as root", file=sys.stderr)
        print("Usage: sudo ./ALPS.py <package> [package2 ...]", file=sys.stderr)
        sys.exit(1)
    if len(sys.argv) < 2:
        print("Error: Please enter a package name ", file=sys.stderr)
        print("Usage: sudo ./ALPS.py <package> [package2 ...]", file=sys.stderr)
        sys.exit(1)
    #Package managers
    packages = sys.argv[1:]
    print(f"Packages wanted to download: {', '.join(packages)}")
    commands = [
        ("APT", ["apt", "install", "-y"]),
        ("Snap", ["snap", "install"]),
        ("Aptitude", ["aptitude", "install", "-y"]),
        ("Flatpak", ["flatpak", "install", "-y", "--user"])
    ]
    
    failed_packages = []
   #Download part 
    for package in packages:
        success = False
        print(f"\n{'='*50}")
        print(f"{package} is downloading")
        print(f"{'='*50}")
        
        for manager, cmd_base in commands:
            cmd = cmd_base + [package]
            
            try:
                print(f"[{manager}] Trying: {' '.join(cmd)}")
                result = subprocess.run(
                    cmd,
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=300
                )
                print(f"✓ [{manager}] Sucsessufly downloaded: {package}")
                if result.stdout.strip():
                    print(f"Reslts: {result.stdout.strip()[:200]}...")
                success = True
                break
                
            except FileNotFoundError:
                print(f"✗ [{manager}] Not found!")
            except subprocess.CalledProcessError as e:
                print(f"✗ [{manager}] ERROR: ({e.returncode}): {e.stderr.strip()[:200]}")
            except Exception as e:
                print(f"✗ [{manager}] Unexpected Error! {str(e)[:200]}")
        #Finally tries to install with dpkg
        if not success and package.endswith('.deb'):
            print(f"\n[dpkg] trying to downlaod with the .deb for: {package}")
            try:
                subprocess.run(
                    ["dpkg", "-i", package],
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                print(f"✓ [dpkg] Downloaded: {package}")
                success = True
            except Exception as e:
                print(f"✗ [dpkg] ERROR: {str(e)[:200]}")
        
        if not success:
            print(f"\n❌ Cannot find the: {package}")
            failed_packages.append(package)
    #Report
    print("\n" + "="*50)
    print("Results")
    print("="*50)
    if failed_packages:
        print(f"❌ Failed Packages: {', '.join(failed_packages)}")
        sys.exit(1)
    else:
        print("✓ Packages downloaded with an sucsess")
        sys.exit(0)

if __name__ == "__main__":
    main()
