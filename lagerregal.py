import argparse
import os

dim = 0.001




#Benennung des Files anhand hash, groesse und art Funktion noch schreiben
def filenamer():
    regalname = "tollesRegal"
    filenameObj = "lagerregal.obj"
    filenameMlt = "lagerregal.obj"
    
    return regalname,filenameObj,filenameMlt

def objHeader():
    header = "#Lorenz Suchy FAPS OBJ File:" + "\n" + "#" + filenamer()[0] + "\n" + "mtllib" + filenamer()[2]
    f.write(header)


def regalstreben(h,l,d,e,t):
    
    contents = "\no Regal"
    #Ursprungsstrebe
    #Strebennummerierung:
    #(0,0) --> x
    #  |   1    2
    #  v   3    4
    #  z    
    #[x,y,z]

    #Punkte erstellen
    points1 = [[0,0,0],[e,0,0],[e,0,t],[t,0,t],[t,0,e],[0,0,e]]
    points2 = [[l,0,0],[l,0,e],[l-t,0,e],[l-t,0,t],[l-e,0,t],[l-e,0,0]]
    points3 = [[0,0,d],[0,0,d-e],[t,0,d-e],[t,0,d-t],[e,0,d-t],[e,0,d]]
    points4 = [[l,0,d],[l-e,0,d],[l-e,0,d-t],[l-t,0,d-t],[l-t,0,d-e],[l,0,d-e]]

    
    allPoints = [points1,points2,points3,points4]

    print("lagerregal")

    for points in allPoints:
        print(points)
        pointNum = 1
        
        for point in points:
            contents += "\nv "
            
            if pointNum == 1:
                for coord in point:
                    contents += str(dim * coord) + " "                    
        
        for point in points:
            contents += "\nv "

            for i in range(3):
                if i != 1 :                
                    contents += str(dim * point[i])
                else:
                    contents += str(dim * (point[i] + h))
                contents += " "
        
        pointNum += 1
    contents += "\ng Streben"

    for j in range(4):
        add = 12 * j
        #Flächen erstellen
        facesBottom = [[1,2,4],[2,3,4],[4,5,6],[1,4,6]]
        facesSides = [[1,2,7],[2,7,8]]

        #Flächen unten und oben
        for face in facesBottom:
            contents += "\nf"
            for point in face:
                contents += " " + str(point + add)

            contents += "\nf"
            for point in face:
                contents += " " + str(point + 6 + add)

        #Flächen seitlich
        for face in facesSides:
            for i in range(6):
                contents += "\nf "
                if i < 5:
                    for point in face:
                        contents += str(point + i + add) + " "
                else:
                    for point in face:
                        if ((point + i)% 6) == 1:
                            contents += str(point + i - 6 + add) + " "
                        else:
                            contents += str(point + i + add) + " "



    print(contents)
    f.write(contents)







if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    #parser.add_argument("-h",required=True ,help="height")
    #parser.add_argument("-l",required=True ,help="length")
    #parser.add_argument('-d',required=True ,help="depth")
    #parser.add_argument('-e',required=True ,help="edge")
    #parser.add_argument('-t',required=True ,help="thickness")

    args = parser.parse_args()

   
    #wbPool = load_workbook(filename = args.pool)
    #wbProj = load_workbook(filename = args.proj)

 

    try:
        f = open(filenamer()[1], "a")
        objHeader()
        regalstreben(2000,1200,600,50,5)

    except:

        print("Exec Failed")

 

 
