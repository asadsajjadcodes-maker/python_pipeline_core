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
| **Day 26**| *Upcoming* | *Pending* | ⏳ Idiomatic Python |

---

## 🛠️ Tech Stack & Core Modules
* **Language:** Python 3.13+
* **Core Modules Used:** 
  * `pathlib` (Object-oriented filesystem paths)
  * `json` (JavaScript Object Notation encoder and decoder)
  * `logging` (Flexible event logging system for applications)
  * `sys` (System-specific parameters and functions)

---

## 📖 Lessons Learned

### Day 1 to Day 24: Batch Pipelines & File I/O
* **Batch Operations & Safety:** Combined recursive pattern search (`rglob`), safe load/save utilities, exception boundary protections, and automated mock dataset generation[cite: 5, 6].

### Day 25: Industrial Logging & Severity Telemetry
Replacing raw terminal `print()` statements with Python's built-in `logging` module elevates automation scripts into observable enterprise software[cite: 7]:
* **Dual-Channel Broadcasting (`handlers`)**: Initializing `logging.basicConfig()` with both `FileHandler` and `StreamHandler` writes persistent execution history to disk (`pipeline.log`) while echoing live progress directly to the terminal console[cite: 7, 8].
* **Standardized Severity Levels**:
  * `logging.info`: Tracks standard lifecycle operations (e.g., scanning asset files, batch completion totals)[cite: 7, 8].
  * `logging.warning`: Highlights non-fatal runtime anomalies (such as missing files on disk)[cite: 7, 8].
  * `logging.error`: Records serious structural faults (like JSON parsing syntax failures in non-JSON assets)[cite: 7, 8].
  * `logging.critical`: Reserves telemetry for severe system-level execution crashes[cite: 7].
* **ISO Timestamping & Log Formatting**: Configuring `format="%(asctime)s [%(levelname)s] %(message)s"` prepends standard date/time stamps and log level markers to every log line, making pipeline audits easy to parse[cite: 7, 8].
