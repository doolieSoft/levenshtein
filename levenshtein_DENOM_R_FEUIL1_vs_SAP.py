import Levenshtein as lev
import re
import unidecode


def main():
    pattern = re.compile('[[:alnum]]*')

    feuil1 = open("C:\\Users\\c158492\\ProjetBoulot\\PYTHON\\levenshtein\\input\\Lev_DENOM_D_FEUIL1_vs_SAP.txt",
                  encoding="utf8")
    zmmartstam = open("C:\\Users\\c158492\\ProjetBoulot\\PYTHON\\levenshtein\\input\\zmmartstam.txt", encoding="utf8")

    #feuil1 = open("C:\\Users\\c158492\\ProjetBoulot\\PYTHON\\levenshtein\\input\\eosin.txt",
    #              encoding="utf8")
    #zmmartstam = open("C:\\Users\\c158492\\ProjetBoulot\\PYTHON\\levenshtein\\input\\zmmartstam_eosine.txt",
    #                  encoding="utf8")

    lines_zmmartstam = zmmartstam.readlines()
    zmmartstam.close()

    result = open(
        "C:\\Users\\c158492\\ProjetBoulot\\PYTHON\\levenshtein\\output\\result_feuil1_R_vs_zmmartstam_sap.csv",
        "w",
        encoding="utf8")

    #result = open(
    #    "C:\\Users\\c158492\\ProjetBoulot\\PYTHON\\levenshtein\\output\\result_test.csv",
    #    "w",
    #    encoding="utf8")

    for line_feuil1 in feuil1:

        line_feuil1 = line_feuil1.strip()
        line_feuil1 = line_feuil1.split("\t")

        dists = []

        lines_zmmartstam_denom = []
        lines_zmmartstam_matnr = []

        if len(line_feuil1) < 3:
            id_prod = line_feuil1[0]
            labo = line_feuil1[1]
            result.write("{0}\t{1}\t\t\t\t1,00\n".format(id_prod, labo))
            continue

        line_feuil1_tmp = line_feuil1[2].upper()
        line_feuil1_tmp = unidecode.unidecode(line_feuil1_tmp)
        line_feuil1_tmp = re.sub('[^0-9A-Z]+', '', line_feuil1_tmp)

        for line_zmmartstam in lines_zmmartstam:
            line_zmmartstam = line_zmmartstam.strip()
            line_zmmartstam = line_zmmartstam.split("\t")

            line_zmmartstam_tmp = re.sub('[^0-9A-Z]+', '', line_zmmartstam[1].upper())
            line_zmmartstam_tmp = unidecode.unidecode(line_zmmartstam_tmp)
            # print(line_zmmartstam_tmp)
            # print(line_feuil1_tmp)
            dist = lev.distance(line_feuil1_tmp, line_zmmartstam_tmp)
            divide = len(line_feuil1_tmp)
            dist = dist / divide
            dists.append(dist)

            lines_zmmartstam_denom.append(line_zmmartstam[1])
            lines_zmmartstam_matnr.append(line_zmmartstam[0])

        if len(dists) > 0:
            ind_min = dists.index(min(dists))
            levenshtein_val = "{0:0.2f}".format(dists[ind_min])
            levenshtein_val = levenshtein_val.replace(".", ",")
            result.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(line_feuil1[0], line_feuil1[1], line_feuil1[2],
                                                                 lines_zmmartstam_matnr[ind_min],
                                                                 lines_zmmartstam_denom[ind_min], levenshtein_val))
    result.close()


if __name__ == "__main__":
    main()
