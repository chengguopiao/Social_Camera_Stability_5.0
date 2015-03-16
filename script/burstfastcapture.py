#!/usr/bin/python
# coding:utf-8

from uiautomatorplug.android import device as d
import unittest
import commands
import os
import string
import time
import sys
import util 
import string
import random

AD           = util.Adb()
tb           = util.TouchButton()
so           = util.SetOption()
sm           = util.SetCaptureMode()
Exposure     = util.Exposure
Scenes       = util.Scenes
Geo_Location = util.Geo_Location
Picture_Size = util.Picture_Size

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        AD.setUpDevice(False)
        sm.switchCaptureMode('Burst','Fast')

    def tearDown(self):
        super(CameraTest,self).tearDown()
        AD.pressBackKey(4)
        time.sleep(2)

    def testCaptureWithExposure(self):
        '''
            Summary: Capture image with Exposure
            Steps  :  
                1.Launch burst activity and select fast burst mode
                2.Check exposure setting icon, random set a value
                3.Touch shutter button to capture burst picture
                4.Exit activity
        '''
        randomoption = random.choice(Exposure) #Random select an option
        so.setCameraOption('Exposure',randomoption)
        tb.captureAndCheckPicCount('single',3,1,'burst')

    def testCapturePictureWithScenes(self):
        '''
            Summary: Capture image with Scene
            Steps  :  
                1.Launch burst activity and select fast burst mode
                2.Check scence mode ,set mode
                3.Touch shutter button to capture burst picture
                4.Exit activity
        '''
        randomoption = random.choice(Scenes) #Random select an option
        so.setCameraOption('Scenes',randomoption)
        tb.captureAndCheckPicCount('single',3,1,'burst')
        so.setCameraOption('Scenes','auto') #Force set scenes to off

    def testCaptureWithPictureSize(self):
        '''
            Summary: Capture image with Photo size
            Steps  :  
                1.Launch burst activity and select fast burst mode
                2.Check photo size ,set its size
                3.Touch shutter button to capture burst picture
                4.Exit activity
        '''
        randomoption = random.choice(Picture_Size) #Random select an option
        so.setCameraOption('Picture Size',randomoption)
        tb.captureAndCheckPicCount('single',3,1,'burst')

    def testCapturepictureWithGeoLocation(self):
        '''
            Summary: Capture image with Geo-tag
            Steps  : 
                1.Launch burst activity and select fast burst mode
                2.Check geo-tag ,set Geo on/off
                3.Touch shutter button to capture burst picture
                4.Exit activity
        '''
        randomoption = random.choice(Geo_Location) #Random select an option
        so.setCameraOption('Geo Location',randomoption)
        tb.captureAndCheckPicCount('single',3,1,'burst')
