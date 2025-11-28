#index =    0       1       2        3
colors = ["red", "green", "blue", "yellow"]

# print(colors[1])

# for color in colors:
#     print(color)
# colors.pop(1)

colors.insert(2, "orange")

for i in range(len(colors)):
    color = colors[i]
    human_count = i + 1
    print(f"{human_count} - {color}")