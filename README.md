<div align="center">

# Python Pipeline Core & Media Asset Manager

### Modular Python Automation Pipelines, CLI Batch Auditing Tools & PySide6 Desktop Utilities

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/PySide6-Qt_for_Python-41CD52?style=for-the-badge&logo=qt&logoColor=white)](https://doc.qt.io/qtforpython/)
[![Automation](https://img.shields.io/badge/Focus-File_%26_Data_Pipelines-007ACC?style=for-the-badge)](https://github.com/asadsajjadcodes-maker/python_pipeline_core)

</div>

---

**Python Pipeline Core** is a structured engineering repository focused on building reliable Python automation workflows, fault-tolerant JSON/file pipelines, CLI batch utilities, and a modern QSS-styled **PySide6 Media Asset Manager**.

The repository contains **30 root daily scripts (`day_01_basics.py`–`day_30_gui_basics.py`)** covering `pathlib`, defensive JSON serialization, and 10,000+ file CLI batch verification, along with a modular scanner package (`day_29_modular/`) and the multi-module **Pro Media Asset Manager** desktop GUI (`media_organizer/`, developed across stages 31–39).

---

## 🚀 Featured Applications Inside This Repository

### 1. ⚡ Pro Media Asset Manager (`media_organizer/`)
A dark-themed **PySide6** desktop application for auditing and automatically organizing directories into categorized folders (`Images`, `Videos`, `Audio`, `Documents`, `Archives`, `Code`, and `others`).

- **Custom QSS Dark Theme:** Styled with Catppuccin-inspired dark stylesheets (`#1E1E2E`), custom buttons, progress bars, and monospace terminal output.
- **Directory Audit & Auto-Organizer:** Scans nested folders recursively (`scanner.py`) and safely relocates files by extension without overwriting existing files (`organizer.py`).
- **Qt Signal-Slot Logging Bridge:** Uses multiple inheritance (`QObject` + `logging.Handler` in `gui_handler.py`) to stream standard Python log events straight into the GUI console (`QTextEdit`), `app.log`, and terminal simultaneously.

```bash
python media_organizer/main.py
```

### 2. 🔍 CLI Batch JSON Auditing & Telemetry Engine (`day_27_pipeline_summary.py`)
A command-line batch verification tool built with `argparse` and dual-channel `logging` capable of auditing 10,000+ JSON configuration files, tracking execution throughput, supporting `--dry-run` simulation, and exporting structured JSON audit summaries.

```bash
python day_27_pipeline_summary.py --dir path/to/json_assets --dry-run
```

### 3. 📦 Modular Media Asset Scanner (`day_29_modular/`)
A decoupled CLI and library package (`asset_scanner.py`, `logger_config.py`, `main.py`) that categorizes multimedia files and computes cumulative storage metrics in megabytes (`MB`).

```bash
python day_29_modular/main.py
```

---

## 📂 Project Structure

```text
python_pipeline_core/
├── media_organizer/               # PySide6 Desktop Media Asset Manager (Stages 31–39)
│   ├── main.py                    # QMainWindow GUI, QSS dark theme & event controllers
│   ├── organizer.py               # Extension-mapped auto-organizer with collision protection
│   ├── scanner.py                 # Recursive pathlib directory scanner
│   ├── gui_handler.py             # Custom QObject + logging.Handler Qt signal bridge
│   └── logger.py                  # Triple-destination logger (Console, File, GUI)
│
├── day_29_modular/                # Modular CLI Media Asset Scanner
│   ├── main.py                    # Entry point & summary reporting
│   ├── asset_scanner.py           # Media classification & MB size calculation
│   └── logger_config.py           # Reusable dual-channel logger setup
│
├── day_01_basics.py ... day_30_gui_basics.py  # 30 standalone root pipeline scripts
├── asset_config.json              # Sample nested asset configuration file
├── .gitattributes
├── .gitignore
└── README.md
```

---

## 📅 Daily Progress Tracker (`day_01`–`day_30` Root Scripts & `media_organizer/` Stages 31–39)

| Stage | Topic | Core Engineering Focus | Status |
| :--- | :--- | :--- | :---: |
| **Day 01** | Smart File Handling (`pathlib`) | Transitioning from raw string manipulation to object-oriented path handling. | ✅ |
| **Day 02** | Path Anatomy Deep Dive | Breaking down asset paths using `.name`, `.stem`, and `.suffix` properties. | ✅ |
| **Day 03** | Directory Hierarchy Navigation | Traversing parent and grandparent folder levels dynamically using `.parent`. | ✅ |
| **Day 04** | Path Validation & Verification | Confirming item existence and distinguishing files from directories safely. | ✅ |
| **Day 05** | Idiomatic Path Joining | Constructing complex cross-platform paths cleanly using the `/` operator. | ✅ |
| **Day 06** | Immutable Path Modification | Swapping file components and suffixes immutably using path-transformation methods. | ✅ |
| **Day 07** | Directory Scanning & Iteration | Automating batch tasks by scanning directories and filtering items with `.iterdir()`. | ✅ |
| **Day 08** | Pattern Matching with Glob | Filtering files dynamically using pattern-based matching with `.glob()`. | ✅ |
| **Day 09** | Robust Folder Creation | Generating nested directory trees dynamically on disk using `.mkdir()`. | ✅ |
| **Day 10** | Active File Relocation & Writing | Writing files, verifying destination workspaces, and moving assets using `.rename()`. | ✅ |
| **Day 11** | Safe File I/O & Streaming | Appending persistent log metadata and reading files securely using context managers. | ✅ |
| **Day 12** | Structured Log Parsing | Dissecting key-value metadata dynamically from raw text strings using controlled splits. | ✅ |
| **Day 13** | Conditional Log Searching | Building automated QA keyword scanners to sweep log files for specific statuses. | ✅ |
| **Day 14** | In-Memory Data Replacing | Reading files and dynamically modifying layout configurations using string replacements. | ✅ |
| **Day 15** | JSON Data Serialization | Serializing structured dictionary metadata directly into formatted JSON configs using `json.dump()`. | ✅ |
| **Day 16** | JSON Ingestion & Guardrails | Deserializing JSON structures with `json.load()`, type validation, and graceful `sys.exit()` terminations. | ✅ |
| **Day 17** | Dynamic JSON Configuration Editing | Modifying in-memory JSON configurations dynamically and saving updates via a Read-Modify-Write workflow. | ✅ |
| **Day 18** | Defensive Dictionary Lookups | Preventing dictionary lookup crashes using `.get()` with safe default fallback boundaries. | ✅ |
| **Day 19** | Nested Configuration Parsing | Navigating deeply nested, multi-layered JSON metadata properties safely using chained dictionary lookups. | ✅ |
| **Day 20** | Modular Abstraction & Functions | Encapsulating validation logic inside reusable custom functions for modular data processing. | ✅ |
| **Day 21** | Structural Exception Handling | Implementing multi-layered `try/except` blocks to isolate asset ingestion states from unexpected file failures. | ✅ |
| **Day 22** | Reusable Loader Utilities | Abstracting JSON ingestion into a production loader utility (`safe_load_json`) with customizable fallbacks. | ✅ |
| **Day 23** | Reusable Saver Utilities | Building `safe_save_json` to automatically guarantee folder paths, catch write permissions, and handle serialization errors. | ✅ |
| **Day 24** | Batch Processing Engine & Dataset Generator | Building automated dataset generation utilities and orchestrating multi-file asset workflows via recursive search (`rglob`). | ✅ |
| **Day 25** | Dual-Channel Logging Infrastructure | Implementing standard `logging` with file/console output streams, severity classification, and ISO timestamp formatting. | ✅ |
| **Day 26** | CLI Argument Parsing & Pipeline Auditing | Integrating `argparse` with dual-channel `logging` to execute parameter-driven batch scans and dry runs. | ✅ |
| **Day 27** | Scalable Batch Processing & Analytics Export | Scaling batch verification to 10,000+ files, tracking runtime metrics, and exporting analytics reports. | ✅ |
| **Day 28** | Media Asset Auditing & Classification Pipeline | Scanning directories recursively, categorizing picture and video formats by extensions, and calculating total storage usage. | ✅ |
| **Day 29** | Modular Media Asset Scanner & Logging Integration | Refactoring asset scanning logic into reusable modules (`asset_scanner`, `logger_config`) with CLI parameter controls. | ✅ |
| **Day 30** | PySide6 GUI for Media Asset Inspection | Building a desktop interface with PySide6, implementing path input handlers, and streaming real-time status updates to a GUI display. | ✅ |
| **Day 31** | Multi-Action Desktop GUI & Directory Dialogs | Expanding PySide6 window controls with OS native folder dialogs (`QFileDialog`) and audit execution triggers. | ✅ |
| **Day 32** | Modern QSS Styling & Visual Feedback Interface | Redesigning the Media Asset Manager with modern Qt stylesheets (QSS), dark terminal logs, rounded input controls, and progress indicators. | ✅ |
| **Day 33** | Live Backend-GUI Integration & Dynamic Progress | Connecting `pathlib` recursive scanner logic (`scanner.py`) to the PySide6 UI with real-time progress bar tracking and live event processing. | ✅ |
| **Day 34** | UI Message Abstraction & Logging Preparation | Centralizing GUI message handling with a reusable `show_message()` helper, reducing duplicated UI update logic. | ✅ |
| **Lesson 35** | Integrated Multi-Module Logging Engine | Implementing a dedicated logging module (`logger.py`) with severity levels (`INFO`, `WARNING`, `ERROR`) integrated across backend and GUI layers. | ✅ |
| **Lesson 36** | Logging Architecture & StreamHandler | Replacing `logging.basicConfig()` with an explicit `StreamHandler` and manual logger-to-handler configuration. | ✅ |
| **Lesson 37** | Multi-Destination Logging with FileHandler | Extending the logging system with a dedicated `FileHandler` for simultaneous terminal and persistent `app.log` output. | ✅ |
| **Lesson 38** | Specialized Multi-Destination Logging & Auto-Organizer | Integrating `organizer.py` for automated extension mapping and safe file relocation with distinct console/file formatters. | ✅ |
| **Lesson 39** | Qt Signal-Slot Logging Bridge & GuiHandler | Enhancing `GuiHandler` with PySide6 `QObject` and `Signal(str)` to stream backend logs directly into the GUI console. | ✅ |

---

## 🛠️ Tech Stack & Core Modules

- **Language:** Python 3.10+
- **Desktop GUI:** `PySide6` (Qt Widgets, QSS Stylesheets, `QFileDialog`, `QProgressBar`, `QObject`, `Signal`)
- **File & OS Automation:** `pathlib` (`Path`, `rglob`, `iterdir`, `stat`, `rename`, `mkdir`)
- **Data Serialization:** `json` (`load`, `dump`, defensive validation & error recovery)
- **CLI & Diagnostics:** `argparse` (`ArgumentParser`, `--dry-run` flags) & `logging` (`StreamHandler`, `FileHandler`, custom `GuiHandler`)

---

## 📖 Architectural Highlights

### CLI-Driven Operations & Safe Dry-Run Audits (Days 26–27)
- **Command-Line Interface (`argparse.ArgumentParser`):** Supports runtime flags (`--dir`, `--file-path`, `--report-file`, `--dry-run`) without modifying source code.
- **Dry-Run Simulation Mode:** Validates paths and streams preview logs (`[Dry run] Would scan...`) without performing disk writes.
- **Performance Telemetry:** Tracks execution times and exports structured JSON verification reports (`passed`, `failed`, `skipped`, and `execution_time_seconds`).

### Decoupled Desktop GUI & Triple-Channel Logging (Lessons 30–39)
- **Qt Multiple Inheritance (`QObject` + `logging.Handler`):** `GuiHandler` in `media_organizer/gui_handler.py` inherits from both `QObject` and `logging.Handler`, emitting a thread-safe `Signal(str)` whenever any backend module logs a message.
- **Collision-Safe File Organization:** `organize_folder()` in `media_organizer/organizer.py` categorizes files by extension, automatically creates target subdirectories, skips files already in their category folder, and refuses to overwrite existing files.

---

## 👤 Author

**Asad Sajjad**
- GitHub: [@asadsajjadcodes-maker](https://github.com/asadsajjadcodes-maker)