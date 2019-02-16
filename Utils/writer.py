
def save_mats(path, mats, order = 4):
    with open(path, 'w') as file:
        file.write(str(len(mats) ) +'\n')
        for i in mats.keys():
            for j in range(len(mats[i])):
                file.write(str(i[0]) + " " + str(i[1]) + "\n")
                mat = mats[i][j][0]
                for k in range(len(mat)):
                    for l in range(len(mat[k])):
                        for m in range(len(mat[k][l])):
                            file.write(str(mat[k][l][m]) + " ")
                    file.write("\n")
