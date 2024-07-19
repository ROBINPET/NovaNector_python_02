
# Invoice Generator

# Define a dictionary to store the invoice data
invoice = {
    'date': '',
    'number': '',
    'customer': '',
    'items': []
}

# Function to add items to the invoice
def add_item():
    item = {}
    item['name'] = input('Enter item name: ')
    item['quantity'] = int(input('Enter quantity: '))
    item['price'] = float(input('Enter price: '))
    invoice['items'].append(item)

# Function to generate the invoice
def generate_invoice():
    print('Invoice Date:', invoice['date'])
    print('Invoice Number:', invoice['number'])
    print('Customer:', invoice['customer'])
    print('Items:')
    for item in invoice['items']:
        print(f"  {item['name']} x {item['quantity']} @ ${item['price']:.2f} = ${item['quantity'] * item['price']:.2f}")
    print(f'Total: ${sum(item["quantity"] * item["price"] for item in invoice["items"]):.2f}')

# Main program
invoice['date'] = input('Enter invoice date (YYYY-MM-DD): ')
invoice['number'] = input('Enter invoice number: ')
invoice['customer'] = input('Enter customer name: ')

while True:
    add_item()
    response = input('Add another item? (y/n): ')
    if response.lower() != 'y':
        break

generate_invoice()