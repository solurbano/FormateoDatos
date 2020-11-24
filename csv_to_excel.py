import pandas as pd
import glob

colums = ["VarName","TimeString","VarValue","Validity","Time_ms"]
termometros = ['TI1010', 'TIC1020', 'TIC1030', 'TIC1040', 'TIC1050', 'TIC1060', \
    'TIC1070', 'TIC1080', 'TIC1090', 'TIC1100', 'TIC1110', 'TIC1120', 'TIC1130', \
    'TIC1140', 'TIC1150', 'TIC1160', 'TIC1170', 'TIC1180', 'TIC1190', 'TI1200', \
    'TI1210', 'TI1220', 'TI1230', 'TIC1240', 'TIC1250', 'TIC1260', 'TIC1270', \
    'TIC1280', 'TIC1290', 'TIC1300', 'TIC1310', 'TIC1320', 'TIC1330', 'TIC1340', \
    'TIC1350', 'TIC1360', 'TIC1370', 'TIC1380', 'TIC1390', 'TIC1400']

def getTermometros(folder="Data"):
    termos = set()
    for file in glob.glob(folder+"/*"):
        ter = file[file.find('/')+1: file.find('_')]
        termos.add(ter)

    return  list(termos)

def getFilePath(termometro,folder="Data"):
    for file in glob.glob(folder+"/"+termometro+"*"):
        return file
    return ""

df = pd.DataFrame()

print(getTermometros())

first = True

with pd.ExcelWriter('output.xlsx') as writer:

    for termometro in termometros:
        print(termometro)

        file_name = getFilePath(termometro)
        temp_df = pd.read_csv(file_name, error_bad_lines=False)

        if (first):
            first=False
            df["TimeString"] = temp_df["TimeString"]
            df["Time_ms"]=temp_df["Time_ms"]
        df[termometro]=temp_df['VarValue']

    df.to_excel(writer, index = False, sheet_name="Data", )


writer.save()
