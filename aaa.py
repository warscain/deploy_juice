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

# print aaa._DeployCreate_Judge('1',['Ubuntu-12.04-x86_64','centos-5.3-x86_64'],'/source/pycharm/deploy_juice/testdirdpl1',[2])
# print aaa._DeployCreate_Judge('2',['Ubuntu-12.04-x86_64','centos-5.3-x86_64'],'/source/pycharm/deploy_juice/testdirdpl2',[2])
# print aaa._DeployCreate_Judge('12311',['Ubuntu-12.04-x86_64','centos-5.3-x86_64'],'/source/pycharm/deploy_juice/testdirdplnew',[1,2,3])

aaa.DeployCreate('1',['Ubuntu-12.04-x86_64','centos-5.3-x86_64'],'/source/pycharm/deploy_juice/testdirdpl1')
aaa.DeployCreate('2',['Ubuntu-12.04-x86_64','centos-5.3-x86_64'],'/source/pycharm/deploy_juice/testdirdpl2')
aaa.DeployCreate('3',['Ubuntu-12.04-x86_64','centos-5.3-x86_64'],'/source/pycharm/deploy_juice/testdirdpl3')

aaa.DeployCreate('12311',['Ubuntu-12.04-x86_64','centos-5.3-x86_64'],'/source/pycharm/deploy_juice/testdirdplnew',[1,2,3])


# print aaa.DeployList()
# print aaa.DeployRead(12311)

# aaa.DeployDelete(1)
# aaa.DeployDelete(2)
# aaa.DeployDelete(3)
# aaa.DeployDelete(12311)

# def _List2string(list):
#     count = 0
#     num = len(list)
#     final = ''
#     for item in list:
#         count += 1
#         if count < num:
#             final += item + ', '
#         else:
#             final += item
#     print "aaaaa%saaaaa"  % final
#
# _List2string(['Ubuntu-12.04-x86_64','centos-5.3-x86_64'])