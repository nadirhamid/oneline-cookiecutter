
## example controller, controls your app           
import ol
def {{ cookcutter.repo_name }}_init(startserver=True,sql='{{ cookiecutter.repo_name }}.sql'):
  print "starting new {{ cookiecutter.repo_name }} named {{ cookiecutter.repo_name }}"
  return ol.controller_init(startserver=startserver,sql=sql)
def {{ cookiecutter.repo_name }}_stop(stopserver=True):
  print "Stopping server"
  return ol.controller_stop(stopserver=stopserver)
def {{ cookiecutter.repo_name }}_clean(cleansql=True):
  print "Cleaning app contents"
  return ol.controller_clean(cleansql=cleansql)
def {{ cookiecutter.repo_name }}_restart():
  print "Restarting application"
  return ol.controller_restart()
                
