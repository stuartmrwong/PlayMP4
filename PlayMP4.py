# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:57:50 2019

@author: Stuart
"""

import os

from pycaw.pycaw import AudioUtilities 
    
"""
#the below code will actually mute everything/ all processes except vlc

sessions = AudioUtilities.GetAllSessions()
for session in sessions:
    volume = session.SimpleAudioVolume
    if session.Process and session.Process.name() == "vlc.exe":
        volume.SetMute(0, None)
    else:
        volume.SetMute(0, None)
"""    
  
def playmp4(path):
    os.startfile(path)
 

playmp4(r"c:\users\stuart\【ワイズマ】( ワールドイズマイン アニメーション MV) World is Mine Music Video.mp4")


