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
| **Day 12**| *Upcoming* | *Pending* | ⏳ Idiomatic Python |

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
While `iterdir()` captures every single element within a folder, pipeline scripts often only care about specific asset types. `pathlib` offers an elegant, built-in pattern matcher called `.glob()` to handle this cleanly:
* **`current_repo.glob("*.py")`**: Uses the wildcard character `*` to fetch *only* items matching a specific extension or name criteria.
* **Efficiency Boost:** This pattern eliminates the need to manually fetch all items and run subsequent string or suffix logical checks, filtering the stream directly.

### Day 9: Safe and Deep Directory Creation
When pipelines automatically export files, you must make sure the targeted save directories exist on your machine before hitting write commands. `pathlib` provides `.mkdir()` to manipulate your system storage directly:
* **`.mkdir()`**: Instructs the operating system to construct a physical directory at the initialized path.
* **`parents=True`**: Forces Python to sequentially build every missing parent folder in the tree automatically.
* **`exist_ok=True`**: Turns it into an idempotent action—if the directory is already configured on disk, Python skips past gracefully without blowing up your automation pipeline.

### Day 10: Writing Data and Relocating Pipeline Assets
With foundational workspace checking and folder manipulation mastered, an automation pipeline must handle actual asset generation and moving procedures safely:
* **`.write_text("Data")`**: Directly opens a path, dumps string context inside it, and closes the stream in a single high-level action. Perfect for generating runtime logs, setting parameters, or building dummy manifests.
* **`.rename(destination_path)`**: Physically relocates a file or directory from its source path to a targeted destination path. 
* **Pipeline Safety Check:** Combining `.exists()` validation checks prior to running a `.rename()` function ensures that missing storage trees are automatically initialized via `.mkdir(parents=True)` first. This design pattern completely prevents file migration crashes.

### Day 11: Context Managers & Safe File Streaming (File I/O)
When writing log frameworks or exporting pipeline asset histories, open system streams must be managed meticulously to prevent memory leaks and file corruption:
* **`with open(...)` Context Manager:** Guarantees that the underlying file buffer stream closes cleanly immediately after the nested code block completes execution, even if runtime syntax exceptions occur mid-stream.
* **Append Mode (`mode="a"`)**: Opens an asset file for writing without erasing historic telemetry. New input strings generated via `.write()` are pushed strictly to the tail end of the file data—critical for sequential engine export manifests.
* **Read Mode (`mode="r"`) & Iteration:** Opens files strictly for data ingestion. Accessing lines sequentially via a `for line in f:` syntax structure sweeps entries row-by-row, while string cleanup tools like `.strip()` truncate annoying trailing carriage returns (`\n`) or loose padding spaces cleanly.
* **Explicit Encoding (`encoding="utf-8"`)**: Enforcing text formatting standardizations explicit within file interaction pipelines protects pipeline structures from throwing multi-platform decoding errors when handling complex asset metadata scripts.
