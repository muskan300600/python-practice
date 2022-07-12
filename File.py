for i in range (2,21):
    with open(f"Multiplication_Table_Of_{i}.txt","w")as f:
        for j in range(10):
            print(f"{i}x{j}={i*j}\n")
    