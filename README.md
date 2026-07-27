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

---

## 🛠️ Tech Stack & Core Modules
* **Language:** Python 3.13+
* **Core Modules Used:** 
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
Building an automated media auditor to scan nested workspace directories and organize multimedia assets based on format definitions[cite: 4]:
* **Extension Set Classification**: Defined lookup sets (`IMAGE_EXTENSIONS`, `VIDEO_EXTENSIONS`) to swiftly sort media formats into specific asset categories[cite: 4].
* **File Metadata Extraction**: Utilized `file.stat().st_size` alongside `pathlib` utilities to convert raw bytes into readable megabyte metrics (`MB`) and aggregate cumulative storage size[cite: 4].
* **Terminal Summary Formatting**: Structured the audit pipeline to output structured counts and cumulative size calculations directly to standard output[cite: 4].