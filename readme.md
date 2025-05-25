```markdown
# SE4HPC – Task 1: Unit Testing & CI Pipeline

## 🎯 Objective

This repository contains the implementation of **Task 1** for the Software Engineering for HPC course. It focuses on developing **unit tests** for a C++ grayscale image conversion tool and automating their execution through a **GitHub Actions CI pipeline**.

---

## 👥 Group Members

| Name                     | Person Code |
|--------------------------|-------------|
| Salvatore Mariano Librici | 11078653    |
| Rong Huang               | 10948935    |
| Yibo Li                  | 11022291    |
| Zhaochen Qiao            | 11021721    |

---

## 🧪 Test Cases

We implemented unit tests for the `convert_grayscale` functionality using Google Test. The tests validate:

- ✅ Correct grayscale conversion using different methods:
  - Average
  - Luminosity
  - Lightness

- ✅ Proper error handling for:
  - Missing or malformed input files
  - Edge cases like empty files or single-pixel images

---

## ⚙️ CI Pipeline (GitHub Actions)

A continuous integration pipeline is triggered on every `push` and `pull request` to the repository. The pipeline includes:

1. ✅ Repository checkout
2. ✅ CMake configuration
3. ✅ Build using `g++`
4. ✅ Execution of unit tests via Google Test
5. ✅ Automatic test result reporting to GitHub

This ensures immediate feedback on code changes and prevents regressions.

---

## 🛠️ Project Structure

```

.
├── CMakeLists.txt         # CMake configuration
├── include/               # Header files
├── src/                   # Implementation files
├── test/                  # Google Test cases
└── .github/workflows/
└── ci.yml             # GitHub Actions pipeline definition

```

---

## 🧩 Difficulties Faced

### ✅ Solved

- **Google Test setup**: Integrated GTest as a submodule and resolved linking issues.
- **CI environment issues**: Addressed missing package errors by installing system dependencies in the workflow.

### ❌ Remaining

- Some tests depend on external files (e.g., image data), which slows down test runs and complicates mocking.

---

## 📄 License

This repository is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.