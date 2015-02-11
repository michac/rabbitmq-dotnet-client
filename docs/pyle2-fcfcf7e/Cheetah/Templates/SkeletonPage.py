#!/usr/bin/env python


"""A Skeleton HTML page template, that provides basic structure and utility methods.
"""


##################################################
## DEPENDENCIES
import sys
import os
import os.path
from os.path import getmtime, exists
import time
import types
import __builtin__
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import DummyTransaction
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from Cheetah.Templates._SkeletonPage import _SkeletonPage

##################################################
## MODULE CONSTANTS
try:
    True, False
except NameError:
    True, False = (1==1), (1==0)
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.0rc6'
__CHEETAH_versionTuple__ = (2, 0, 0, 'candidate', 6)
__CHEETAH_genTime__ = 1139107954.3640411
__CHEETAH_genTimestamp__ = 'Sat Feb  4 18:52:34 2006'
__CHEETAH_src__ = 'src/Templates/SkeletonPage.tmpl'
__CHEETAH_srcLastModified__ = 'Mon Oct  7 11:37:30 2002'
__CHEETAH_docstring__ = 'Autogenerated by CHEETAH: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class SkeletonPage(_SkeletonPage):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        _SkeletonPage.__init__(self, *args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def writeHeadTag(self, **KWS):



        ## CHEETAH: generated from #block writeHeadTag at line 22, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write('<head>\n<title>')
        _v = VFFSL(SL,"title",True) # '$title' on line 24, col 8
        if _v is not None: write(_filter(_v, rawExpr='$title')) # from line 24, col 8.
        write('</title>\n')
        _v = VFFSL(SL,"metaTags",True) # '$metaTags' on line 25, col 1
        if _v is not None: write(_filter(_v, rawExpr='$metaTags')) # from line 25, col 1.
        write(' \n')
        _v = VFFSL(SL,"stylesheetTags",True) # '$stylesheetTags' on line 26, col 1
        if _v is not None: write(_filter(_v, rawExpr='$stylesheetTags')) # from line 26, col 1.
        write(' \n')
        _v = VFFSL(SL,"javascriptTags",True) # '$javascriptTags' on line 27, col 1
        if _v is not None: write(_filter(_v, rawExpr='$javascriptTags')) # from line 27, col 1.
        write('\n</head>\n')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def writeBody(self, **KWS):



        ## CHEETAH: generated from #block writeBody at line 36, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write('This skeleton page has no flesh. Its body needs to be implemented.\n')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        
        ## START CACHE REGION: ID=header. line 6, col 1 in the source.
        _RECACHE_header = False
        _cacheRegion_header = self.getCacheRegion(regionID='header', cacheInfo={'type': 2, 'id': 'header'})
        if _cacheRegion_header.isNew():
            _RECACHE_header = True
        _cacheItem_header = _cacheRegion_header.getCacheItem('header')
        if _cacheItem_header.hasExpired():
            _RECACHE_header = True
        if (not _RECACHE_header) and _cacheItem_header.getRefreshTime():
            try:
                _output = _cacheItem_header.renderOutput()
            except KeyError:
                _RECACHE_header = True
            else:
                write(_output)
                del _output
        if _RECACHE_header or not _cacheItem_header.getRefreshTime():
            _orig_transheader = trans
            trans = _cacheCollector_header = DummyTransaction()
            write = _cacheCollector_header.response().write
            _v = VFFSL(SL,"docType",True) # '$docType' on line 7, col 1
            if _v is not None: write(_filter(_v, rawExpr='$docType')) # from line 7, col 1.
            write('\n')
            _v = VFFSL(SL,"htmlTag",True) # '$htmlTag' on line 8, col 1
            if _v is not None: write(_filter(_v, rawExpr='$htmlTag')) # from line 8, col 1.
            write('''
<!-- This document was autogenerated by Cheetah(http://CheetahTemplate.org). 
Do not edit it directly!

Copyright ''')
            _v = VFFSL(SL,"currentYr",True) # '$currentYr' on line 12, col 11
            if _v is not None: write(_filter(_v, rawExpr='$currentYr')) # from line 12, col 11.
            write(' - ')
            _v = VFFSL(SL,"siteCopyrightName",True) # '$siteCopyrightName' on line 12, col 24
            if _v is not None: write(_filter(_v, rawExpr='$siteCopyrightName')) # from line 12, col 24.
            write(' - All Rights Reserved.\nFeel free to copy any javascript or html you like on this site,\nprovided you remove all links and/or references to ')
            _v = VFFSL(SL,"siteDomainName",True) # '$siteDomainName' on line 14, col 52
            if _v is not None: write(_filter(_v, rawExpr='$siteDomainName')) # from line 14, col 52.
            write('''
However, please do not copy any content or images without permission.

''')
            _v = VFFSL(SL,"siteCredits",True) # '$siteCredits' on line 17, col 1
            if _v is not None: write(_filter(_v, rawExpr='$siteCredits')) # from line 17, col 1.
            write('''

-->


''')
            self.writeHeadTag(trans=trans)
            write('\n')
            trans = _orig_transheader
            write = trans.response().write
            _cacheData = _cacheCollector_header.response().getvalue()
            _cacheItem_header.setData(_cacheData)
            write(_cacheData)
            del _cacheData
            del _cacheCollector_header
            del _orig_transheader
        ## END CACHE REGION: header
        
        write('\n')
        _v = VFFSL(SL,"bodyTag",True) # '$bodyTag' on line 34, col 1
        if _v is not None: write(_filter(_v, rawExpr='$bodyTag')) # from line 34, col 1.
        write('\n\n')
        self.writeBody(trans=trans)
        write('''
</body>
</html>



''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_SkeletonPage= 'respond'

## END CLASS DEFINITION

if not hasattr(SkeletonPage, '_initCheetahAttributes'):
    templateAPIClass = getattr(SkeletonPage, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(SkeletonPage)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=SkeletonPage()).run()

