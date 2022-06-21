
import camelot as cp

tables = cp.read_pdf("table_extraction/food.pdf", pages= '1')
print(tables)

tables.export('foo.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')
