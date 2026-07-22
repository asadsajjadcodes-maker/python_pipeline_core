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
| **Day 25**| *Upcoming* | *Pending* | ⏳ Idiomatic Python |

---

## 🛠️ Tech Stack & Core Modules
* **Language:** Python 3.13+
* **Core Modules Used:** 
  * `pathlib` (Object-oriented filesystem paths)
  * `json` (JavaScript Object Notation encoder and decoder)
  * `sys` (System-specific parameters and functions)

---

## 📖 Lessons Learned

### Day 1 to Day 23: Reusable Utility Architecture
* **I/O Helpers:** Integrated `safe_load_json` and `safe_save_json` functions to encapsulate error handling, directory creation, and serialization boundaries[cite: 6].

### Day 24: Programmatic Mock Datasets & Batch Processing Engine
Scaling automation from single assets to studio-wide pipelines requires both automated test-data generation and batch processing systems[cite: 5, 6]:
* **Automated Dataset Generation (`batch_json_files_genrator.py`)**: Programmatically populating test datasets via loops (`range(101)`) allows developers to stress-test pipeline loops against bulk data files in seconds[cite: 5].
* **Recursive Pattern Discovery (`rglob`)**: Utilizing `input_path.rglob("*.json")` traverses input folders and subfolders to extract all targeted configuration assets automatically[cite: 6].
* **Modular Pipeline Integration**: Connecting standalone utility helpers (`safe_load_json` and `safe_save_json`) directly into the processing loop ensures each individual file step benefits from built-in try/except safety nets[cite: 6].
* **Fault Isolation (`continue`)**: When corrupted or unreadable files return `None`, using the `continue` keyword skips downstream processing for that single item without halting the entire batch loop[cite: 6].
* **Execution Telemetry**: Tracking runtime metrics via `success_count` and `fail_count` generates clear batch summary reports (`Batch summary: X succeeded | Y failed`), giving pipeline developers instant visibility into execution health[cite: 6].
