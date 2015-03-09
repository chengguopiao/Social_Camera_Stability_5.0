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

#Written by ZhuYanbo

a              = util.Adb()
sm             = util.SetCaptureMode()
so             = util.SetOption()
tb             = util.TouchButton()
Exposure       = util.Exposure
Scenes         = util.Scenes
Picture_Size   = util.Picture_Size
Geo_Location   = util.Geo_Location
Face_Detection = util.Face_Detection
Self_Timer     = util.Self_Timer

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        a.setUpDevice()
        sm.switchCaptureMode('Single','HDR')

    def tearDown(self):
        super(CameraTest,self).tearDown()
        a.pressBackKey(4)

    # Testcase 1
    def testCapturePictureWithFD(self):
        '''
            Summary: Capture image with FD/FR
            Steps  : 
                1.Launch HDR capture activity
                2.Set FD/FR ON/OFF
                3.Touch shutter button to capture picture
                4.Exit activity
        '''
        fdfr = random.choice(Face_Detection)
        # Step 2
        so.setCameraOption('Face Detection',fdfr)
        # Step 3
        tb.captureAndCheckPicCount('single')

    # Testcase 2
    def testCapturepictureWithGeoLocation(self):
        '''
            Summary: Capture image with Geo-tag
            Steps  : 
                1.Launch HDR capture activity
                2.Set photo Geo-tag ON/OFF
                3.Touch shutter button to capture picture
                4.Exit  activity
        '''
        geo = random.choice(Geo_Location)
        # Step 2
        so.setCameraOption('Geo Location',geo)
        # Step 3
        tb.captureAndCheckPicCount('single')

    # Testcase 3
    def testCapturePictureWithPictureSize(self):
        '''
            Summary: Capture image with Photo size
            Steps  : 
                1.Launch HDR capture activity
                2.Set photo size 6MP/13MP
                3.Touch shutter button to capture picture
                4.Exit  activity
        '''
        size = random.choice(Picture_Size)
        # Step 2
        so.setCameraOption('Picture Size',size)
        # Step 3
        tb.captureAndCheckPicCount('single')
        so.setCameraOption('Picture Size','WideScreen') #Force set to the default setting

    # Testcase 4
    def testCapturePictureWithSelfTimer(self):
        '''
        Summary: Capture image with Self-timer
        Steps  :  1.Launch HDR capture activity
                2.Set Self-timer setting
                3.Touch shutter button to capture picture
                4.Exit  activity
        '''
        timer = random.choice(Self_Timer)
        # Step 2
        so.setCameraOption('Self Timer',timer)
        # Step 3
        tb.captureAndCheckPicCount('single',int(timer))
        so.setCameraOption('Self Timer','0') #Force set timer to off
