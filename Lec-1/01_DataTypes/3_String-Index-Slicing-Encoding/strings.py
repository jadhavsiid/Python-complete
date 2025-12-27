chai_type = "Ginger Chai"
custName = "John"
print(f"One {chai_type} please, for our customer {custName}")

# ! String Slicing
chai_desc = "Aromatic and Bold"
print(f"first word: {chai_desc[0:8]}")
print(f"Last Word: {chai_desc[12:]}")

# ! Special symbols
label_text = "Chai speciàl"
print(f"Special Characters: {label_text}")
encoded_label = label_text.encode("utf-8")
print(f"Encoded Label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded Label: {decoded_label}")