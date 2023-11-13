scores = {"network":60, "database":80, "security":50}
del scores["security"]
print(scores)

# score = scores.pop("network")
# print(scores)
# print(score)

print(scores.items())
print(scores.values())
print(list(scores.keys()))