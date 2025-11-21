# If name is less than 3 characters long:
# - Print an error message saying "Name must be at least 3 characters long.""
# If name is more than 50 characters long:
# - Print an error message saying "Name can be a maximum of 50 Characters."
# Otherwise
# - Print "Name looks good!"

name = "Joesfssdfffdkfmkmfsdmfs;fmdmfsdffsdflfsllnlsnflnflnldnlsdnlkgns"
print(len(name))
if len(name) < 3:
    print("Name must be atleast 3 characters long.")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters.")
else:
    print("Name looks good")