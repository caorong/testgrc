#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Mult Fm Nogui
# Generated: Tue Nov 11 19:09:54 2014
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr

class mult_fm_noGUI(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Mult Fm Nogui")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 8e6
        self.channel_width = channel_width = 200e3
        self.center_freq = center_freq = 97.9e6

        ##################################################
        # Blocks
        ##################################################
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
        self.blocks_udp_sink_0_0 = blocks.udp_sink(gr.sizeof_short*1, "192.168.3.131", 5006, 1472, True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_short*1, "0.0.0.0", 5005, 1472, True)
        self.blocks_multiply_xx_0_0_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_float_to_short_0_3 = blocks.float_to_short(1, 32767)
        self.blocks_float_to_short_0_2 = blocks.float_to_short(1, 32767)
        self.blocks_float_to_short_0_1 = blocks.float_to_short(1, 32767)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 32767)
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 32767)
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
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - 94.0, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0_0, 0))
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
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.analog_wfm_rcv_0_0, 0))



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
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)

    def get_channel_width(self):
        return self.channel_width

    def set_channel_width(self, channel_width):
        self.channel_width = channel_width

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.osmosdr_source_0.set_center_freq(self.center_freq, 0)
        self.analog_sig_source_x_4.set_frequency(self.center_freq - 105.7e6)
        self.analog_sig_source_x_2.set_frequency(self.center_freq - 97.7e6)
        self.analog_sig_source_x_3.set_frequency(self.center_freq - 103.7e6)
        self.analog_sig_source_x_0.set_frequency(self.center_freq - 94.0)
        self.analog_sig_source_x_1.set_frequency(self.center_freq - 101.7e6)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = mult_fm_noGUI()
    tb.start()
    raw_input('Press Enter to quit: ')
    tb.stop()
    tb.wait()
