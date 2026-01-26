def chai_counter():
    chai_order = "Masala Chai"
    def print_order():
        chai_order = "Lemon Tea"
        print(chai_order)
    print_order()
    print(chai_order)


chai_order = "Green Tea"
chai_counter()
print(chai_order)