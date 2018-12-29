# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:01:35 2015

@author: thewhitetulip
"""

import os
import shutil
import sys

home_dir = os.environ['HOME']

path=""

if sys.platform.startswith('win') == True:
    path = os.path.join(home_dir, '\\Downloads')
elif sys.platform.startswith('linux')==True or sys.platform.startswith('darwin')==True:
    path = os.path.join(home_dir, "Downloads")

if not os.path.exists(path):
    print("You are using an unsupported version of this program, please submit your downloads folder path on github, ")
    exit(0)
   
files = os.listdir(path)
#extensions = [ifile.split(".")[-1] for ifile in files if os.path.isfile(path+'/'+ifile) and '.' in ifile]
#print(set(extensions))

doc = ('rtf', 'docx','doc',  'docm', 'epub', 'xls','xlsx', 'torrent','pdf', 'ica','xml','ppt','pptx')
audio=('mp3','wav','ogg')
videos = ('mp4','mkv')
binaries = ('exe', 'oxt', 'deb', 'apk','msi')
images = ('jpg','jpeg','png','tiff','svg')
compressed = ('tgz', 'gz', 'xz','bz2', 'zip', 'iso')
code=('js','py', 'c', 'cpp', 'java','rb','css','go')

#directories = [ifile.split(' ')[0] for ifile in files if os.path.isdir(path+'/'+ifile)]


DOCS = '/'.join((path,'Documents'))
AUDIO = '/'.join((path,'Audio'))
VIDEOS = '/'.join((path,'Video'))
BINARIES='/'.join((path,'Binaries'))
IMAGES='/'.join((path,'Images'))
CODE='/'.join((path,'Code'))
COMPRESSED='/'.join((path,'Compressed'))

dirlist = [DOCS, AUDIO, VIDEOS, BINARIES,IMAGES,CODE,COMPRESSED]

for dirname in dirlist:
    if not os.path.exists(dirname) and not os.path.isfile(dirname):
        os.mkdir(dirname)

files = [path+'/'+ifile for ifile in files if os.path.isfile(path+'/'+ifile)]

for ifile in files:
    extension=ifile.split('.')[-1].lower()
    if extension in doc:
        try:
            shutil.move(ifile, DOCS)
        except:
            print("Error")
    elif extension in audio:
        try:
            shutil.move(ifile, AUDIO)            
        except:
            pass
    elif extension in videos:
        try:
            shutil.move(ifile, VIDEOS)            
        except:
            pass
    elif extension in images:
        try:
            shutil.move(ifile, IMAGES)
        except:
            pass
    elif extension in compressed:
        try:
            shutil.move(ifile, COMPRESSED)            
        except:
            pass
    elif extension in binaries:
        try:
            shutil.move(ifile, BINARIES)
        except:
            pass
    elif extension in code:
        try:
            shutil.move(ifile, CODE)
        except:
            pass
