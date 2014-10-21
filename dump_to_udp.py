#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Dump To Udp
# Generated: Tue Oct 21 19:18:53 2014
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx

class dump_to_udp(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Dump To Udp")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 8e5
        self.channel_width = channel_width = 200e3
        self.channel_freq = channel_freq = 99.3e6
        self.center_freq = center_freq = 101.8e6
        self.audio_gain = audio_gain = 1

        ##################################################
        # Blocks
        ##################################################
        _center_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._center_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_center_freq_sizer,
        	value=self.center_freq,
        	callback=self.set_center_freq,
        	label='center_freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._center_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_center_freq_sizer,
        	value=self.center_freq,
        	callback=self.set_center_freq,
        	minimum=85e6,
        	maximum=120e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_center_freq_sizer)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(center_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.digital_gmsk_demod_0 = digital.gmsk_demod(
        	samples_per_symbol=2,
        	gain_mu=0.175,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        _channel_width_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_width_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_width_sizer,
        	value=self.channel_width,
        	callback=self.set_channel_width,
        	label='channel_width',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_width_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_width_sizer,
        	value=self.channel_width,
        	callback=self.set_channel_width,
        	minimum=10e3,
        	maximum=1000e3,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_channel_width_sizer)
        _channel_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq_sizer,
        	value=self.channel_freq,
        	callback=self.set_channel_freq,
        	label='channel_freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq_sizer,
        	value=self.channel_freq,
        	callback=self.set_channel_freq,
        	minimum=50e6,
        	maximum=220e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_channel_freq_sizer)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_char*1, "0.0.0.0", 5005, 1472, True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, "/home/caorong/workspace_hackrf/123.ts", True)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code="",
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )
        _audio_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._audio_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_audio_gain_sizer,
        	value=self.audio_gain,
        	callback=self.set_audio_gain,
        	label='audio_gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._audio_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_audio_gain_sizer,
        	value=self.audio_gain,
        	callback=self.set_audio_gain,
        	minimum=0,
        	maximum=10,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_audio_gain_sizer)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_gmsk_demod_0, 0), (self.blks2_packet_decoder_0, 0))
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.digital_gmsk_demod_0, 0))



    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_channel_width(self):
        return self.channel_width

    def set_channel_width(self, channel_width):
        self.channel_width = channel_width
        self._channel_width_slider.set_value(self.channel_width)
        self._channel_width_text_box.set_value(self.channel_width)

    def get_channel_freq(self):
        return self.channel_freq

    def set_channel_freq(self, channel_freq):
        self.channel_freq = channel_freq
        self._channel_freq_slider.set_value(self.channel_freq)
        self._channel_freq_text_box.set_value(self.channel_freq)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self._center_freq_slider.set_value(self.center_freq)
        self._center_freq_text_box.set_value(self.center_freq)
        self.osmosdr_source_0.set_center_freq(self.center_freq, 0)

    def get_audio_gain(self):
        return self.audio_gain

    def set_audio_gain(self, audio_gain):
        self.audio_gain = audio_gain
        self._audio_gain_slider.set_value(self.audio_gain)
        self._audio_gain_text_box.set_value(self.audio_gain)

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
    tb = dump_to_udp()
    tb.Start(True)
    tb.Wait()
