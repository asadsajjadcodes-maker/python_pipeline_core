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
| **Day 9** | *Upcoming* | *Pending* | ⏳ Idiomatic Python |

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
* **`.exists()`**: Returns `True` if the path points to an actual file or directory on the system.
* **`.is_file()`**: Returns `True` only if the path points explicitly to a file.
* **`.is_dir()`**: Returns `True` if the path is a folder/directory.

### Day 5: Cross-Platform Path Joining
Hardcoding path separators like backward slashes (`\`) or forward slashes (`/`) makes scripts fragile and error-prone. `pathlib` solves this elegantly by overloading the division (`/`) operator to combine paths:
* **The `/` Operator:** Link directory paths, sub-folders, and final asset names using `/`.
* **Smart Handling:** Python automatically identifies the host operating system and injects the correct system-specific separator.

### Day 6: Immutable Path Modifications & Swapping
When constructing asset pipelines, you frequently need to generate paths for derivative or processed files. `pathlib` provides path-manipulation techniques that return entirely new path objects without altering the original baseline path:
* **`.with_name("new_name.ext")`**: Retains the exact directory hierarchy but swaps out the final file name and extension entirely.
* **`.with_suffix(".new_ext")`**: Preserves the parent directories and the target filename, swapping out only the trailing extension.
* **Method Chaining:** Sequentially link methods together (e.g., `path.with_name("mesh.fbx").with_suffix(".obj")`) to transform file anatomy components in a single readable line.

### Day 7: Scanning Directories with Iterdir
To automate batch processes, you must look inside directories dynamically. 
* **`.iterdir()`**: Yields an iterator containing `Path` objects for every single item inside that directory, including folders and hidden configurations.
* **Combining with Filters:** By looping through an `.iterdir()` sequence and wrapping it in conditional checks (like `if item.is_file()`), scripts can instantly skip over nested sub-folders to isolate and operate only on target files.

### Day 8: Pattern Matching via Globbing
While `iterdir()` captures every single element within a folder, pipeline scripts often only care about specific asset types (e.g., extracting only Python scripts, FBX meshes, or PNG textures). `pathlib` offers an elegant, built-in pattern matcher called `.glob()` to handle this cleanly:
* **`current_repo.glob("*.py")`**: Uses the wildcard character `*` to fetch *only* items ending in `.py`.
* **Efficiency Boost:** This pattern eliminates the need to manually fetch all items and run subsequent `if item.suffix == ".py"` logical checks. It returns an iterator yielding matching path objects directly, making asset ingestion pipelines significantly faster and cleaner.

