  file.write(str(r[0]) + " ")
    s = r[1]
    print(s)
    for i in range(len(r[1])):

            file.write(str(s[i]) + " ")
    file.write("\n")
file.close()