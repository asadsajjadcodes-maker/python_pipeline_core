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
| **Day 17**| *Upcoming* | *Pending* | ⏳ Idiomatic Python |

---

## 🛠️ Tech Stack & Core Modules
* **Language:** Python 3.13+
* **Core Modules Used:** 
  * `pathlib` (Object-oriented filesystem paths)
  * `json` (JavaScript Object Notation encoder and decoder)
  * `sys` (System-specific parameters and functions)

---

## 📖 Lessons Learned

### Day 1 to Day 15: Path Automation, File I/O & JSON Serialization
* **Path & Directory Mechanics:** Mastered dynamic path navigation, validation routines, wildcard matching via `.glob()`, and safe idempotent tree creation using `.mkdir(parents=True, exist_ok=True)`.
* **Streaming & Data Processing:** Built safe streaming channels with `with open()`, constructed key-value log parsers with `maxsplit=1`, developed case-insensitive search scripts, and serialized Python dictionary objects into clean, indented JSON files via `json.dump()`.

### Day 16: Deserialization, Native Data Restorations, and System Guardrails
Reading external configurations safely back into Python code completes the full cycle of pipeline data persistence:
* **JSON Deserialization (`json.load(fp)`)**: Converts JSON schema strings from a file directly back into native Python objects (dictionaries, lists, integers, booleans) without requiring manual string conversion or parsing.
* **Automatic Type Restoration**: Native types stored in JSON retain their proper Python datatypes upon ingestion. A JSON boolean `true` automatically reconstructs as Python's `<class 'bool'>` (`True`), allowing immediate boolean logical checks in pipeline scripts without string casts.
* **Graceful Exit Guardrails (`sys.exit(1)`)**: Checking if a configuration file exists via `.exists()` *before* opening prevents unhandled `FileNotFoundError` exceptions. Calling `sys.exit(1)` terminates execution immediately with an explicit non-zero exit code, communicating script failure cleanly to parent automation orchestrators or CI/CD pipelines.

