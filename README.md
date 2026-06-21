# python_pipeline_core

A repository dedicated to mastering Python automation, core programming workflows, and building robust backend pipelines. This project tracks daily progress, shifting from foundational concepts to advanced modular automation scripts.

## 📅 Daily Progress Tracker

| Day  | Topic | Description | Status |
| :--- | :--- | :--- | :--- |
| **Day 1** | Smart File Handling (`pathlib`) | Transitioning from raw string manipulation to object-oriented path handling. |  Done |
| **Day 2** | *Upcoming* | *Pending* | ⏳ Idiomatic Python |

---

## 🛠️ Tech Stack & Core Modules
* **Language:** Python 3.13+
* **Core Modules Used:** * `pathlib` (Object-oriented filesystem paths)

---

## 📖 Lessons Learned

### Day 1: Pathlib vs. Raw Strings
* **Raw Strings:** Treating a file path or name as a pure string limits flexibility and can break across different operating systems (Windows `\` vs. Mac/Linux `/`).
* **Path Objects:** Using `pathlib.Path` converts a string into a "smart object," allowing instant access to file properties:
  * `.name` retrieves the full filename.
  * `.suffix` extracts the file extension.
  * `.cwd()` dynamically finds the current working directory.

---


