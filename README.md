# 🥕 Enanito’s Verdulería – Order Management System

A command-line Python application for managing vegetable orders and customer data, built as a university project for the course *Algorithms and Programming I* (University of Buenos Aires).

The system allows users to **add**, **modify**, **delete**, and **list** vegetable orders and associated customers using commands from the terminal. All data is stored and persisted in CSV files.

---

## 📦 Project Overview

This project simulates a vegetable order system for the famous characters *Snow White and the Seven Dwarfs*. Orders and customers are stored in two separate CSV files:

- `pedidos.csv` – Contains individual order entries.
- `clientes.csv` – Contains customer names associated with each order.

Each order may include multiple vegetable types and is uniquely identified by an auto-incrementing ID.

---

## 🧰 Features

- Add new orders and customers.
- Modify existing orders (update or add vegetables).
- Delete orders from both files.
- List specific or all orders.
- Strict input validation.
- Modular codebase following clean design principles.

---

## 📁 File Structure

```plaintext
verduleria.py         # Main application script
pedidos.csv           # Orders file (created automatically if not present)
clientes.csv          # Customers file (created automatically if not present)
README.md             # Project documentation
📋 CSV File Formats
pedidos.csv
Each line represents a vegetable in an order:

Copiar
Editar
id_pedido;verdura;cantidad
Example:

r
Copiar
Editar
7;T;4
7;Z;5
Valid vegetables:

T = Tomato

B = Broccoli

Z = Carrot (Zanahoria)

L = Lettuce

clientes.csv
Each line represents a customer name tied to a specific order:

Copiar
Editar
id_pedido;nombre_cliente
Example:

Copiar
Editar
7;Tomi
🧑‍💻 Usage
Run the program using terminal commands:

bash
Copiar
Editar
python3 verduleria.py [command] [arguments...]
🔹 agregar <cantidad> <verdura> <cliente>
Adds a new order. If the input is invalid, the order is not created.

bash
Copiar
Editar
python3 verduleria.py agregar 3 B Agustina
🔹 modificar <id_pedido> <cantidad> <verdura>
Modifies an existing order. Updates quantity if the vegetable is already present or adds a new entry otherwise.

bash
Copiar
Editar
python3 verduleria.py modificar 1 5 T
🔹 eliminar <id_pedido>
Deletes all records of the specified order from both files.

bash
Copiar
Editar
python3 verduleria.py eliminar 1
🔹 listar [id_pedido]
Lists all orders if no ID is provided. If an ID is given, displays only that order.

bash
Copiar
Editar
python3 verduleria.py listar         # Lists all orders
python3 verduleria.py listar 3       # Lists order with ID 3
❗ Input Validation
Quantity must be a positive integer.

Vegetable types must be T, B, Z, or L.

Commands require all necessary arguments, otherwise an error is shown.

Order IDs must be valid and existing for modificar, eliminar, and listar.

✅ Good Practices Followed
Clear, modular design.

No use of input() – all arguments are from the command line.

Organized file handling with automatic creation if files are missing.

User-friendly feedback and error messages.

🧑‍🏫 Author & Project Info
This project was developed as part of the Trabajo Práctico Nº 3 for the subject:

75.40 Algoritmos y Programación I
Department of Computer Science – University of Buenos Aires
Professor: Camejo

Deadline: 28/11/2023

📜 License
This project is for educational purposes and does not use a formal license. You are free to explore, fork, and adapt it for learning.
