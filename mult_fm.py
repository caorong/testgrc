#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Mult Fm
# Generated: Fri Oct 24 13:58:26 2014
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx

class mult_fm(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Mult Fm")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 11e6
        self.channel_width = channel_width = 200e3
        self.channel_freq1 = channel_freq1 = 94.0e6
        self.center_freq = center_freq = 97.9e6
        self.audio_gain1 = audio_gain1 = 1

        ##################################################
        # Blocks
        ##################################################
        _channel_freq1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq1_sizer,
        	value=self.channel_freq1,
        	callback=self.set_channel_freq1,
        	label='channel_freq1',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq1_sizer,
        	value=self.channel_freq1,
        	callback=self.set_channel_freq1,
        	minimum=87.9e6,
        	maximum=107.9e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_channel_freq1_sizer)
        _audio_gain1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._audio_gain1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_audio_gain1_sizer,
        	value=self.audio_gain1,
        	callback=self.set_audio_gain1,
        	label='audio_gain1',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._audio_gain1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_audio_gain1_sizer,
        	value=self.audio_gain1,
        	callback=self.set_audio_gain1,
        	minimum=0,
        	maximum=10,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_audio_gain1_sizer)
        self.rational_resampler_xxx_0_0_0_0_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0_0_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
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
          
        self.low_pass_filter_0_0_0_0_0 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0_0 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_sink_0_0_0_0_0 = blocks.wavfile_sink("/home/caorong/workspace_hackrf/105.7.wav", 1, 48000, 8)
        self.blocks_wavfile_sink_0_0_0_0 = blocks.wavfile_sink("/home/caorong/workspace_hackrf/103.7.wav", 1, 48000, 8)
        self.blocks_wavfile_sink_0_0_0 = blocks.wavfile_sink("/home/caorong/workspace_hackrf/97.7.wav", 1, 48000, 8)
        self.blocks_wavfile_sink_0_0 = blocks.wavfile_sink("/home/caorong/workspace_hackrf/101.7.wav", 1, 48000, 8)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink("/home/caorong/workspace_hackrf/94.0.wav", 1, 48000, 8)
        self.blocks_udp_sink_0_3 = blocks.udp_sink(gr.sizeof_short*1, "0.0.0.0", 5009, 1472, True)
        self.blocks_udp_sink_0_2 = blocks.udp_sink(gr.sizeof_short*1, "0.0.0.0", 5008, 1472, True)
        self.blocks_udp_sink_0_1 = blocks.udp_sink(gr.sizeof_short*1, "0.0.0.0", 5007, 1472, True)
        self.blocks_udp_sink_0_0 = blocks.udp_sink(gr.sizeof_short*1, "0.0.0.0", 5006, 1472, True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_short*1, "0.0.0.0", 5005, 1472, True)
        self.blocks_multiply_xx_0_0_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((audio_gain1, ))
        self.blocks_float_to_short_0_3 = blocks.float_to_short(1, 32767)
        self.blocks_float_to_short_0_2 = blocks.float_to_short(1, 32767)
        self.blocks_float_to_short_0_1 = blocks.float_to_short(1, 32767)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 32767)
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 32767)
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_wfm_rcv_0_0_0_0_0 = analog.wfm_rcv(
        	quad_rate=480e3,
        	audio_decimation=10,
        )
        self.analog_wfm_rcv_0_0_0_0 = analog.wfm_rcv(
        	quad_rate=480e3,
        	audio_decimation=10,
        )
        self.analog_wfm_rcv_0_0_0 = analog.wfm_rcv(
        	quad_rate=480e3,
        	audio_decimation=10,
        )
        self.analog_wfm_rcv_0_0 = analog.wfm_rcv(
        	quad_rate=480e3,
        	audio_decimation=10,
        )
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=480e3,
        	audio_decimation=10,
        )
        self.analog_sig_source_x_4 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - 105.7e6, 1, 0)
        self.analog_sig_source_x_3 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - 103.7e6, 1, 0)
        self.analog_sig_source_x_2 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - 97.7e6, 1, 0)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - 101.7e6, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - channel_freq1, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.analog_wfm_rcv_0_0, 0))
        self.connect((self.analog_wfm_rcv_0_0, 0), (self.blocks_wavfile_sink_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_2, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.low_pass_filter_0_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.analog_wfm_rcv_0_0_0, 0))
        self.connect((self.analog_wfm_rcv_0_0_0, 0), (self.blocks_wavfile_sink_0_0_0, 0))
        self.connect((self.analog_sig_source_x_3, 0), (self.blocks_multiply_xx_0_0_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0_0_0, 0), (self.low_pass_filter_0_0_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0_0, 0), (self.rational_resampler_xxx_0_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0, 0), (self.analog_wfm_rcv_0_0_0_0, 0))
        self.connect((self.analog_wfm_rcv_0_0_0_0, 0), (self.blocks_wavfile_sink_0_0_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_0_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_0_0_0_0, 0))
        self.connect((self.blocks_float_to_short_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_float_to_short_0, 0))
        self.connect((self.blocks_float_to_short_0_0, 0), (self.blocks_udp_sink_0_0, 0))
        self.connect((self.analog_wfm_rcv_0_0, 0), (self.blocks_float_to_short_0_0, 0))
        self.connect((self.blocks_float_to_short_0_1, 0), (self.blocks_udp_sink_0_1, 0))
        self.connect((self.analog_wfm_rcv_0_0_0, 0), (self.blocks_float_to_short_0_1, 0))
        self.connect((self.blocks_float_to_short_0_2, 0), (self.blocks_udp_sink_0_2, 0))
        self.connect((self.analog_wfm_rcv_0_0_0_0, 0), (self.blocks_float_to_short_0_2, 0))
        self.connect((self.analog_wfm_rcv_0_0_0_0_0, 0), (self.blocks_float_to_short_0_3, 0))
        self.connect((self.blocks_float_to_short_0_3, 0), (self.blocks_udp_sink_0_3, 0))
        self.connect((self.analog_sig_source_x_4, 0), (self.blocks_multiply_xx_0_0_0_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0_0_0_0, 0), (self.low_pass_filter_0_0_0_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0_0_0, 0), (self.rational_resampler_xxx_0_0_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0_0, 0), (self.analog_wfm_rcv_0_0_0_0_0, 0))
        self.connect((self.analog_wfm_rcv_0_0_0_0_0, 0), (self.blocks_wavfile_sink_0_0_0_0_0, 0))



    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_4.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_3.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_channel_width(self):
        return self.channel_width

    def set_channel_width(self, channel_width):
        self.channel_width = channel_width

    def get_channel_freq1(self):
        return self.channel_freq1

    def set_channel_freq1(self, channel_freq1):
        self.channel_freq1 = channel_freq1
        self._channel_freq1_slider.set_value(self.channel_freq1)
        self._channel_freq1_text_box.set_value(self.channel_freq1)
        self.analog_sig_source_x_0.set_frequency(self.center_freq - self.channel_freq1)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.osmosdr_source_0.set_center_freq(self.center_freq, 0)
        self.analog_sig_source_x_4.set_frequency(self.center_freq - 105.7e6)
        self.analog_sig_source_x_2.set_frequency(self.center_freq - 97.7e6)
        self.analog_sig_source_x_3.set_frequency(self.center_freq - 103.7e6)
        self.analog_sig_source_x_1.set_frequency(self.center_freq - 101.7e6)
        self.analog_sig_source_x_0.set_frequency(self.center_freq - self.channel_freq1)

    def get_audio_gain1(self):
        return self.audio_gain1

    def set_audio_gain1(self, audio_gain1):
        self.audio_gain1 = audio_gain1
        self._audio_gain1_slider.set_value(self.audio_gain1)
        self._audio_gain1_text_box.set_value(self.audio_gain1)
        self.blocks_multiply_const_vxx_0.set_k((self.audio_gain1, ))

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
    tb = mult_fm()
    tb.Start(True)
    tb.Wait()
