
# 1. ცვლადები

try:
    cart_total = int(input("enter price in lari?"))
except:
  print("nu maimunob")

#   ეს დღევანდელ ლექციაზე დავამატე
user_status = "vip"
has_promo_code = True
loyalty_points = 600
delivery_city = "თბილისი"
is_account_active = True

# 2. ანგარიშის ვალიდაცია
if not is_account_active:
    print("your account is blocked, we cant process")

elif cart_total <= 0:
    print("error.")

else:
    # 3. ფასდაკლების გამოთვლა
    if user_status == "vip":
        if loyalty_points >= 500:
            discount = 25
        else:
            discount = 20

    elif user_status == "regular":
        if has_promo_code or cart_total >= 150:
            discount = 10
        else:
            discount = 0

    elif user_status == "admin":
        discount = 50

    else:
        discount = 0
        print("Warning: Unknown user status.")

    # 4. ფასდაკლებული თანხის გამოთვლა
    discount_amount = cart_total * discount / 100
    discounted_total = cart_total - discount_amount

    # 5. მიტანის საფასურის გამოთვლა
    if delivery_city in ["თბილისი", "ქუთაისი", "ბათუმი"]:
        if discounted_total >= 100:
            delivery_fee = 0
        else:
            delivery_fee = 5
    else:
        delivery_fee = 15

    # 6. საბოლოო თანხა
    final_total = discounted_total + delivery_fee

    # 7. ინვოისი

    print(f"price {cart_total:.2f} lari")
    print(f"discount: {discount}%")
    print(f"discunt price: {discount_amount:.2f} lari")
    print(f"discount total {discounted_total:.2f} lari")
    print(f"delivery: {delivery_fee:.2f} lari")
    print(f"final price: {final_total:.2f} lari")
    
