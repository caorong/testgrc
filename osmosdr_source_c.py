#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Osmosdr Source C
# Generated: Mon Oct 20 22:44:13 2014
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx

class osmosdr_source_c(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Osmosdr Source C")

        ##################################################
        # Variables
        ##################################################
        self.samplerate = samplerate = 2.048e6
        self.gain = gain = 10
        self.freq = freq = 100e6

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=100e6,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=2.048e6,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        _samplerate_sizer = wx.BoxSizer(wx.VERTICAL)
        self._samplerate_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_samplerate_sizer,
        	value=self.samplerate,
        	callback=self.set_samplerate,
        	label='samplerate',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._samplerate_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_samplerate_sizer,
        	value=self.samplerate,
        	callback=self.set_samplerate,
        	minimum=1.6e6,
        	maximum=3.2e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_samplerate_sizer)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(2.048e6)
        self.osmosdr_source_0.set_center_freq(100e6, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        _gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_gain_sizer,
        	value=self.gain,
        	callback=self.set_gain,
        	label='gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_gain_sizer,
        	value=self.gain,
        	callback=self.set_gain,
        	minimum=0,
        	maximum=30,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_gain_sizer)
        _freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	label='freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	minimum=50e6,
        	maximum=2.2e9,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_sizer)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.wxgui_fftsink2_0, 0))



    def get_samplerate(self):
        return self.samplerate

    def set_samplerate(self, samplerate):
        self.samplerate = samplerate
        self._samplerate_slider.set_value(self.samplerate)
        self._samplerate_text_box.set_value(self.samplerate)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self._gain_slider.set_value(self.gain)
        self._gain_text_box.set_value(self.gain)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = osmosdr_source_c()
    tb.Start(True)
    tb.Wait()
