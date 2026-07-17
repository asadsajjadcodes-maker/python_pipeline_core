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
| **Day 18**| *Upcoming* | *Pending* | ⏳ Idiomatic Python |

---

## 🛠️ Tech Stack & Core Modules
* **Language:** Python 3.13+
* **Core Modules Used:** 
  * `pathlib` (Object-oriented filesystem paths)
  * `json` (JavaScript Object Notation encoder and decoder)
  * `sys` (System-specific parameters and functions)

---

## 📖 Lessons Learned

### Day 1 to Day 16: Path Automation & JSON Foundations
* **Path & Directory Operations:** Mastered `pathlib.Path` objects, wildcard search mechanics via `.glob()`, deep path navigation, and idempotent directory creation via `.mkdir(parents=True, exist_ok=True)`.
* **Streaming & JSON I/O:** Built stream-safe file handlers with `with open()`, engineered string lookups using `.lower()`, and handled single-file JSON serialization (`json.dump()`) and deserialization (`json.load()`) alongside defensive `sys.exit()` error guardrails.

### Day 17: In-Memory JSON Modifications & Read-Modify-Write Cycle
Updating persistent configuration state on disk is a core requirement for automated pipelines (e.g., updating mesh vertex counts after a LOD optimization pass or flagging asset compilation flags):
* **The Read-Modify-Write Design Pattern**:
  1. **Read:** Ingest the existing disk state into memory using `json.load()` within a read-stream block (`mode="r"`).
  2. **Modify:** Mutate dictionary keys (`config_data["vertex_count"] = 9999`) or inject new key-value tracking pairs (`config_data["optimization_completed"] = True`) natively in memory.
  3. **Write:** Re-open the target file in write mode (`mode="w"`) and overwrite disk storage with `json.dump(config_data, f, indent=4)`.
* **Dynamic Key Injection**: Because deserialized JSON objects behave as standard Python dictionaries, inserting new tracking metadata keys requires no schema pre-definition—assigning a value to a new key updates the structure automatically prior to serialization.

