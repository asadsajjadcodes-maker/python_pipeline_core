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
| **Day 24**| *Upcoming* | *Pending* | ⏳ Idiomatic Python |

---

## 🛠️ Tech Stack & Core Modules
* **Language:** Python 3.13+
* **Core Modules Used:** 
  * `pathlib` (Object-oriented filesystem paths)
  * `json` (JavaScript Object Notation encoder and decoder)
  * `sys` (System-specific parameters and functions)

---

## 📖 Lessons Learned

### Day 1 to Day 22: Path Automation & Loader Utilities
* **Data Pipelines & Ingestion:** Built end-to-end file management workflows, nested JSON dictionary accessors, and exception-safe loading functions (`safe_load_json`).

### Day 23: Complete JSON Persistence Suite (`safe_save_json`)
Pairing data ingestion utilities with a production-grade saver function completes the full I/O serialization workflow[cite: 4]:
* **Automatic Directory Provisioning (`mkdir`)**: Calling `target_path.parent.mkdir(parents=True, exist_ok=True)` automatically creates any missing parent directories before writing, preventing `FileNotFoundError` exceptions when outputting to new folders[cite: 4].
* **Write Failure Interception**:
  * `PermissionError`: Intercepts system write blocks when files are open in another process or restricted by OS permissions[cite: 4].
  * `TypeError`: Catches non-serializable Python objects (such as raw set objects or custom classes) before they corrupt the file stream[cite: 4].
* **Explicit Status Flagging**: Returning a boolean status (`True`/`False`) allows parent scripts to conditionally check output success before triggering downstream pipeline steps[cite: 4].

