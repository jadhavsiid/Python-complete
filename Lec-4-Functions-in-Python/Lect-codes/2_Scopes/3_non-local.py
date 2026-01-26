def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type
        chai_type = "kesar"
    
    kitchen()
    print(f"After update chai type is: {chai_type}")

update_order()