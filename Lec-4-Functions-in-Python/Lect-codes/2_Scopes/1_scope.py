def serve_chai():
    chai_type = "Masala chai" # local scope => Scope is within the function
    print(f'Chai type inside function: {chai_type}')


chai_type = "Lemon tea" # global scope
print(f'Chai type outside function: {chai_type}')

serve_chai()