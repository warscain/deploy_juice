#!/usr/bin/python
#coding=utf-8
#

import ConfigParser
import os
import platform
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
            PlatForm_Cur = OSnVer_Cur[0] + '-' + OSnVer_Cur[1] + '-' + Arch_Cur
            return PlatForm_Cur
        elif SystemType == 'Windows':
            PlatForm_Cur = platform.platform()
            return PlatForm_Cur

    def _List2string(self, list):
        if list:
            count = 0
            num = len(list)
            final = ''
            for item in list:
                count += 1
                if count < num:
                    final += str(item) + ', '
                else:
                    final += str(item)
            return final
        else:
            return None

    def _FilesExist(self, Files):
        for File in Files:
            if not os.path.exists(File):
                return False
        return True

    def _DeployCreate_Judge(self, dplname, osver, dplloc, dpldep=None):
        Dpl_CfgName = str(dplname) + '.dpl'
        Dpl_CfgLoc = self.Dpl_RootPath + os.sep + Dpl_CfgName
        self._Dpl_CfgLoc = Dpl_CfgLoc
        Dpl_FilesLoc = dplloc

        Dpl_DepFilesLoc = []
        if dpldep:
            for item in dpldep:
                Dpl_DepFileName = str(item) + '.dpl'
                Dpl_DepFileLoc = self.Dpl_RootPath + os.sep + Dpl_DepFileName
                Dpl_DepFilesLoc.append(Dpl_DepFileLoc)

        if not os.path.exists(Dpl_CfgLoc):
            if self.PlatForm() in osver:
                if not os.path.exists(Dpl_FilesLoc):
                    if dpldep:
                        if self._FilesExist(Dpl_DepFilesLoc):
                            print '''dep dpl exist can create.'''
                            return True
                        else:
                            print '''some dep dpl not exist, can't create'''
                    else:
                        print '''dep dpl is none, can create'''
                        return True
                else: print '''dpl files location exist, can't create'''
            else: print '''Plat form not match, can't create'''
        else: print '''dpl config file exist, can't create'''
        return False

    def DeployCreate(self, dplname, osver, dplloc, dpldep=None):
        if self._DeployCreate_Judge(dplname, osver, dplloc, dpldep):
            Dpl_CfgHD = ConfigParser.ConfigParser()
            Dpl_CfgHD.add_section(dplname)
            Dpl_CfgHD.set(dplname,'dependence', self._List2string(dpldep))
            Dpl_CfgHD.set(dplname,'osversion', self._List2string(osver))
            Dpl_CfgHD.set(dplname,'location', dplloc)
            Cfg_FHD = open(self._Dpl_CfgLoc, 'w')
            Dpl_CfgHD.write(Cfg_FHD)
            Cfg_FHD.close()
            ## create Dpl_FilesLoc
            os.umask(0000)
            os.mkdir(dplloc, 0755)
            os.umask(0022)
            return True

    def DeployDelete(self, dplname):
        ## get deploy config file path
        Dpl_CfgLoc = self.Dpl_RootPath + os.sep + str(dplname) + '.dpl'
        if os.path.exists(Dpl_CfgLoc):
            ## get deploy files path
            Dpl_CfgHD = ConfigParser.ConfigParser()
            Dpl_CfgHD.read(Dpl_CfgLoc)
            Dpl_FilesLoc = Dpl_CfgHD.get(str(dplname), 'location')
            ## remove config file
            os.remove(Dpl_CfgLoc)
            ## remove other files, only do if the path exist. so 'return' position is at this place.
            if os.path.exists(Dpl_FilesLoc):
                shutil.rmtree(Dpl_FilesLoc)
            return True
        else:
            print '''Config file not exist'''
            return False

    def DeployList(self):
        ReturnList = []
        for f in os.listdir(self.Dpl_RootPath):
            if f.endswith('.dpl'):
               ReturnList.append(f.replace('.dpl','') )
        return ReturnList

    def DeployEdit(self, dplname):
        print '''This feature will coming soon.'''
        pass

    def DeployRead(self, dplname):
        ## define a return list
        ReturnList = []
        ## open dpl config handler
        Dpl_CfgLoc = self.Dpl_RootPath + os.sep + str(dplname) + '.dpl'
        Dpl_CfgHD = ConfigParser.ConfigParser()
        Dpl_CfgHD.read(Dpl_CfgLoc)

        ReturnList.append(str(dplname))
        ReturnList.append(Dpl_CfgHD.get(str(dplname), 'dependence'))
        ReturnList.append(Dpl_CfgHD.get(str(dplname), 'osversion'))
        ReturnList.append(Dpl_CfgHD.get(str(dplname), 'location'))
        ## write result to return list
        # try:
        #     ReturnList.append(str(dplname))
        #     ReturnList.append(Dpl_CfgHD.get(str(dplname), 'dependence'))
        #     ReturnList.append(Dpl_CfgHD.get(str(dplname), 'osversion'))
        #     ReturnList.append(Dpl_CfgHD.get(str(dplname), 'location'))
        # except ConfigParser.NoSectionError:
        #     print '''No such deploy!'''
        ## return
        return ReturnList






