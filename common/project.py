#!/usr/bin/python
#coding=utf-8
#

import ConfigParser
import os
import platform


# Linux OS selection list
OSType = ['redhat', 'centos']
OSVersion = ['5.0', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6', '5.7', '5.8', '5.9',\
           '6.0', '6.1', '6.2', '6.3', '6.4', '6.5']
OSArch = ['x86_64', 'i686']

Prg_RootPath = os.getcwd()
Dpl_RootPath = Prg_RootPath + os.sep + 'deploy'

def PlatForm():
    SystemType = platform.system()
    if SystemType == 'Linux':
        Arch_Cur = platform.machine()
        OSnVer_Cur = list(platform.dist()[0:2])
        OSnVer_Cur.append(Arch_Cur)
        PlatForm_Cur = OSnVer_Cur
        return PlatForm_Cur
    elif SystemType == 'Windows':
        PlatForm_Cur = platform.platform()
        return PlatForm_Cur

def _DeployCreate_Judge(dplname, osver, dplloc, dpldep=None):
    Dpl_CfgName = str(dplname) + '.dpl'
    Dpl_CfgLoc = Dpl_RootPath + os.sep + Dpl_CfgName
    Dpl_DepFileName = str(dpldep) + '.dpl'
    Dpl_DepFileLoc = Dpl_RootPath + os.sep + Dpl_DepFileName
    Dpl_FilesLoc = dplloc

    if not os.path.exists(Dpl_CfgLoc):
        if PlatForm() in osver:
            if not os.path.exists(Dpl_FilesLoc):
                if not dpldep:
                    # print 'nodep, you can create'
                    return True
                elif os.path.exists(Dpl_DepFileLoc):
                    # print 'have dep , you can create'
                    return True
                else:
                    print '''have dep, but not exist file, can't create'''
            else: print '''dpl files location exist, can't create it'''
        else: print '''Plat form not match'''
    else: print '''dpl config file exist, can't create'''

    return False

def DeployCreate(dplname, osver, dplloc, dpldep=None):
    if _DeployCreate_Judge(dplname, osver, dplloc, dpldep=None):

        # Cfg_FH = open(Dpl_FileLoc, 'w')
        Dpl_CFGHD = ConfigParser.ConfigParser()
        Dpl_CFGHD.add_section(dplname)
        Dpl_CFGHD.set(dplname,'dependance', dpldep)
        Dpl_CFGHD.items(dplname)


