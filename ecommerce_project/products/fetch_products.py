import json
import re

def clean_price(price):
    # توحيد تنسيق الأسعار
    price = price.replace(',', '.')  # استبدال الفاصلة بالنقطة إن وجدت
    price = re.sub(r'[^0-9\.€$]', '', price)  # إزالة أي رموز غير الأرقام والعملات
    return price.strip()

def filter_products(products, existing_products):
    cleaned_products = {p['title']: p for p in existing_products}  # استخدام قاموس لتجنب التكرار
    
    for product in products:
        if product['title'].lower() == 'shop on ebay':
            continue  # تجاهل المنتجات غير المفيدة
        
        product['price'] = clean_price(product['price'])
        cleaned_products[product['title']] = product  # تحديث البيانات أو إضافتها
    
    return list(cleaned_products.values())

def load_products(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # إرجاع قائمة فارغة إذا لم يكن الملف موجودًا أو كان فارغًا

def save_products(filename, products):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(products, file, indent=4, ensure_ascii=False)

# تحميل البيانات القديمة والجديدة
existing_products = load_products('cleaned_ebay_products.json')
new_products = load_products('ebay_products.json')

# تصفية البيانات وتحديثها
filtered_products = filter_products(new_products, existing_products)
save_products('cleaned_ebay_products.json', filtered_products)

print(f'✅ تم تنظيف البيانات وتحديثها وحفظها في cleaned_ebay_products.json')







