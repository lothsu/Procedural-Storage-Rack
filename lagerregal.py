import argparse
import os


#Benennung des Files anhand hash groesse und art Funktion noch schreiben


def filenamer():
    regalname = "tollesRegal"
    filenameObj = "lagerregal.obj"
    filenameMlt = "lagerregal.obj"
    
    return regalname,filenameObj,filenameMlt

def objHeader():
    header = "#Lorenz Suchy FAPS OBJ File:" + "\n" + "#" + filenamer()[0] + "\n" + "mtllib" + filenamer()[2]
    f.write(header)


def regalstreben(h,l,d):
    
    contents = "o Regal\n"
    contents += "g Streben\n"
    #Ursprungsstrebe
    #Strebennummerierung:
    #(0,0) -->
    #  |   1    2
    #  v   3    4    
    
    points1 = [[0,0,0],[50,0,0],[50,5,0],[5,5,0],[5,50,0],[0,50,0]]

    
    








if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    #parser.add_argument("-h",required=True ,help="height")
    #parser.add_argument("-l",required=True ,help="length")
    #parser.add_argument('-d',required=True ,help="depth")

    args = parser.parse_args()

   
    #wbPool = load_workbook(filename = args.pool)
    #wbProj = load_workbook(filename = args.proj)

 

    try:
        f = open(filenamer()[1], "a")
        objHeader()

    except:

        print("Exec Failed")

 

 
