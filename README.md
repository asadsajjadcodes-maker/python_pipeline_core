# Python Pipeline Core

A repository dedicated to mastering Python automation, core programming workflows, and building robust backend pipelines. This project tracks daily progress, shifting from foundational concepts to advanced modular automation scripts.

## 📅 Daily Progress Tracker

| Day  | Topic | Description | Status |
| :--- | :--- | :--- | :--- |
| **Day 1** | Smart File Handling (`pathlib`) | Transitioning from raw string manipulation to object-oriented path handling. | ✅ Done |
| **Day 2** | Path Anatomy Deep Dive | Breaking down asset paths using `.name`, `.stem`, and `.suffix` properties. | ✅ Done |
| **Day 3** | Directory Hierarchy Navigation | Traversing parent and grandparent folder levels dynamically using `.parent`. | ✅ Done |
| **Day 4** | Path Validation & Verification | Confirming item existence and distinguishing files from directories safely. | ✅ Done |
| **Day 5** | Idiomatic Path Joining | Constructing complex cross-platform paths cleanly using the `/` operator. | ✅ Done |
| **Day 6** | Immutable Path Modification | Swapping file components and suffixes immutably using path-transformation methods. | ✅ Done |
| **Day 7** | Directory Scanning & Iteration | Automating batch tasks by scanning directories and filtering items with `.iterdir()`. | ✅ Done |
| **Day 8** | Pattern Matching with Glob | Filtering files dynamically using pattern-based matching with `.glob()`. | ✅ Done |
| **Day 9** | Robust Folder Creation | Generating nested directory trees dynamically on disk using `.mkdir()`. | ✅ Done |
| **Day 10**| Active File Relocation & Writing | Writing files, verifying destination workspaces, and moving assets using `.rename()`. | ✅ Done |
| **Day 11**| Safe File I/O & Streaming | Appending persistent log metadata and reading files securely using context managers. | ✅ Done |
| **Day 12**| Structured Log Parsing | Dissecting key-value metadata dynamically from raw text strings using controlled splits. | ✅ Done |
| **Day 13**| Conditional Log Searching | Building automated QA keyword scanners to sweep log files for specific statuses. | ✅ Done |
| **Day 14**| In-Memory Data Replacing | Reading files and dynamically modifying layout configurations using string replacements. | ✅ Done |
| **Day 15**| JSON Data Serialization | Serializing structured dictionary metadata directly into formatted JSON configs using `json.dump()`. | ✅ Done |
| **Day 16**| JSON Ingestion & Guardrails | Deserializing JSON structures with `json.load()`, type validation, and graceful `sys.exit()` terminations. | ✅ Done |
| **Day 17**| Dynamic JSON Configuration Editing | Modifying in-memory JSON configurations dynamically and saving updates via a Read-Modify-Write workflow. | ✅ Done |
| **Day 18**| Defensive Dictionary Lookups | Preventing dictionary lookup crashes using `.get()` with safe default fallback boundaries. | ✅ Done |
| **Day 19**| Nested Configuration Parsing | Navigating deeply nested, multi-layered JSON metadata properties safely using chained dictionary lookups. | ✅ Done |
| **Day 20**| Modular Abstraction & Functions | Encapsulating validation logic inside reusable custom functions for modular data processing. | ✅ Done |
| **Day 21**| Structural Exception Handling | Implementing multi-layered `try/except` blocks to isolate asset ingestion states from unexpected file failures. | ✅ Done |
| **Day 22**| Reusable Loader Utilities | Abstracting JSON ingestion into a production loader utility (`safe_load_json`) with customizable fallbacks. | ✅ Done |
| **Day 23**| Reusable Saver Utilities | Building `safe_save_json` to automatically guarantee folder paths, catch write permissions, and handle serialization errors. | ✅ Done |
| **Day 24**| Batch Processing Engine & Dataset Generator | Building automated dataset generation utilities and orchestrating multi-file asset workflows via recursive search (`rglob`). | ✅ Done |
| **Day 25**| Dual-Channel Logging Infrastructure | Implementing standard `logging` with file/console output streams, severity classification, and ISO timestamp formatting. | ✅ Done |
| **Day 26**| CLI Argument Parsing & Pipeline Auditing | Integrating `argparse` with dual-channel `logging` to execute parameter-driven batch scans and dry runs. | ✅ Done |
| **Day 27**| Scalable Batch Processing & Analytics Export | Scaling batch verification to 10,000+ files, tracking runtime metrics, and exporting analytics reports. | ✅ Done |
| **Day 28**| Media Asset Auditing & Classification Pipeline | Scanning directories recursively, categorizing picture and video formats by extensions, and calculating total storage usage. | ✅ Done |
| **Day 29**| Modular Media Asset Scanner & Logging Integration | Refactoring asset scanning logic into reusable modules (`asset_scanner`, `logger_config`) with CLI parameter controls. | ✅ Done |
| **Day 30**| PySide6 GUI for Media Asset Inspection | Building a desktop interface with PySide6, implementing path input handlers, and streaming real-time status updates to a GUI display. | ✅ Done |
| **Day 31**| Multi-Action Desktop GUI & Directory Dialogs | Expanding PySide6 window controls with OS native folder dialogs (`QFileDialog`) and audit execution triggers. | ✅ Done |
| **Day 32**| Modern QSS Styling & Visual Feedback Interface | Redesigning the Media Asset Manager with modern Qt stylesheets (QSS), dark terminal logs, rounded input controls, and progress indicators. | ✅ Done |
| **Day 33**| Live Backend-GUI Integration & Dynamic Progress | Connecting `pathlib` recursive scanner logic (`scanner.py`) to the PySide6 UI with real-time progress bar tracking and live event processing. | ✅ Done |
| **Day 34**| UI Message Abstraction & Logging Preparation | Centralized GUI message handling with a reusable `show_message()` helper, reducing duplicated UI update logic. | ✅ Done |
| **Lesson 35**| Integrated Multi-Module Logging Engine | Implementing a dedicated logging module (`logger.py`) with severity levels (`INFO`, `WARNING`, `ERROR`) integrated across backend and GUI layers. | ✅ Done |
| **Lesson 36** | Logging Architecture & StreamHandler | Replaced `logging.basicConfig()` with an explicit `StreamHandler`, configured the logger manually, introduced logger-to-handler architecture, and gained a deeper understanding of how log records flow from the application to their output destinations. | ✅ Done |
| **Lesson 37** | Multi-Destination Logging with FileHandler | Extended the logging system by adding a `FileHandler`, allowing a single log message to be written to both the terminal and `app.log`. Reused the same formatter across multiple handlers and implemented duplicate-handler prevention using `if not logger.handlers:` to avoid repeated log entries. | ✅ Done |
| **Lesson 38** | Specialized Multi-Destination Logging & Auto-Organizer Module | Created `organizer.py` for automated extension mapping and safe file relocation. Configured distinct formatters for console and file logging to capture module metadata, function names, and line numbers. | ✅ Done |

---

## 🛠️ Tech Stack & Core Modules
* **Language:** Python 3.13+
* **Core Modules Used:** 
  * `PySide6` (Qt for Python GUI framework with custom QSS styling)
  * `argparse` (CLI flag and argument parser)
  * `pathlib` (Object-oriented filesystem paths)
  * `json` (JavaScript Object Notation encoder and decoder)
  * `logging` (Flexible event logging system for applications)

---

## 📖 Lessons Learned

### Day 1 to Day 25: Core Pipeline Foundations
* **Batch Operations & Telemetry:** Combined recursive pattern search (`rglob`), exception handling boundaries, and dual-channel streaming logs (`FileHandler` + `StreamHandler`).

### Day 26: CLI-Driven Operations & Safe Dry-Run Audits
Integrating `argparse` directly into the batch auditing engine converts hardcoded Python scripts into versatile command-line tools:
* **Command-Line Interface (`argparse.ArgumentParser`)**: Configured custom terminal arguments (`--dir`, `--log-file`, `--dry-run`) allowing runtime target definitions without modifying source files.
* **Boolean Simulation Flag (`action="store_true"`)**: Implemented a `--dry-run` flag that validates target paths and streams preview logs (`🔍[Dry run] Would scan...`) without triggering heavy file reading or disk writes.
* **Dynamic Config & Logging Sync**: User-defined arguments dynamically dictate where logs are saved on disk (`log_path`) and which target directory (`args.dir`) is recursively audited.

### Day 27: Scalable Batch Processing & Analytics Export
Scaling batch operations to support high-volume file processing while ensuring reliable error tracing and runtime monitoring:
* **Performance Telemetry & Throughput**: Measured processing execution times using high-precision timers to calculate total duration and system throughput (files/sec).
* **Automated JSON Analytics Reports**: Standardized output telemetry by summarizing execution counts (total files, verified passes, failed assets) into an auto-generated `pipeline_report.json` file.
* **High-Volume Scale Resilience**: Ensured robust error capture during batch processing up to 10,000+ items without disrupting the broader pipeline lifecycle.

### Day 28: Media Asset Auditing & Classification Pipeline
Building an automated media auditor to scan nested workspace directories and organize multimedia assets based on format definitions:
* **Extension Set Classification**: Defined lookup sets (`IMAGE_EXTENSIONS`, `VIDEO_EXTENSIONS`) to swiftly sort media formats into specific asset categories.
* **File Metadata Extraction**: Utilized `file.stat().st_size` alongside `pathlib` utilities to convert raw bytes into readable megabyte metrics (`MB`) and aggregate cumulative storage size.
* **Terminal Summary Formatting**: Structured the audit pipeline to output structured counts and cumulative size calculations directly to standard output.

### Day 29: Modular Media Asset Scanner & Logging Integration
Decoupling asset auditing logic into independent, importable Python modules for cleaner architecture and reusability:
* **Modular Code Structure**: Separated pipeline responsibilities across `logger_config.py`, `asset_scanner.py`, and the main CLI driver script.
* **Centralized Pipeline Telemetry**: Configured a dedicated `PipelineLogger` instance to handle stream and file logging (`day29_run.log`) across modular execution boundaries.
* **Structured Dictionary Output**: Formatted scan outputs into a detailed dictionary tracking scanned file counts, isolated image/video lists, and cumulative storage totals.

### Day 30: PySide6 GUI for Media Asset Inspection
Transitioning pipeline tools to a Graphical User Interface using PySide6 widgets and layout managers:
* **Window & Layout Hierarchy**: Configured `QMainWindow` with central widgets, `QVBoxLayout`, and `QHBoxLayout` to arrange headers, input controls, and output areas cleanly.
* **Signal-Slot Event Connection**: Linked button click events (`clicked.connect`) to custom event handler functions (`handle_inspect_click`) for real-time user interaction.
* **Interactive Output Console**: Utilized read-only `QTextEdit` widgets as live visual consoles to stream inspection status, warnings, and system logs to the user interface.

### Day 31: Multi-Action Desktop GUI & Directory Dialogs
Extending the PySide6 Media Asset Manager with dynamic file dialogs and action handlers[cite: 25]:
* **Native OS Directory Picker (`QFileDialog`)**: Integrated `QFileDialog.getExistingDirectory` to allow users to interactively pick target workspace folders directly[cite: 22, 25].
* **Multi-Action Command Triggers**: Wired distinct push buttons (`Browse Directory`, `Run Audit`, `Run Manager`) to dedicated event handler methods (`folder_dialog`, `run_Audit`, `run_manager`)[cite: 22, 25].
* **Real-time Console Feedback**: Implemented defensive input checks in `run_Audit` and `run_manager` to alert users when no directory is selected before executing actions[cite: 22, 25].

### Day 32: Modern QSS Styling & Visual Feedback Interface
Overhauling the desktop GUI design using Qt Stylesheets (QSS) and visual task indicators:
* **Custom UI Aesthetics**: Applied modern CSS/QSS styling to customize buttons, header typography ("⚡ Pro Media Asset Manager"), input path bars, and container margins[cite: 22, 25].
* **Dark Console & Log Indicators**: Styled the read-only console area with a dark terminal background (`#11111B`) and color-coded status icons (⚠️ warnings, 🚀 operations, ✅ completion status)[cite: 22, 25].
* **Progress Bar Integration**: Added a stylized execution progress bar to provide real-time visual completion percentages during background audit and organization processes[cite: 22, 25].

### Day 33: Live Backend-GUI Integration & Dynamic Progress
Linking backend `pathlib` file scanner functions directly to the PySide6 desktop interface[cite: 22, 24, 25]:
* **Modular Backend Integration**: Connected `scanner.py` (`path_test`) into the main window driver (`main.py`) to execute live recursive asset scans (`rglob("*")`) on disk[cite: 22, 24, 25].
* **Dynamic Progress Percentage Calculations**: Iterated through scanned asset lists, calculating execution progress as `int((index / total_files) * 100)` to update `QProgressBar` in real time[cite: 22, 25].
* **Live GUI Frame Refreshing**: Integrated `QApplication.processEvents()` inside iteration loops to force PySide to render live console text and progress updates without freezing the interface[cite: 22, 25].

### Day 34: UI Message Abstraction & Logging Preparation
Preparing the Media Asset Manager for a professional logging system by separating user interface messaging from backend operations[cite: 22, 25]:
* **Centralized GUI Messaging**: Introduced a dedicated `show_message()` helper inside `MainWindow` to encapsulate all `QTextEdit` updates[cite: 22, 25].
* **Reduced Code Duplication**: Standardized message routing to streamline user interface updates and simplify logging integration[cite: 22, 25].
* **Separation of Concerns**: Isolated UI component operations from core processing logic to build a maintainable application architecture[cite: 22, 25].

### Lesson 35: Integrated Multi-Module Logging Engine
Integrating Python's standard `logging` library across the backend scanner and PySide6 application layers[cite: 21, 22, 24, 25]:
* **Dedicated Logging Module (`logger.py`)**: Designed a centralized logging utility configuring `basicConfig` with ISO-formatted timestamps, and helper functions (`log_info`, `log_warning`, `log_error`)[cite: 21, 25].
* **Backend File Telemetry**: Integrated logging statements directly into `scanner.py` (`path_test`) to log detected files, missing paths, and execution errors automatically during recursive directory scans[cite: 24, 25].
* **Dual GUI & System Telemetry**: Synchronized user-facing UI updates (`show_message()`) with systemic application logging inside `main.py` across all main window actions[cite: 22, 25].

### Lesson 36: Logging Architecture & StreamHandler
Moving beyond `logging.basicConfig()` to understand the internal architecture of Python's logging framework.
* **Manual Logger Configuration:** Replaced `logging.basicConfig()` with an explicitly configured `StreamHandler`, providing greater control over how log messages are processed.
* **Understanding Logging Architecture:** Learned the relationship between the application, logger, handlers, formatter, and final output destination.
* **StreamHandler:** Configured a dedicated `StreamHandler` responsible for sending log messages to the terminal while keeping the logger independent of the output destination.

### Lesson 37: Multi-Destination Logging with FileHandler
Expanding the logging system from a single output destination to a reusable multi-handler architecture.
* **FileHandler Integration:** Added a dedicated `FileHandler` to automatically write application logs to `app.log` while preserving terminal output.
* **Duplicate Handler Prevention:** Introduced `if not logger.handlers:` to prevent duplicate handlers from being attached when the logging module is imported multiple times.

### Lesson 38: Specialized Multi-Destination Logging & Auto-Organizer Module
Implementing modular file movement and deep source tracking across file and console logs[cite: 21, 23]:
* **Automated Category Mapping (`organizer.py`)**: Designed a rule-based organizer engine (`organize_folder`) using dictionary lookup sets (`EXTENSION_MAP`) to sort files into designated folders (Images, Videos, Code, etc.)[cite: 23].
* **Conflict Prevention Guardrails**: Safely checked `target_path.exists()` prior to moving files, recording skipped duplicate metrics and outputting clear log warnings[cite: 23].
* **Destination-Specific Formatters**: Applied independent `console_formatter` (clean output) and `file_formatter` (enriched with `filename`, `funcName`, and `lineno`) for enhanced debugging without cluttering console output[cite: 21].
* **Integrated PySide GUI Controls**: Wired `organize_folder()` into `main.py` under `run_organizer()`, updating progress bars, UI text widgets, and system logs simultaneously[cite: 22, 23].