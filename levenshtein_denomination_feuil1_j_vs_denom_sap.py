import Levenshtein as lev


def main():
    feuil1 = open("C:\\Users\\c158492\\ProjetBoulot\\PYTHON\\levenshtein\\feuil1v2.txt", encoding="utf8")

    for line_feuil1 in feuil1:

        line_feuil1 = line_feuil1.strip()
        line_feuil1 = line_feuil1.split("\t")

        dists = []

        lines_zmmartstam_denom = []
        lines_zmmartstam_matnr = []

        zmmartstam = open("C:\\Users\\c158492\\ProjetBoulot\\PYTHON\\levenshtein\\zmmartstamv2.txt", encoding="utf8")
        for line_zmmartstam in zmmartstam:
            line_zmmartstam = line_zmmartstam.strip()
            line_zmmartstam = line_zmmartstam.split("\t")

            dist = lev.distance(line_feuil1[2], line_zmmartstam[1])
            dist = dist / len(line_feuil1[2])
            dists.append(dist)
            lines_zmmartstam_denom.append(line_zmmartstam[1])
            lines_zmmartstam_matnr.append(line_zmmartstam[0])

        zmmartstam.close()

        ind_min = dists.index(min(dists))
        print("{0}\t{1}\t{2}\t{3}\t{4}\t{5:0.2f}".format(line_feuil1[0], line_feuil1[1], line_feuil1[2],
                                                         lines_zmmartstam_matnr[ind_min],
                                                         lines_zmmartstam_denom[ind_min], dists[ind_min]))


if __name__ == "__main__":
    main()
