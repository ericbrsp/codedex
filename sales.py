import csv


with open('bestsellers.csv', 'r', encoding='utf8') as file:
    file.readline()
    csv_reader = csv.reader(file)
    
    max_sales = float('-inf')
    best_selling_book = None

    for row in csv_reader:
        current_sales = float(row[4])
        if current_sales > max_sales:
            max_sales = current_sales
            best_selling_book = row
            print(max_sales)


print("Maior número de vendas:", max_sales)
print("Livro mais vendido:", best_selling_book)
