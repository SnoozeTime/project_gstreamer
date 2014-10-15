#-*- coding:utf-8 -*-
#!/usr/bin/python

import pygst
pygst.require("0.10")
import gst
import pygtk
import gtk
#gst-launch-0.10 filesrc location=jonobacon-beatingheart.ogg ! decodebin ! audioconvert ! alsasink
class Main:
    def __init__(self):
        self.pipeline = gst.Pipeline("mypipeline")

        #create an element for the pipeline. First arg is what is the element, and second arg is name of the element
        self.audiotestsrc = gst.element_factory_make("filesrc", "audio")
        self.pipeline.add(self.audiotestsrc) # add it to our pipeline
        #propertie of the element
        self.audiotestsrc.set_property("location", "kenshin.mp3")
        
        #decodebin
        self.decodebin = gst.element_factory_make("decodebin", "decode")
        self.pipeline.add(self.decodebin)

        #audioconvert
        self.audioconvert = gst.element_factory_make("audioconvert", "audioconv")
        self.pipeline.add(self.audioconvert)

        #element: use alsasink to send sound to our sound card
        self.sink = gst.element_factory_make("alsasink", "sink")
        self.pipeline.add(self.sink)

        #link both elements
        self.audiotestsrc.link(self.decodebin)
        self.decodebin.link(self.audioconvert)
        self.audioconvert.link(self.sink)
        #state of the pipeline
        self.pipeline.set_state(gst.STATE_PLAYING)
#run the script
start=Main()
gtk.main()