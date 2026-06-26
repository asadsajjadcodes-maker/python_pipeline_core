# Python Pipeline Core

A repository dedicated to mastering Python automation, core programming workflows, and building robust backend pipelines. This project tracks daily progress, shifting from foundational concepts to advanced modular automation scripts.

## 📅 Daily Progress Tracker

| Day  | Topic | Description | Status |
| :--- | :--- | :--- | :--- |
| **Day 1** | Smart File Handling (`pathlib`) | Transitioning from raw string manipulation to object-oriented path handling. | ✅ Done |
| **Day 2** | Path Anatomy Deep Dive | Breaking down asset paths using `.name`, `.stem`, and `.suffix` properties. | ✅ Done |
| **Day 3** | Directory Hierarchy Navigation | Traversing parent and grandparent folder levels dynamically using `.parent`. | ✅ Done |
| **Day 4** | Path Validation & Verification | Confirming item existence and distinguishing files from directories safely. | ✅ Done |
| **Day 5** | *Upcoming* | *Pending* | ⏳ Idiomatic Python |

---

## 🛠️ Tech Stack & Core Modules
* **Language:** Python 3.13+
* **Core Modules Used:** * `pathlib` (Object-oriented filesystem paths)

---

## 📖 Lessons Learned

### Day 1: Pathlib vs. Raw Strings
* **Raw Strings:** Treating a file path or name as a pure string limits flexibility and can break across different operating systems.
* **Path Objects:** Using `pathlib.Path` converts a string into a "smart object," allowing dynamic properties access.

### Day 2: Anatomy of a Path File
When working with pipeline assets, `pathlib` makes it easy to dissect a file's name properties without messy string splitting:
* **`.name`**: Returns the complete filename including the extension.
* **`.stem`**: Extracts the pure file name *without* the extension.
* **`.suffix`**: Returns only the file extension type including the dot.

### Day 3: Traversing Directory Trees
When managing complex game dev asset structures, you frequently need to find where an asset sits relative to its project environment. `pathlib` handles tree traversal cleanly through property chaining:
* **`.parent`**: Retrieves the full path of the immediate directory enclosing the asset.
* **`.parent.parent`**: Traverses up another tier to get the grandparent folder path.
* **`.parent.name`**: Isolates just the string name of the parent folder itself.

### Day 4: Path Validation
Before running automation scripts that modify, copy, or delete assets, verifying that target files or folders actually exist prevents script crashes. `pathlib` handles this with built-in validation methods:
* **`.exists()`**: Returns `True` if the path points to an actual file or directory on the system, and `False` if it does not (like looking for a missing asset).
* **`.is_file()`**: Returns `True` only if the path points explicitly to a file, preventing your code from accidentally treating directories like individual assets.
* **`.is_dir()`**: Returns `True` if the path is a folder/directory. Passing an empty string `Path("")` represents the current working directory, which evaluates correctly as a directory (`.`).
