# -*- coding: utf-8 -*-
"""Module ga4gh.drs.cli.methods.schemes.py
Contains main entrypoint method(s) for the 'schemes' command group
"""

import ga4gh.drs.config.globals as gl

def ls(**kwargs):
    """List all supported URI schemes for DRS object download

    Arguments:
        kwargs (dict): command-line arguments parsed via Click package
    """

    template = "{key}{spacer}\t{desc}"

    acc_dict = gl.ACCESS_METHOD_TYPES_DESC.copy()
    keys = sorted(acc_dict.keys())
    acc_dict.update({"Scheme": "Description"})
    keys.insert(0, "Scheme")
    maxlen = max([len(a) for a in keys])

    for key in keys:
        spacer = " " * (maxlen - len(key))
        desc = acc_dict[key]
        output_string = template.format(key=key, spacer=spacer, desc=desc)
        print(output_string)
