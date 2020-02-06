import Levenshtein as lev


def main():
    feuil1 = open("C:\\Users\\c158492\\ProjetBoulot\\PYTHON\\levenshtein\\feuil1.txt")
    zmmartstam = open("C:\\Users\\c158492\\ProjetBoulot\\PYTHON\\levenshtein\\zmmartstam.txt")

    feuil1_lines_dict_to_distance = {}

    for line_feuil1 in feuil1:
        print(line_feuil1)

        feuil1_lines_dict_to_distance[line_feuil1] = {}

        line_feuil1 = line_feuil1.strip()

        dists = []

        lines_zmmartstam = []

        for line_zmmartstam in zmmartstam.readlines():
            print(line_zmmartstam)
            line_zmmartstam = line_zmmartstam.strip()

            dist = lev.distance(line_feuil1, line_zmmartstam)

            dists.append(dist)
            lines_zmmartstam.append(line_zmmartstam)

        # if len(dists) > 0:
        ind_min = dists.index(min(dists))
        print(line_feuil1 + " " + lines_zmmartstam[ind_min] + " dist =" + dists[ind_min])

    if __name__ == "__main__":
        main()
