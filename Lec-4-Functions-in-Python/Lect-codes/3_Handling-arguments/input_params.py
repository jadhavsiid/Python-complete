chai = "Ginger chai"

def prepare_chai(order):
    print(f"Preparing : {chai}")

prepare_chai(chai)
print(chai)

# ------------------------------------------------------------------------------------------
chai = [1, 2, 3]
print(f'Og chai: {chai}')
def edit_chai(cup):
    cup[2] = 55

edit_chai(chai)
print(f'Edited chai: {chai}')

# ------------------------------------------------------------------------------------------

# Positional parameters
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Masala","Yes","1 tablespoon")

# Swapping positional parameters
make_chai(milk="No", tea="Ginger",sugar="Little")

# ------------------------------------------------------------------------------------------

# Arguments and key-value arguments

def special_chai(*ingrediants, **extras):
    print(f'Ingrediants: {ingrediants}')
    print(f'Extras: {extras}')


special_chai("Cinnamon","Cardamom", sweetner = "honey", foam = "yes")

# ------------------------------------------------------------------------------------------
# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

# chai_order()
# chai_order()


def chai_order(order=None):
    if order is None:
        order = []
        print(order)

chai_order()
chai_order()