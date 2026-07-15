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
| **Day 16**| *Upcoming* | *Pending* | ⏳ Idiomatic Python |

---

## 🛠️ Tech Stack & Core Modules
* **Language:** Python 3.13+
* **Core Modules Used:** * `pathlib` (Object-oriented filesystem paths)
  * `json` (JavaScript Object Notation encoder and decoder)

---

## 📖 Lessons Learned

### Day 1 to Day 14: Path Automation & Text Processing
* **Path Operations:** Mastered `pathlib.Path` structures, relative traversing, safe disk checks, wildcard pattern matching via `.glob()`, and safe nested directory initialization with `.mkdir(parents=True, exist_ok=True)`.
* **Resource Context & String Parsing:** Built robust streaming channels using `with open()`, handled key-value split limits via `maxsplit=1`, designed QA scanners using `.lower()`, and performed in-memory text updates via `.replace()`.

### Day 15: Structured Configuration Management (JSON Serialization)
While plain text logs are great for visual verification, production software architectures rely on standardized structured formats like JSON (JavaScript Object Notation) to store complex asset settings, mesh properties, and environment profiles:
* **Python Dictionaries to JSON Objects**: Python dictionaries align natively with JSON objects. Passing asset data containing key types such as integers, booleans, lists, and strings allows complex nested configurations to be preserved cleanly.
* **Stream Serialization (`json.dump(obj, fp)`)**: Instead of manually formatting string brackets or key quotes, `json.dump()` converts Python dictionary structures into valid JSON schema directly over an open file buffer context stream (`mode="w"`).
* **Pretty Printing (`indent=4`)**: Supplying the `indent=4` keyword argument forces the JSON serializer to output clean, line-broken, and properly indented code structures instead of a single compressed raw data line. This makes generated config files easily human-readable and git-diff friendly.

