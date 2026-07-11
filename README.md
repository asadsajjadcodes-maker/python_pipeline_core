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
| **Day 14**| *Upcoming* | *Pending* | ⏳ Idiomatic Python |

---

## 🛠️ Tech Stack & Core Modules
* **Language:** Python 3.13+
* **Core Modules Used:** * `pathlib` (Object-oriented filesystem paths)

---

## 📖 Lessons Learned

### Day 1 to Day 12: Path and Parsing Foundations
* **Path Management:** Progressed from `pathlib.Path` configurations, structural traversing, safe validation routines, pattern filters via `.glob()`, and idempotent folder trees via `.mkdir(parents=True, exist_ok=True)`.
* **Resource Context Manipulation:** Mastered basic string partitioning via `.split(maxsplit=1)` and managed raw multi-platform file stream architectures securely via text context blocks.

### Day 13: Conditional Stream Querying & Automated QA Scanning
When dealing with massive production log outputs, pipeline managers must programmatically scan text logs for specific system errors, successes, or alerts instead of auditing files line-by-line:
* **Case Insensitivity Safeguards (`.lower()`)**: Hardcoded string lookups often fail if a script logs `"ERROR"`, `"error"`, or `"Error"`. Normalizing lines on ingest using `line.lower()` guarantees condition structures reliably intercept targets regardless of system formatting inconsistencies.
* **Substring Membership Testing (`in` Operator)**: Using Python's native `in` evaluation allows fast, highly readable text inspection to trace whether critical pipeline markers exist within rows.
* **Visual Status Reporting & QA Flags**: Incorporating custom tracking parameters—such as matching success statements with green operational flags (🟢) or failure statements with red indicators (🔴)—turns a dense console stream into an easily readable visual audit board.

