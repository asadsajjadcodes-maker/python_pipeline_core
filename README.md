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
| **Day 15**| *Upcoming* | *Pending* | ⏳ Idiomatic Python |

---

## 🛠️ Tech Stack & Core Modules
* **Language:** Python 3.13+
* **Core Modules Used:** * `pathlib` (Object-oriented filesystem paths)

---

## 📖 Lessons Learned

### Day 1 to Day 13: Core Automation & Text Search
* **Path Management:** Advanced from raw strings to platform-agnostic directory handling, validation checks, deep directory building with `.mkdir(parents=True)`, and pattern filtering with `.glob()`.
* **Resource Context & Parsing:** Implemented safe file operations using `with open()` context managers, limited splits via `.split(maxsplit=1)` to handle timestamps safely, and used `.lower()` with membership operators (`in`) to create case-insensitive search logic for QA reporting.

### Day 14: Reading, Modifying, and Replacing Data
As automation pipelines grow, they frequently need to update configuration values, patch asset names in text files, or fix outdated metadata keys without manual human intervention:
* **Whole-File Ingestion (`.read()`)**: While looping through a file line-by-line is perfect for scanning and parsing, calling `.read()` directly on a file context pulls the entire file contents into a single string variable, making global text replacements easy.
* **String Replacements (`.replace("old", "new")`)**: Python's native `.replace()` method sweeps through the string and cleanly swaps target values (e.g., updating asset name `"SM_Castle_Gate"` to `"SM_Castle_Gate_V02"`) instantly. Because strings are immutable, this generates a brand-new modified string while keeping your original variables safe.
* **Pipeline Applications**: This is a core technique used for rewriting asset paths, modifying environment configurations dynamically, or bulk renaming references inside scene files, settings files, or logs.

---