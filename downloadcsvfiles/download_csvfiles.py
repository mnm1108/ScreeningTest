#Python program to download csv files from remote server to local database using SFTP

import pysftp
import re
import pandas as pd
from sqlalchemy import create_engine
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

#remote server credentials
myHostname = "localhost"
myUsername = "megha"
myPassword = "annagund123."

#create connection with MySQL database
engine = create_engine('mysql://root:root@localhost:3306/csvdata')

#connect to remote server using pysftp
with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, cnopts=cnopts) as sftp:
    print("Connection succesfully established ... ")
    remote_path = 'dumps/files'
    filepattern = re.compile('^Perf-\d+-([0-9]{4})-([0-9]{2})-([0-9]{2}) +([0-9]{4}).csv$')

    filelist = sftp.listdir('dumps/files')

    #change to appropriate remote directory
    sftp.chdir('dumps/files/')

    #check for relevant csv files
    for filename in filelist:
        if(filename.endswith('.csv') and re.search(filepattern,filename)):
            with sftp.open(filename) as f:
                #read csv into a dataframe
                df = pd.read_csv(f)

                #write records stored in dataframe to MySQL database
                df.to_sql(filename, con=engine)
