def shop_from_grocery_list(budget, grocery_list, *products):
    purchased_products = []
    for current_product in products:
        product_name, product_price = current_product
        if product_name not in grocery_list:
            continue
        elif product_name in purchased_products:
            continue
        else:
            if budget < product_price:
                break
            purchased_products.append(product_name)
            budget -= product_price

    check = all(item in purchased_products for item in grocery_list)

    if check:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        result = set(grocery_list).difference(set(purchased_products))
        return f"You did not buy all the products. Missing products: {', '.join(str(x) for x in result)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))