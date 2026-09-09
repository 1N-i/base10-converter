# 🔢 Base Converter

![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python)

A modular Python utility designed to convert numbers between arbitrary numeral bases (from Base 2 up to Base 36) using Base 10 as an intermediate bridge.

## 📋 Summary
- [Technologies](#-technologies)
- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [What I Learned](#-what-i-learned)
- [Future Improvements](#-future-improvements)
- [How to Run](#-how-to-run)

---

## 🛠 Technologies
- **Python 3.x**: Core logic and base conversion calculations.

## ✨ Features
- **Base to Decimal Conversion:** Translates string representations of numbers from any base (2–36) into Base 10.
- **Decimal to Any Base Conversion:** Converts Base 10 integer values into any base targeted (2–36).
- **Universal Base Converter:** Direct conversions from Base X to Base Y by using Base 10 intermediary processing.
- **Alphanumeric Mapping:** Utilizes `0-9` and `A-Z` characters to support higher base representations.

## 📂 Project Architecture
The project is structured into individual functions separating each stage of conversion:
* `Base_ToBase10.py`: Script containing logic to convert an input string from a specified base into a decimal integer.
* `Base10ToBase_.py`: Script containing logic to convert a decimal integer into a string of a target base.
* `BaseXToBaseY.py`: Main module importing both functions to perform complete base-to-base transitions.

## 📚 What I Learned
* **Positional Systems:** Utilizing positional weight indices and polynomial arithmetic to compute decimal totals.
* **Modulo Arithmetic:** Applying integer division (`//`) and modulo (`%`) loops to extract digits.
* **Modular Integration:** Importing specialized functions across python modules to create a unified function pipeline.

## 🔮 Future Improvements
- [X] Implement reverse conversion (Base-N to Base 10).
- [X] Add support for direct Base-A to Base-B conversion
- [ ] Add input validation to ensure number / string characters match the original base domain.
- [X] Support negative numbers.
- [ ] Support floating-point.
- [ ] Build a Command-Line Interface (CLI) for interactive terminal user input.
