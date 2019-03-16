import base64
import os
from MongoDbConnection import MongoConnection
class UploadImage():
    def upload(self,email):
        j=0
        Images_Path="/home/pi/Desktop/Minor/Images/"
        collect=MongoConnection.getConnection()
        listImages=os.listdir(Images_Path)
        
        for i in listImages:
            with open(Images_Path+i, "rb") as imageFile:
                string = base64.b64encode(imageFile.read())
                dataDict={"Image":string,
                          "Email_ID":email
                          }
                collect.insert_one(dataDict)
                j=j+1
                os.remove(Images_Path+i)
        print(str(j)+" Images inserted in db")
    