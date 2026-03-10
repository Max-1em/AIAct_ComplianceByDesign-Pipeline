with open("docs/model_card.txt", "w") as f:
    f.write("Model Card\n")
    f.write("Model: RandomForest\n")
    f.write("Dataset: Iris\n")

with open("docs/risk_log.txt", "w") as f:
    f.write("Risk Log\n")
    f.write("Potential bias risk\n")

print("Compliance docs generated")
