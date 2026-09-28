# Student Record & Grade Calculator Engine (CLI)

A high-performance command-line utility built in native Python to help teachers log student records, view academic lists, calculate automated marks percentages, and extract class statistics using a low-overhead, text-only operational platform.

## Features Built-In
* **Teacher Identity Portal:** Secure registration routines leveraging custom string inversion masking.
* **Student Registry Ledger:** Full record setup, list generation, and direct row wiping operations (CRUD).
* **Grade Assessment Logic:** Automatic back-end calculation matrix providing final letter grades based on three subject fields.
* **Institutional Metrics:** Instant reporting on entire class benchmarks, displaying running averages alongside individual class toppers.

## System Architecture Details
The codebase uses a clean, separate directory structure to keep terminal display configurations separate from data evaluation modules:
* `main.py` - Core interaction loop handling structural navigation choices.
* `src/auth.py` - Low-level flat file reading logic managing profile verification.
* `src/database.py` - Main database simulator processing text entry creations and row deletions.
* `src/calculator.py` - Marks aggregate calculator logic and class analytics reporting array.

## Setup & System Prerequisites
This management script runs natively using default system resources. You do not need to install external packages or libraries.
* System Baseline: Python 3.8 or subsequent versions.
* Supported Systems: Windows terminal, macOS terminal emulator, Linux shells.

## How to Initialize the Application
To run the terminal interface, launch your system's console tool inside the repository directory and type this command:

```bash
python main.py
```
