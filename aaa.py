#!/usr/bin/python
#coding=utf-8
#
#code style:
#Dir_Working = 'aaaa'
#def PrjControl(hostname)
#Class HostControl
#


from common import project




# /\def DeployCreate(dplname, osver, dplloc, dpldep=None):
aaa = project.DeployPrj()
# aaa.DeployCreate('1231',[['a'],['Ubuntu', '12.04', 'x86_64']],'/source/pycharm/deploy_juice/testdirdpl')
# aaa.DeployDelete(1231)
print aaa.DeployList()
