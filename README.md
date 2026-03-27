# 🧾 Billing System 

A simple terminal-based Python application that allows users to register products, validate input data, and calculate the total cost of each product using a modular approach.

---

## 📖 Project Overview

This project is a basic **billing system** that lets users input product information (name, price, and quantity), validates the data, and calculates the total cost.

The system uses a **modular design**, separating validation logic from the main program to ensure clean code and better maintainability.

---

## 🚀 Key Features

* ✔ Product registration from console
* ✔ Input validation using reusable functions
* ✔ Text validation (only letters and spaces allowed)
* ✔ Numeric validation (positive numbers only)
* ✔ Automatic total calculation (price × quantity)
* ✔ Continuous execution until user decides to exit

---

## 🧠 Technologies Used

* Python 3.x
* Standard Library only (no external dependencies)

---

## 📁 Project Structure

* `SysFacturacio.py` → Main program (handles user interaction and logic flow)
* `Fun_validations.py` → Validation module with reusable functions
* `README.md` → Project documentation

---

## ⚙️ How the System Works

1. The program starts a loop that allows continuous product registration

2. The user is asked to enter:

   * Product name
   * Product price
   * Product quantity

3. Input validation is applied:

   * `validate_text()` ensures the name is not empty and contains only letters
   * `validate_number()` ensures numeric values are valid and positive

4. The system calculates:

   * **Total cost = price × quantity**

5. The result is displayed in a formatted output

6. The user decides whether to continue or exit the program

---

## 🧩 Validation Strategy

The system uses **recursive validation functions**, which means:

* If the user enters invalid data, the function calls itself again
* This ensures the program never crashes due to incorrect input
* Guarantees clean and reliable data for processing

---

## ▶️ Installation & Execution

### 1. Clone the repository

```bash
git clone https://github.com/JromeroRodriguez/Historia-de-usuario-M1S1.git
```

### 2. Navigate to the project folder

```bash
cd your-repo
```

### 3. Run the program

```bash
python SysFacturacio.py
```

---

## 🧪 Example Execution

```
--- Registro de Producto ---

Ingrese el nombre del producto: arroz
Ingrese el precio del producto: 2000
Ingrese la cantidad del producto: 3

Producto: arroz | Precio: $2000.00 | Cantidad: 3 | Total: $6000.00
```

---

## ⚠️ Important Notes

* The system prevents invalid input through recursion
* Only positive numbers are allowed for price and quantity
* The program runs continuously until the user chooses to exit

---

## 📈 Future Improvements

* Store billing data in a CSV file
* Add multiple product invoices
* Generate total invoice summaries
* Implement a graphical interface (Tkinter)

---

## 📊 Flowchart

Below is the system flowchart:

<img width="544" height="773" alt="CAPTURE" src="https://github.com/user-attachments/assets/25710785-a1b3-45ba-b84e-4545b6d06f11" />



---

## 👨‍💻 Author

Joseph Romero
Software Development Student
