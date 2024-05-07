#TODO
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Invoice:
 def __init__(self, id, client, date, total):
 self.id = id
 self.client = client
 self.date = date
 self.total = total

class Client:
 def __init__(self, id, name, address):
 self.id = id
 self.name = name
 self.address = address

clients = [
 Client(1, "John Doe", "123 Main St"),
 Client(2, "Jane Doe", "456 Elm St")
]

invoices = [
 Invoice(1, clients[0], datetime.now(), 100.0),
 Invoice(2, clients[1], datetime.now(), 200.0)
]

@app.route('/')
def index():
 return render_template('index.html', clients=clients)

@app.route('/create/invoice', methods=['POST'])
def create_invoice():
 client_id = int(request.form['client_id'])
 client = next(c for c in clients if c.id == client_id)
 invoice = Invoice(len(invoices) + 1, client, datetime.now(), 0.0)
 invoices.append(invoice)
 return redirect(url_for('index'))

@app.route('/invoices')
def get_invoices():
 return render_template('invoices.html', invoices=invoices)

@app.route('/invoice/<int:invoice_id>')
def get_invoice(invoice_id):
 invoice = next(i for i in invoices if i.id == invoice_id)
 return render_template('invoice.html', invoice=invoice)

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)
