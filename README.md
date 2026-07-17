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
| **Day 19**| *Upcoming* | *Pending* | ⏳ Idiomatic Python |

---

## 🛠️ Tech Stack & Core Modules
* **Language:** Python 3.13+
* **Core Modules Used:** 
  * `pathlib` (Object-oriented filesystem paths)
  * `json` (JavaScript Object Notation encoder and decoder)
  * `sys` (System-specific parameters and functions)

---

## 📖 Lessons Learned

### Day 1 to Day 17: Workspace Management & JSON Cycles
* **Path & Configuration Lifecycle:** Mastered `pathlib.Path` environments, file modification pipelines, and multi-layered directory verification rules.
* **JSON Read-Modify-Write Patterns:** Completed the data loop by combining `json.load()` and `json.dump()` to dynamically mutate, append, and overwrite configuration data on local disks safely.

### Day 18: Defensive Coding via Dictionary Fallbacks
In automated asset pipelines, you cannot always guarantee that an incoming JSON configuration contains every single parameters key your script expects. Accessing a missing key using standard bracket notation (e.g., `data["missing_key"]`) will immediately crash your execution thread with a `KeyError`.
* **The Safe `.get()` Method**: Calling `.get("key_name")` intercepts missing keys gracefully. Instead of raising a fatal runtime exception, it returns a placeholder value if the target property is missing from the JSON schema.
* **Explicit Default Values**: Supplying a secondary argument (e.g., `config_data.get("lod_count", 1)`) provides an intentional fallback value. If the key exists, Python utilizes the file's data; if it is absent, it seamlessly defaults to the pipeline's fallback parameters (such as a default of `1` for LOD layers or `100` for baseline vertex tracking tolerances).
* **Implicit Safe Defaults**: When a secondary parameter is omitted (e.g., `config_data.get("pipeline_status")`), Python implicitly falls back to returning `None` instead of breaking your environment loop. This permits quick, clean conditional evaluations downstream.

