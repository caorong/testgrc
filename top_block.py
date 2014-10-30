#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Thu Oct 30 12:08:41 2014
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.ch = ch = 90
        self.vdelay = vdelay = 50
        self.samp_rate = samp_rate = 2e6
        self.hsync = hsync = 0
        self.hdelay = hdelay = 50
        self.freq = freq = ch*1e6+1.25e6

        ##################################################
        # Blocks
        ##################################################
        _hsync_sizer = wx.BoxSizer(wx.VERTICAL)
        self._hsync_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_hsync_sizer,
        	value=self.hsync,
        	callback=self.set_hsync,
        	label='hsync',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._hsync_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_hsync_sizer,
        	value=self.hsync,
        	callback=self.set_hsync,
        	minimum=-10,
        	maximum=+10,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_hsync_sizer, 4, 0, 1, 4)
        _hdelay_sizer = wx.BoxSizer(wx.VERTICAL)
        self._hdelay_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_hdelay_sizer,
        	value=self.hdelay,
        	callback=self.set_hdelay,
        	label='hdelay',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._hdelay_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_hdelay_sizer,
        	value=self.hdelay,
        	callback=self.set_hdelay,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.GridAdd(_hdelay_sizer, 5, 0, 1, 1)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0.5,
        	v_offset=0.5,
        	t_scale=0.000020,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=3,
        	trig_mode=wxgui.TRIG_MODE_NORM,
        	y_axis_label="Counts",
        )
        self.GridAdd(self.wxgui_scopesink2_0.win, 0, 0, 3, 1)
        _vdelay_sizer = wx.BoxSizer(wx.VERTICAL)
        self._vdelay_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_vdelay_sizer,
        	value=self.vdelay,
        	callback=self.set_vdelay,
        	label='vdelay',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._vdelay_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_vdelay_sizer,
        	value=self.vdelay,
        	callback=self.set_vdelay,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.GridAdd(_vdelay_sizer, 5, 1, 1, 1)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(freq, 0)
        self.rtlsdr_source_0.set_freq_corr(-16, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, 80e3, 80e3, firdes.WIN_HAMMING, 6.76))
        self._ch_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.ch,
        	callback=self.set_ch,
        	label='ch',
        	choices=[90, 96, 102, 170, 176, 182, 188, 192, 198, 204, 210, 216],
        	labels=['1ch', '2ch', '3ch', '4ch', '5ch', '6ch', '7ch', '8ch', '9ch', '10ch', '11ch', '12ch'],
        )
        self.Add(self._ch_chooser)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((-2, ))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, hdelay*100)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((1.5, ))
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, 15734+hsync, 7, -3.5)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.low_pass_filter_0, 0), (self.wxgui_scopesink2_0, 1))
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.wxgui_scopesink2_0, 2))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.wxgui_scopesink2_0, 0))



    def get_ch(self):
        return self.ch

    def set_ch(self, ch):
        self.ch = ch
        self.set_freq(self.ch*1e6+1.25e6)
        self._ch_chooser.set_value(self.ch)

    def get_vdelay(self):
        return self.vdelay

    def set_vdelay(self, vdelay):
        self.vdelay = vdelay
        self._vdelay_slider.set_value(self.vdelay)
        self._vdelay_text_box.set_value(self.vdelay)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 80e3, 80e3, firdes.WIN_HAMMING, 6.76))
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_hsync(self):
        return self.hsync

    def set_hsync(self, hsync):
        self.hsync = hsync
        self.analog_sig_source_x_0.set_frequency(15734+self.hsync)
        self._hsync_slider.set_value(self.hsync)
        self._hsync_text_box.set_value(self.hsync)

    def get_hdelay(self):
        return self.hdelay

    def set_hdelay(self, hdelay):
        self.hdelay = hdelay
        self._hdelay_slider.set_value(self.hdelay)
        self._hdelay_text_box.set_value(self.hdelay)
        self.blocks_delay_0.set_dly(self.hdelay*100)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.rtlsdr_source_0.set_center_freq(self.freq, 0)

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
    tb = top_block()
    tb.Start(True)
    tb.Wait()
