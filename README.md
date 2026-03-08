# Apex

A simple utility project that provides a small command-line tool for sorting files in a directory into subfolders.


## 📦 What it does

`sort_files.py` can organize files in a directory by:

- **Extension** (default, e.g., `.jpg` → `jpg/`)
- **Date** (year-month based on file modification time, e.g., `2026-03/`)
- **Size** (buckets like `small`, `medium`, `large`, `huge`)
- **Name** (group by first letter, e.g., `A/`, `B/`, `_other/`)

## 🚀 Usage

```bash
python sort_files.py <target-dir> [--mode extension|date|size|name] [--recursive] [--dry-run]
```

### Examples

```bash
python sort_files.py "C:\\Users\\You\\Downloads"
python sort_files.py ./workspace --mode date --recursive
python sort_files.py ./workspace --mode size --dry-run
```

## 🧩 Notes

- Runs on Windows/macOS/Linux with Python 3.8+.
- `--dry-run` shows what would happen without moving files.
- Files are moved into subfolders under the target directory.

---

Created for quick file organization tasks.
