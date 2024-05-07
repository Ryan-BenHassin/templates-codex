import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class BillingAndInvoicing:
 def __init__(self, root):
 self.root = root
 self.root.title("Billing and Invoicing System")

 # create tabs
 self.tabs = ttk.Notebook(self.root)
 self.billing_tab = ttk.Frame(self.tabs)
 self.invoicing_tab = ttk.Frame(self.tabs)
 self.tabs.add(self.billing_tab, text="Billing")
 self.tabs.add(self.invoicing_tab, text="Invoicing")
 self.tabs.pack(fill="both", expand=True)

 # billing tab
 self.customer_label = ttk.Label(self.billing_tab, text="Customer Name:")
 self.customer_label.pack()
 self.customer_entry = ttk.Entry(self.billing_tab, width=30)
 self.customer_entry.pack()

 self.date_label = ttk.Label(self.billing_tab, text="Date:")
 self.date_label.pack()
 self.date_entry = ttk.Entry(self.billing_tab, width=30)
 self.date_entry.pack()

 self.item_label = ttk.Label(self.billing_tab, text="Item:")
 self.item_label.pack()
 self.item_entry = ttk.Entry(self.billing_tab, width=30)
 self.item_entry.pack()

 self.quantity_label = ttk.Label(self.billing_tab, text="Quantity:")
 self.quantity_label.pack()
 self.quantity_entry = ttk.Entry(self.billing_tab, width=30)
 self.quantity_entry.pack()

 self.price_label = ttk.Label(self.billing_tab, text="Price:")
 self.price_label.pack()
 self.price_entry = ttk.Entry(self.billing_tab, width=30)
 self.price_entry.pack()

 self.billing_button = ttk.Button(self.billing_tab, text="Generate Bill", command=self.generate_bill)
 self.billing_button.pack()

 # invoicing tab
 self.invoice_customer_label = ttk.Label(self.invoicing_tab, text="Customer Name:")
 self.invoice_customer_label.pack()
 self.invoice_customer_entry = ttk.Entry(self.invoicing_tab, width=30)
 self.invoice_customer_entry.pack()

 self.invoice_date_label = ttk.Label(self.invoicing_tab, text="Date:")
 self.invoice_date_label.pack()
 self.invoice_date_entry = ttk.Entry(self.invoicing_tab, width=30)
 self.invoice_date_entry.pack()

 self.invoice_item_label = ttk.Label(self.invoicing_tab, text="Item:")
 self.invoice_item_label.pack()
 self.invoice_item_entry = ttk.Entry(self.invoicing_tab, width=30)
 self.invoice_item_entry.pack()

 self.invoice_quantity_label = ttk.Label(self.invoicing_tab, text="Quantity:")
 self.invoice_quantity_label.pack()
 self.invoice_quantity_entry = ttk.Entry(self.invoicing_tab, width=30)
 self.invoice_quantity_entry.pack()

 self.invoice_price_label = ttk.Label(self.invoicing_tab, text="Price:")
 self.invoice_price_label.pack()
 self.invoice_price_entry = ttk.Entry(self.invoicing_tab, width=30)
 self.invoice_price_entry.pack()

 self.invoicing_button = ttk.Button(self.invoicing_tab, text="Generate Invoice", command=self.generate_invoice)
 self.invoicing_button.pack()

 def generate_bill(self):
 customer_name = self.customer_entry.get()
 date = self.date_entry.get()
 item = self.item_entry.get()
 quantity = self.quantity_entry.get()
 price = self.price_entry.get()

 if not customer_name or not date or not item or not quantity or not price:
 messagebox.showerror("Error", "Please fill in all fields")
 return

 bill_text = f"Bill for {customer_name}\nDate: {date}\nItem: {item}\nQuantity: {quantity}\nPrice: {price}"
 messagebox.showinfo("Bill", bill_text)

 def generate_invoice(self):
 customer_name = self.invoice_customer_entry.get()
 date = self.invoice_date_entry.get()
 item = self.invoice_item_entry.get()
 quantity = self.invoice_quantity_entry.get()
 price = self.invoice_price_entry.get()

 if not customer_name or not date or not item or not quantity or not price:
 messagebox.showerror("Error", "Please fill in all fields")
 return

 invoice_text = f"Invoice for {customer_name}\nDate: {date}\nItem: {item}\nQuantity: {quantity}\nPrice: {price}"
 messagebox.showinfo("Invoice", invoice_text)

root = tk.Tk()
app = BillingAndInvoicing(root)
root.mainloop()
