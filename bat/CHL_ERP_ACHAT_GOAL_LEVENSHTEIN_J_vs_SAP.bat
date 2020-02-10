@echo off
call venv\Scripts\activate

set p1=--fullpath_denomination_labo="C:\\Users\\c158492\\ProjetBoulot\\PYTHON\\levenshtein\\input\\DENOMINATION_J_FEUIL1_LABO.txt"
set p2=--fullpath_denomination_sap="C:\\Users\\c158492\\ProjetBoulot\\PYTHON\\levenshtein\\input\\DENOMINATION_SAP.txt"
set p3=--fullpath_output="C:\\Users\\c158492\\ProjetBoulot\\PYTHON\\levenshtein\\output\\RESULT_COMPARAISON_DENOMINATION_J_FEUIL1_LABO_vs_SAP.csv"
python CHL_ERP_ACHAT_GOAL_COMPARAISON_ARTICLE_LEVENSHTEIN.py %p1% %p2% %p3%

call venv\Scripts\deactivate
