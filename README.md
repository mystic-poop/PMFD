# PMFD - Package Manager For Debian

[![GitHub license](https://img.shields.io/github/license/mystic-poop/PMFD)](https://github.com/mystic-poop/PMFD/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org)
[![Platform](https://img.shields.io/badge/platform-Debian%2FUbuntu-lightgrey)](https://debian.org)

PMFD (Package Manager For Debian) is a universal Python-based package manager that intelligently determines the best installation method for any given package on Debian-based systems. It aggregates multiple package managers into a single unified interface, automatically selecting the optimal installation method.

## Key Features

- 🔍 **Universal Package Discovery** - Automatically finds packages across multiple sources
- ⚡ **Intelligent Installation** - Chooses the best package manager for each package
- 🔄 **Multi-Source Support** - Works with:
  - APT (native Debian packages)
  - Snap (universal packages)
  - Flatpak (sandboxed applications)
  - dpkg (direct .deb file installation)
- ✅ **Error Handling** - Comprehensive error detection and reporting
- 📦 **Batch Operations** - Install multiple packages with a single command
- 🛠️ **Root Automation** - Handles privilege escalation automatically

## Installation

### Quick Install
```bash
sudo curl -L https://raw.githubusercontent.com/mystic-poop/PMFD/main/pmfd.py -o /usr/local/bin/pmfd
sudo chmod +x /usr/local/bin/pmfd
```
## Manual Installation
1.Clone the repository:
```bash
git clone https://github.com/mystic-poop/PMFD.git
cd PMFD
```
2.Make the script executable:
```bash
chmod +x pmfd.py
```
3.Create a symlink for easy access:
```bash
sudo ln -s $(pwd)/pmfd.py /usr/local/bin/pmfd
```
## Usage
Basic commands
```bash
# Install single package
sudo pmfd install <package-name>

# Install multiple packages
sudo pmfd install <package1> <package2> ...

# Install .deb file
sudo pmfd install /path/to/package.deb

# Install popular applications
sudo pmfd install firefox vscode discord

# Install from different sources
sudo pmfd install gimp snapd flatpak

# Install local .deb file
sudo pmfd install ~/Downloads/custom-package.deb
```
## How It Works
PMFD uses a smart algorithm to determine the best installation method:
1. **APT Check** - Attempts installation via native Debian packages
2. **Snap Fallback** - Tries Snap store if APT package not found
3. **Flatpak Option** - Looks for Flatpak availability as third option
4. **dpkg Handling** - Automatically installs .deb files
5. **Error Reporting** - Provides detailed error messages for missing packages
The tool automatically detects which package managers are available on your system and only uses relevant installation methods.
## Requirements
- Python 3.8+
- Debian-based Linux distribution (Debian, Ubuntu, Mint, etc.)
- sudo privileges for package installation
- Internet connection (for repository packages)
