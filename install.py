#!/usr/bin/python
import platform
import os
import time
def OperationSystem():
  uname = platform.uname()
  if uname[0] == 'Linux' :
    return "Linux"
  elif uname[0] == "Darwin" :
    return "Mac"
def getBashProfile():
  home = os.environ['HOME'] 
  if OperationSystem() == 'Mac' :
    return "%s/.bash_profile" % home
  else :
     if os.path.isfile( ".bashrc") :
       return "%s/.bashrc" % home
     elif os.path.isfile("~/.bash_profile") :
       return "%s/.bash_profile" % home
def InsertPath() :
  profilepath = getBashProfile() 
  if not os.path.isfile( profilepath ) :
    print "%s is not a regular file !" % profilepath
    exit(1)
  else :
    profileobj = open( profilepath , "r+" )
    oldContent = profileobj.read()
    #do save old file
    tp =  time.strftime('%Y-%m-%d_%H:%M:%S') ;
    savefileName = "%s.cvsClient_saved_at_%s" % ( profilepath , tp )
    savefile = open(  savefileName , "w" )
    savefile.write( oldContent )
    savefile.close()
    msg = "\n\n##\n#Your previous %s file was backed up as %s \n##\n\n#cvsClient Installer addition on %s adding an appropriate PATH variable for use with cvsClient.\nexport PATH=%s:$PATH\n# Finished adapting your PATH environment variable for use with cvsClient.\n" % (  profilepath , savefileName , tp , os.environ['PWD'] )
    profileobj.write( msg )
    profileobj.close()
    print("Please run command :\n source %s " % profilepath )
if __name__ == '__main__' :
  print "Start to install"
  InsertPath()
  print "Success ! "
