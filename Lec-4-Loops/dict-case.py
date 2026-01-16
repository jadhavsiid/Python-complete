users = [
    {
        'id': 1,
        'total': 100,
        'coupon-code': 'p20'
    },
    {
        'id': 2,
        'total': 150,
        'coupon-code': 's10'
    },
    {
        'id': 3,
        'total': 250,
        'coupon-code': 'g50'
    }
]

discounts = {
    "p20": (0.2,0),
    "s10": (0.5,0),
    "g50": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupon-code"],(0,0))
    discount = user["total"] * percent + fixed
    print(f"{user ["id"]} paid {user["total"]} and got discount for next visit of rupees {discount}")
