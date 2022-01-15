#!/usr/bin/env python3

import psutil

from libqtile.widget import base


class CPU(base.ThreadPoolText):
    """
    A simple widget to display CPU load and frequency.

    Widget requirements: psutil_.

    .. _psutil: https://pypi.org/project/psutil/
    """
    defaults = [
        ("update_interval", 1.0, "Update interval for the CPU widget"),
        (
            "format",
            "CPU {freq_current}GHz {load_percent}%",
            "CPU display format",
        ),
    ]

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(CPU.defaults)

    def poll(self):
        variables = dict()

        variables["load_percent"] = round(psutil.cpu_percent(), 1)
        freq = psutil.cpu_freq()
        variables["freq_current"] = round(freq.current, 1)
        variables["freq_max"] = round(freq.max / 1000, 1)
        variables["freq_min"] = round(freq.min / 1000, 1)

        return self.format.format(**variables)
