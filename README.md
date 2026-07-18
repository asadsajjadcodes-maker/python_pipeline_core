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
| **Day 20**| *Upcoming* | *Pending* | ⏳ Idiomatic Python |

---

## 🛠️ Tech Stack & Core Modules
* **Language:** Python 3.13+
* **Core Modules Used:** 
  * `pathlib` (Object-oriented filesystem paths)
  * `json` (JavaScript Object Notation encoder and decoder)
  * `sys` (System-specific parameters and functions)

---

## 📖 Lessons Learned

### Day 1 to Day 18: Core Pipelines & Defensive Access
* **Workspace Management:** Built complex cross-platform environments, performed validations, and managed files via iterative search boundaries.
* **Defensive Schema Parsing:** Mastered basic file configuration reading and safe lookup access via the `.get()` utility to return fallback values rather than triggering a `KeyError`.

### Day 19: Chained Lookups & Nested Object Safeguards
In production data architectures, configuration data rarely sits entirely flat. Profiles typically nest metadata groups inside separate sub-objects (e.g., placing engine build statuses inside a `pipeline_details` object, inside a broader parent `metadata` map):
* **Chained Dictionary Lookups**: Standard key indexing cascades errors heavily if you try to step through multiple levels (e.g., `data["metadata"]["pipeline_details"]["version"]`) when any higher-level key is absent. Chaining `.get()` methods allows safe traversal deep into nested tree hierarchies.
* **Empty Dictionary Fallbacks (`{}`)**: When chaining lookups down a nested tree, supplying an empty dictionary as the fallback target (e.g., `.get("metadata", {})`) guarantees that even if a parent key is completely missing from the target JSON file, the next chained `.get()` executes smoothly against a blank dictionary object rather than trying to evaluate a `NoneType`, completely preventing application crashes.
* **Collections Validation**: Fetching array collections (like `lod_settings`) via fallback targets like `.get("key", [])` ensures the returned variable behaves safely as a native Python list. This enables downstream collection evaluations like indexing (`list[0]`) or array length checks (`len()`) to loop seamlessly without checking types.

