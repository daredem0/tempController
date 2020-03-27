#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:53:56 2020

@author: florian
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

import socket
from tcp_t import conTcp, disTcp, setTemp

class MyGrid(Widget):
    #name = ObjectProperty(None) #comes from kv file
    #email = ObjectProperty(None) #comes from kv file
    s=None
    def btn_set(self):
        rec = setTemp(float(self.new.text), self.s)
        print("Sent Temp: ", float(self.new.text), "Received Temp: ", rec)
        self.rec.text = str(rec)

    def btn_con(self):
        self.s = conTcp('192.168.1.164', 32)

    def btn_dis(self):
        disTcp(self.s)

class TemperatureController(App):
    def build(self):
        return MyGrid()
    
   
if __name__ == "__main__":
    TemperatureController().run()
