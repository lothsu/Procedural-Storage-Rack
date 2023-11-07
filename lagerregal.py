import argparse
import os


#Benennung des Files anhand hash groesse und art Funktion noch schreiben


def filenamer():
    filenameObj = "lagerregal.obj"
    filenameMlt = "lagerregal.obj"
    return filenameObj,filenameMlt
 

f = open(filenamer()[0], "a")


def objHeader():
    f.write("# lagerregal.py ")
    f.write("Lorenz Suchy FAPS OBJ File:")
    f.write("# lagerregal.py ")



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-h",required=True ,help="height")
    parser.add_argument("-l",required=True ,help="length")
    parser.add_argument('-d',required=True ,help="depth")

    args = parser.parse_args()

   
    wbPool = load_workbook(filename = args.pool)
    wbProj = load_workbook(filename = args.proj)

 

    try:

        compareDirs(poolSheet, projSheet)

        if args.licence:

            printGuide()

    except:

        print("Exec Failed")

 

 
