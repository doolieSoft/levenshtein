import argparse
import re

import Levenshtein as lev
import unidecode

args = None


def getArguments():
    global args
    parser = argparse.ArgumentParser()

    parser.add_argument("--fullpath_denomination_labo",
                        help="chemin complet du fichier de dénomination des articles de labos", type=str)
    parser.add_argument("--fullpath_denomination_sap",
                        help="chemin complet du fichier de dénomination des articles dans sap", type=str)
    parser.add_argument("--fullpath_output",
                        help="chemin complet du fichier de sortie donnant la distance de levenshtein pour chaque ligne d'article de labo",
                        type=str)

    args = parser.parse_args()

    print("--fullpath_denomination_labo :" + args.fullpath_denomination_labo)
    print("--fullpath_denomination_sap :" + args.fullpath_denomination_sap)
    print("--fullpath_output :" + args.fullpath_output)


def main():
    f_denomination_labo = open(args.fullpath_denomination_labo, encoding="utf8")
    f_denomination_sap = open(args.fullpath_denomination_sap, encoding="utf8")
    f_result = open(args.fullpath_output, "w", encoding="utf8")

    lines_denomination_sap_zmmartstam = f_denomination_sap.readlines()
    f_denomination_sap.close()

    lines_zmmartstam_without_accents = []
    lines_zmmartstam_denom = []
    lines_zmmartstam_matnr = []

    for line_zmmartstam in lines_denomination_sap_zmmartstam:
        line_zmmartstam = line_zmmartstam.strip()
        line_zmmartstam = line_zmmartstam.split("\t")

        line_zmmartstam_tmp = line_zmmartstam[1].upper()
        line_zmmartstam_tmp = unidecode.unidecode(line_zmmartstam_tmp)
        line_zmmartstam_tmp = re.sub('[^0-9A-Z]*', '', line_zmmartstam_tmp)

        lines_zmmartstam_without_accents.append(line_zmmartstam_tmp)

        lines_zmmartstam_denom.append(line_zmmartstam[1])
        lines_zmmartstam_matnr.append(line_zmmartstam[0])

    i = 0
    lines_result = []
    for line_feuil1 in f_denomination_labo:
        if i % 100 == 0:
            print(i)
        i += 1

        line_feuil1 = line_feuil1.strip()
        line_feuil1 = line_feuil1.split("\t")

        dists = []

        if len(line_feuil1) < 3:
            id_prod = line_feuil1[0]
            labo = line_feuil1[1]
            lines_result.append("{0}\t{1}\t\t\t\t1,00\n".format(id_prod, labo))
            continue

        line_feuil1_tmp = line_feuil1[2].upper()
        line_feuil1_tmp = unidecode.unidecode(line_feuil1_tmp)
        line_feuil1_tmp = re.sub('[^0-9A-Z]*', '', line_feuil1_tmp)

        for line_zmmartstam_tmp in lines_zmmartstam_without_accents:
            dist = lev.distance(line_feuil1_tmp, line_zmmartstam_tmp)
            divide = len(line_feuil1_tmp)
            dist = dist / divide
            dists.append(dist)

        if len(dists) > 0:
            ind_min = dists.index(min(dists))
            levenshtein_val = "{0:0.2f}".format(dists[ind_min])
            levenshtein_val = levenshtein_val.replace(".", ",")
            lines_result.append("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(line_feuil1[0], line_feuil1[1], line_feuil1[2],
                                                                        lines_zmmartstam_matnr[ind_min],
                                                                        lines_zmmartstam_denom[ind_min],
                                                                        levenshtein_val))
    f_result.write(''.join(lines_result))
    f_result.close()


if __name__ == "__main__":
    getArguments()
    main()
