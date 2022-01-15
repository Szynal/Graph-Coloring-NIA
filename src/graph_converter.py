filename = "games120"
with open(f"../graphs/{filename}.col", "r") as file:
    lines = file.readlines()
print(lines)
new_lines = []
new_lines.append(lines[0].split(" ")[2]+"\n")
current_node = 1
new_line = f""
for text in lines:
    line = text.split(" ")
    if line[2][-1] != "\n":
        line[2] +="\n"
    print(line)
    if line[0] == "e":
        if line[1] == current_node.__str__():
            if len(new_line) > 0:
                new_line += f" {line[2][:-1]}"
            else:
                new_line += f"{line[2][:-1]}"
        else:
            current_node = int(line[1])
            new_line += " 0\n"
            new_lines.append(new_line)
            new_line = f""
            new_line += f"{line[2][:-1]}"
            if text == lines[-1]:
                new_line += " 0\n"
                new_lines.append(new_line)
with open(f"../graphs/{filename}.graph", 'w') as file:
    for line in new_lines:
        file.write(line)

