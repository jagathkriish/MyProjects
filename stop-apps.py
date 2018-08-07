import subprocess
import shlex

import datetime
import time
st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H:%M:%S')
org = ''

space_apps_data = {'org1': ['hello', 'world'], 'org2': ['app1', 'app2']}

api = ''
user = ''
pwd = ''

for space_app in space_apps_data:
    login_specific_org_space = "cf login -a " + api + " -u " + user + " -p " + pwd + " -o " + org + " -s " + space + " --skip-ssl-validation"
    process = subprocess.Popen(shlex.split(login_specific_org_space), stdout=subprocess.PIPE)
    login_org_space = process.communicate()[0]
    print(login_org_space)
    for app in apps:
        process = subprocess.Popen(shlex.split("cf delete "+app), stdout=subprocess.PIPE)
        apps_list_res = process.communicate()[0] 
        apps_list = apps_list_res.split('\n')
