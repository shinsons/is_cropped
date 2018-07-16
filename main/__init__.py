#!/usr/bin/env python
"""
Determine if one image is a cropped version of another.
"""
import argparse
import os
import sys

import numpy

from cv2 import imread, matchTemplate, minMaxLoc, TM_CCORR_NORMED, Canny


MATCH_THRESHOLD = 0.17

def guess_jpg(fname):
    try:
        f = open(fname, 'rb')
        if ord(f.read(1)) != 255:
            raise SystemExit("'%s' does not appear to be a jpeg file." % fname)
            
    except IOError as e:
       raise SystemExit(unicode(e))


def match(img_path1, img_path2):
    img1_raw = imread(img_path1, 1)
    img2_raw = imread(img_path2, 1)
    img1 = Canny(img1_raw, 100, 300)
    img2 = Canny(img2_raw, 100, 300)
    if img2.size > img1.size:
        res = matchTemplate(img2, img1, TM_CCORR_NORMED)
        img_name = os.path.split(img_path2)[-1]
        tmpl_name = os.path.split(img_path1)[-1]
    else:
        res = matchTemplate(img1, img2, TM_CCORR_NORMED)
        img_name = os.path.split(img_path1)[-1]
        tmpl_name = os.path.split(img_path2)[-1]
    
    if numpy.median(res) > MATCH_THRESHOLD:
        min_val, max_val, min_loc, max_loc = minMaxLoc(res)
        return u"'%s' appears to be cropped from '%s' at %s\n" % (tmpl_name,
                img_name, max_loc)

    else:
        return u"'%s' does not appear to be cropped from '%s'\n" % (tmpl_name,
                img_name)

