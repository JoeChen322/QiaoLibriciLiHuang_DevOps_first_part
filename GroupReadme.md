## 🧪 Step 1: Testing the Buggy Grayscale Implementation

### ✅ Objective

The purpose of this step was to evaluate a precompiled grayscale conversion function, `convertToGrayscale(...)`, and verify its correctness using **unit tests** written with **Google Test**. The goal was to **design test cases that expose bugs** in the implementation across multiple grayscale modes.

---

### 🧪 Test Design Strategy

We focused on the following grayscale methods:

* **RedChannel**
* **GreenChannel**
* **BlueChannel**
* **Average**
* **Luminosity**
* **Multi-pixel matrices**

Each test was constructed to:

* Isolate individual RGB components.
* Use clear expected values for easy validation.
* Include **edge cases** such as overflows, negative values, and uniform colors.
* Validate correctness on **single-pixel** and **multi-pixel (2x2)** images.

---

### 📂 Key Test Cases

| Test Name                   | Method       | Input RGB       | Expected Output | Actual Output    | Finding                                                                |
| --------------------------- | ------------ | --------------- | --------------- | ---------------- | ---------------------------------------------------------------------- |
| `RedChannelConversion`      | RedChannel   | (255, 0, 0)     | 255             | 0                | Red channel is ignored or zeroed.                                      |
| `RedUsesOnlyRedComponent`   | RedChannel   | (120, 45, 200)  | 120             | 440              | Red channel is likely being mixed with others.                         |
| `GreenIsolatedCorrectly` ✅  | GreenChannel | (10, 220, 5)    | 220             | 220              | ✅ Correct behavior — green is correctly isolated.                      |
| `BlueChannelCorrectness`    | BlueChannel  | (0, 0, 255)     | 255             | 198              | Blue value is being altered — likely mixing in red/green.              |
| `AverageOfUniformColor`     | Average      | (100, 100, 100) | 100             | 234              | Arithmetic mean logic is incorrect.                                    |
| `AverageHandlesHighValues`  | Average      | (255, 255, 255) | 255             | 510              | No clamping or overflow handling.                                      |
| `AverageWithNegativeValues` | Average      | (-100, 50, 100) | 16              | -36              | Negative input mishandled — likely no bounds check.                    |
| `MultiPixelAverage`         | Average      | 2x2 matrix      | 20, 60, 90, 85  | 48, 106, 57, 148 | Multi-pixel results all incorrect — likely iteration or formula error. |
| `LuminosityConversion`      | Luminosity   | (255, 255, 255) | 255             | 508              | Output not clamped — incorrect formula or scaling.                     |

> 💡 Note: All tests were built and executed using a custom CMake-based build system and `gtest_main` linked via Git submodules.

---

### 🔍 Summary of Findings

* The implementation **fails 9 out of 10 test cases**.
* Only **GreenChannel** passed reliably.
* Major issues include:

  * **Incorrect channel usage or mixing**.
  * **Lack of clamping** for values > 255.
  * **Failure to handle negatives** gracefully.
  * **Incorrect averaging and matrix traversal**.
