from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import datetime
gauth = GoogleAuth()           
drive = GoogleDrive(gauth) 
Database = "TestesBackup"
NomeArquivo = Database +"-"+datetime.datetime.now().strftime("%d-%m-%Y") +".gz"
LocalArquivo  = '"'+os.getcwd() + "/" + NomeArquivo+'"'
LocalConfig = '"'+os.getcwd() + "/config.cnf" +'"'
os.system('mysqldump --defaults-extra-file='+ LocalConfig +' --databases '+Database+' -f | gzip > '+LocalArquivo+'')
gfile = drive.CreateFile({'parents': [{'id': 'COLOQUE_AQUI_SEU_FOLDERID'}]})
gfile.SetContentFile(NomeArquivo)
gfile.Upload()
os.system('rm '+LocalArquivo)
