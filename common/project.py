#!/usr/bin/python
#coding=utf-8
#

import ConfigParser
import os
import platform
import shutil


RHELType = ['redhat', 'centos']
RHELVersion = ['5.0', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6', '5.7', '5.8', '5.9',
             '6.0', '6.1', '6.2', '6.3', '6.4', '6.5']
RHELArch = ['x86_64', 'i686']
RHELSupported = []
for a in RHELType:
    for b in RHELVersion:
        for c in RHELArch:
            print a + '-' + b + '-' + c
            RHELSupported.append(a + '-' + b + '-' + c)


class DeployPrj(object):
    ''''''
    def __init__(self):
        self.Prg_RootPath = os.getcwd()
        self.Dpl_RootPath = self.Prg_RootPath + os.sep + 'deploy'

    def _List2String(self, AList):
        if AList:
            count = 0
            num = len(AList)
            final = ''
            for item in AList:
                count += 1
                if count < num:
                    final += str(item) + ', '
                else:
                    final += str(item)
            return final
        else:
            return None

    def _String2List(self, Astring):
        final = Astring.split(',')
        num = len(final)
        count = 0
        for item in final:
            final[count] = item.strip()
            count += 1
        return final

    def _FilesExist(self, files):
        for File in files:
            if not os.path.exists(File):
                return False
        return True

    def _MkDeepDir(self, dirloc, dirmod):
        if not os.path.exists(dirloc):
            self._MkDeepDir(os.path.dirname(dirloc), dirmod)
            os.mkdir(dirloc, dirmod)

    def _PlatForm(self):
        SystemType = platform.system()
        if SystemType == 'Linux':
            Arch_Cur = platform.machine()
            OSnVer_Cur = list(platform.dist()[0:2])
            PlatForm_Cur = OSnVer_Cur[0] + '-' + OSnVer_Cur[1] + '-' + Arch_Cur
            return PlatForm_Cur
        elif SystemType == 'Windows':
            PlatForm_Cur = platform.platform()
            return PlatForm_Cur

    def _DeployCreate_Judge(self, dplname, osver, dplloc, dpldep=None):
        Dpl_CfgName = str(dplname) + '.dpl'
        Dpl_CfgLoc = self.Dpl_RootPath + os.sep + Dpl_CfgName
        self._Dpl_CfgLoc = Dpl_CfgLoc
        Dpl_FilesLoc = dplloc

        Dpl_DepFilesLoc_List = []
        if dpldep:
            for item in dpldep:
                Dpl_DepFileName = str(item) + '.dpl'
                Dpl_DepFileLoc = self.Dpl_RootPath + os.sep + Dpl_DepFileName
                Dpl_DepFilesLoc_List.append(Dpl_DepFileLoc)

        if not os.path.exists(Dpl_CfgLoc):
            if self._PlatForm() in osver:
                if not os.path.exists(Dpl_FilesLoc):
                    if dpldep:
                        if self._FilesExist(Dpl_DepFilesLoc_List):
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
        dplname = str(dplname)
        osver = osver
        dplloc = str(dplloc)
        dpldep = dpldep
        if self._DeployCreate_Judge(dplname, osver, dplloc, dpldep):
            ## create Dpl
            Dpl_CfgHD = ConfigParser.ConfigParser()
            Dpl_CfgHD.add_section(dplname)
            Dpl_CfgHD.set(dplname,'dependence', self._List2String(dpldep))
            Dpl_CfgHD.set(dplname,'osversion', self._List2String(osver))
            Dpl_CfgHD.set(dplname,'location', dplloc)
            Cfg_FHD = open(self._Dpl_CfgLoc, 'w')
            Dpl_CfgHD.write(Cfg_FHD)
            Cfg_FHD.close()
            ## create Dpl_FilesLoc
            os.umask(0000)
            self._MkDeepDir(dplloc, 0755)
            os.umask(0022)
            return True
        else:
            return False

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

    def DeployRead(self, dplname):
        ## define a return list
        ReturnList = []
        ## open dpl config handler
        Dpl_CfgLoc = self.Dpl_RootPath + os.sep + str(dplname) + '.dpl'
        if os.path.exists(Dpl_CfgLoc):
            Dpl_CfgHD = ConfigParser.ConfigParser()
            Dpl_CfgHD.read(Dpl_CfgLoc)

            ReturnList.append(str(dplname))
            ReturnList.append(self._String2List(Dpl_CfgHD.get(str(dplname), 'dependence')))
            ReturnList.append(self._String2List(Dpl_CfgHD.get(str(dplname), 'osversion')))
            ReturnList.append(Dpl_CfgHD.get(str(dplname), 'location'))

            return ReturnList
        else:
            return False

    def DeployCheck(self, dplname):
        print '''This feature will coming soon.'''
        pass

    def DeployEdit(self, dplname):
        print '''This feature will coming soon.'''
        pass

