import tkinter as tk
from tkinter import ttk
import sqlite3

class BillingSystem:
 def __init__(self, root):
 self.root = root
 self.root.title("Billing and Invoicing System")
 self.root.geometry("800x600")

 # Create a database connection
 self.conn = sqlite3.connect("billing_system.db")
 self.cursor = self.conn.cursor()

 # Create tables if they don't exist
 self.cursor.execute("CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT, address TEXT, phone TEXT, email TEXT)")
 self.cursor.execute("CREATE TABLE IF NOT EXISTS invoices (id INTEGER PRIMARY KEY, customer_id INTEGER, date TEXT, total REAL)")
 self.cursor.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, invoice_id INTEGER, description TEXT, quantity INTEGER, price REAL, total REAL)")

 # Create frames
 self.customer_frame = tk.Frame(self.root)
 self.customer_frame.pack(fill="x")

 self.invoice_frame = tk.Frame(self.root)
 self.invoice_frame.pack(fill="x")

 self.item_frame = tk.Frame(self.root)
 self.item_frame.pack(fill="x")

 # Customer information
 tk.Label(self.customer_frame, text="Customer Name:").pack(side="left")
 self.customer_name = tk.Entry(self.customer_frame, width=20)
 self.customer_name.pack(side="left")
 tk.Label(self.customer_frame, text="Address:").pack(side="left")
 self.customer_address = tk.Entry(self.customer_frame, width=20)
 self.customer_address.pack(side="left")
 tk.Label(self.customer_frame, text="Phone:").pack(side="left")
 self.customer_phone = tk.Entry(self.customer_frame, width=20)
 self.customer_phone.pack(side="left")
 tk.Label(self.customer_frame, text="Email:").pack(side="left")
 self.customer_email = tk.Entry(self.customer_frame, width=20)
 self.customer_email.pack(side="left")
 tk.Button(self.customer_frame, text="Add Customer", command=self.add_customer).pack(side="left")

 # Invoice information
 tk.Label(self.invoice_frame, text="Date:").pack(side="left")
 self.invoice_date = tk.Entry(self.invoice_frame, width=20)
 self.invoice_date.pack(side="left")
 tk.Label(self.invoice_frame, text="Customer:").pack(side="left")
 self.invoice_customer = ttk.Combobox(self.invoice_frame, values=[])
 self.invoice_customer.pack(side="left")
 self.update_customer_list()
 tk.Button(self.invoice_frame, text="Create Invoice", command=self.create_invoice).pack(side="left")

 # Item information
 tk.Label(self.item_frame, text="Description:").pack(side="left")
 self.item_description = tk.Entry(self.item_frame, width=20)
 self.item_description.pack(side="left")
 tk.Label(self.item_frame, text="Quantity:").pack(side="left")
 self.item_quantity = tk.Entry(self.item_frame, width=20)
 self.item_quantity.pack(side="left")
 tk.Label(self.item_frame, text="Price:").pack(side="left")
 self.item_price = tk.Entry(self.item_frame, width=20)
 self.item_price.pack(side="left")
 tk.Button(self.item_frame, text="Add Item", command=self.add_item).pack(side="left")

 def add_customer(self):
 name = self.customer_name.get()
 address = self.customer_address.get()
 phone = self.customer_phone.get()
 email = self.customer_email.get()
 self.cursor.execute("INSERT INTO customers (name, address, phone, email) VALUES (?, ?, ?, ?)", (name, address, phone, email))
 self.conn.commit()
 self.update_customer_list()

 def update_customer_list(self):
 self.cursor.execute("SELECT name FROM customers")
 customers = [row[0] for row in self.cursor.fetchall()]
 self.invoice_customer['values'] = customers

 def create_invoice(self):
 date = self.invoice_date.get()
 customer = self.invoice_customer.get()
 self.cursor.execute("INSERT INTO invoices (customer_id, date) VALUES ((SELECT id FROM customers WHERE name = ?), ?)", (customer, date))
 self.conn.commit()
 self.invoice_date.delete(0, "end")
 self.invoice_customer.set("")

 def add_item(self):
 description = self.item_description.get()
 quantity = self.item_quantity.get()
 price = self.item_price.get()
 total = float(quantity) README.md categories.txt generate.sh start.sh systemPrompt.txt templates float(price)
 self.cursor.execute("INSERT INTO items (invoice_id, description, quantity, price, total) VALUES ((SELECT id FROM invoices ORDER BY id DESC LIMIT 1), ?, ?, ?, ?)", (description, quantity, price, total))
 self.conn.commit()
 self.item_description.delete(0, "end")
 self.item_quantity.delete(0, "end")
 self.item_price.delete(0, "end")

root = tk.Tk()
app = BillingSystem(root)
root.mainloop()
