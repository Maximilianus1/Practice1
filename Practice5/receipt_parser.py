import re
def find_spec(smth):
    c = re.findall(f"{smth}\\n.*",b)
    cc = list(map(lambda x : x.split("\n")[1], c))
    return cc
file = open("raw.txt", "r", encoding="utf-8")
a = file.readlines()
b=""
b= b.join(a)
prices = find_spec("Стоимость")
product_names = find_spec("\d\\.")
time = re.findall(r"\d+\.\d+\.\d+\s\d+\:\d+\:\d+",b)
payment_method = re.findall(r"(Банковская карта|Наличные|Мобильный платеж|Платежная карта)(?=:)", b)
print("="*50)
print(f"TIME: {''.join(time):^50}")
print(f"LIST OF PRODUCTS:")
for i in range(len(product_names)):
    print(i)
    print(f"Name: {product_names[i] :^50}")
    print(f"Cost: {prices[i] :^50}")
    print()
    
print(f"TOTAL AMOUNT: {len(product_names) :^50}")
print(f"PAYMENT METHOD: {''.join(payment_method) :^50}")