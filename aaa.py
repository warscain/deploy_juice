#!/usr/bin/python
#coding=utf-8
#
#code style:
#Dir_Working = 'aaaa'
#def PrjControl(hostname)
#Class HostControl
#


from common import project

# def DeployCreate(dplname, osver, dplloc, dpldep=None):
aaa = project.DeployPrj()

# print aaa._DeployCreate_Judge('1',['Ubuntu-12.04-x86_64','centos-5.3-x86_64'],'/source/pycharm/deploy_juice/testdirdpl1',[2])
# print aaa._DeployCreate_Judge('2',['Ubuntu-12.04-x86_64','centos-5.3-x86_64'],'/source/pycharm/deploy_juice/testdirdpl2',[2])
# print aaa._DeployCreate_Judge('12311',['Ubuntu-12.04-x86_64','centos-5.3-x86_64'],'/source/pycharm/deploy_juice/testdirdplnew',[1,2,3])

aaa.DeployCreate('1',['Ubuntu-12.04-x86_64','centos-5.3-x86_64'],'/source/pycharm/deploy_juice/testdirdpl/1')
aaa.DeployCreate('2',['Ubuntu-12.04-x86_64','centos-5.3-x86_64'],'/source/pycharm/deploy_juice/testdirdpl/2')
aaa.DeployCreate('3',['Ubuntu-12.04-x86_64','centos-5.3-x86_64'],'/source/pycharm/deploy_juice/testdirdpl/3')
aaa.DeployCreate('12311',['Ubuntu-12.04-x86_64','centos-5.3-x86_64'],'/source/pycharm/deploy_juice/testdirdpl/12311',["1",2,3])
aaa.DeployCreate('4444',['Ubuntu-12.04-x86_64'],'/source/pycharm/deploy_juice/testdirdpl/4444',[12311])
aaa.DeployCreate('555',['Ubuntu-12.04-x86_64'],'/source/pycharm/deploy_juice/testdirdpl/555',[12311,2])

print 'DPL LIST', aaa.DeployList()
print aaa.DeployRead(555)
print aaa.DeployRead('1')
print aaa.DeployRead(12311)

aaa.DeployDelete(1)
aaa.DeployDelete(2)
aaa.DeployDelete(3)
aaa.DeployDelete(12311)
aaa.DeployDelete(4444)
aaa.DeployDelete(555)

aaa._MkDeepDir('/tmp/a/b/c/d/s/12', 0755)










