def celik_to_farik(celik):
    return (celik * 9/5) + 32

def farik_to_celik(farik):
    return (farik - 32) * 5/9

print(farik_to_celik(45))
print(celik_to_farik(100))

