
## example controller, controls your app           
import ol
def OnelineModule_init(startserver=True,sql='OnelineModule.sql'):
  print "starting new OnelineModule named OnelineModule"
  return ol.controller_init(startserver=startserver,sql=sql)
def OnelineModule_stop(stopserver=True):
  print "Stopping server"
  return ol.controller_stop(stopserver=stopserver)
def OnelineModule_clean(cleansql=True):
  print "Cleaning app contents"
  return ol.controller_clean(cleansql=cleansql)
def OnelineModule_restart():
  print "Restarting application"
  return ol.controller_restart()
                
