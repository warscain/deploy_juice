#!/usr/bin/python
#coding=utf-8
#

import ConfigParser
import os
import platform
import sys
import shutil

OSType = ['redhat', 'centos']
OSVersion = ['5.0', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6', '5.7', '5.8', '5.9',
             '6.0', '6.1', '6.2', '6.3', '6.4', '6.5']
OSArch = ['x86_64', 'i686']

class DeployPrj(object):
    def __init__(self):
        self.Prg_RootPath = os.getcwd()
        self.Dpl_RootPath = self.Prg_RootPath + os.sep + 'deploy'

    def PlatForm(self):
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

    def _DeployCreate_Judge(self, dplname, osver, dplloc, dpldep=None):
        Dpl_CfgName = str(dplname) + '.dpl'
        Dpl_CfgLoc = self.Dpl_RootPath + os.sep + Dpl_CfgName
        self._Dpl_CfgLoc = Dpl_CfgLoc
        Dpl_DepFileName = str(dpldep) + '.dpl'
        Dpl_DepFileLoc = self.Dpl_RootPath + os.sep + Dpl_DepFileName
        Dpl_FilesLoc = dplloc

        if not os.path.exists(Dpl_CfgLoc):
            if self.PlatForm() in osver:
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

    def DeployCreate(self, dplname, osver, dplloc, dpldep=None):
        if self._DeployCreate_Judge(dplname, osver, dplloc, dpldep=None):
            Dpl_CfgHD = ConfigParser.ConfigParser()
            Dpl_CfgHD.add_section(dplname)
            Dpl_CfgHD.set(dplname,'dependance', dpldep)
            Dpl_CfgHD.set(dplname,'osversion', osver)
            Dpl_CfgHD.set(dplname,'location', dplloc)
            Cfg_FHD = open(self._Dpl_CfgLoc, 'w')
            Dpl_CfgHD.write(Cfg_FHD)
            Cfg_FHD.close()
            #create Dpl_FilesLoc
            os.umask(0000)
            os.mkdir(dplloc, 0755)
            os.umask(0022)
            return True

    def DeployDelete(self, dplname):
        #get deploy config file path
        Dpl_CfgLoc = self.Dpl_RootPath + os.sep + str(dplname) + '.dpl'
        if os.path.exists(Dpl_CfgLoc):
            #get deploy files path
            Dpl_CfgHD = ConfigParser.ConfigParser()
            Dpl_CfgHD.read(Dpl_CfgLoc)
            Dpl_FilesLoc = Dpl_CfgHD.get(str(dplname), 'location')
            #remove config file
            os.remove(Dpl_CfgLoc)
            #remove other files
            if os.path.exists(Dpl_FilesLoc):
                shutil.rmtree(Dpl_FilesLoc)
            return True
        else:
            print '''Config file not exist'''
            return False

    def DeployList(self):
        return os.listdir(self.Dpl_RootPath)

    def DeployEdit(self):
        pass





