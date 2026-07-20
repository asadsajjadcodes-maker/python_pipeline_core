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
| **Day 23**| *Upcoming* | *Pending* | ⏳ Idiomatic Python |

---

## 🛠️ Tech Stack & Core Modules
* **Language:** Python 3.13+
* **Core Modules Used:** 
  * `pathlib` (Object-oriented filesystem paths)
  * `json` (JavaScript Object Notation encoder and decoder)
  * `sys` (System-specific parameters and functions)

---

## 📖 Lessons Learned

### Day 1 to Day 21: Foundations to Exception Handling
* **Path Management & Serialization:** Engineered dynamic file paths, context-managed file handles, and structured JSON Read-Modify-Write cycles with nested lookups.
* **Fault Isolation:** Advanced from basic `sys.exit()` script terminations to structured `try/except` blocks handling `FileNotFoundError` and `json.JSONDecodeError` cleanly.

### Day 22: Building Production Helper Utilities
Moving from inline scripts to modular helper functions converts single-use code into software utilities that scale across complex tools:
* **Production Utility Packaging (`safe_load_json`)**: Encapsulating file operations within a dedicated helper function simplifies data loading down to a single function call, abstracting away boilerplates like open modes, character encoding, and error handlers[cite: 3].
* **Dynamic Parameter Fallbacks (`default_fallback=None`)**: Setting standard default arguments permits flexible function calls[cite: 3]. If a custom fallback payload is passed (e.g., `default_fallback={"status": "missing_asset"}`), the loader uses it; otherwise, it initializes a clean default empty dictionary (`{}`)[cite: 3].
* **Comprehensive Error Cascading**:
  * `FileNotFoundError`: Gracefully intercepts missing file paths and returns the defined fallback payload[cite: 3].
  * `json.JSONDecodeError`: Catches corrupted or invalid JSON data structures on disk[cite: 3].
  * `except Exception`: Serves as a ultimate safety net to handle unexpected system disruptions (e.g., disk permissions or IO errors) without terminating execution[cite: 3].

