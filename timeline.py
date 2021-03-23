"""
    Third example on:
    https://kristw.github.io/d3kit-timeline/
"""

from datetime import date

from labella.timeline import TimelineSVG, TimelineTex
from labella.utils import COLOR_10


def main():
    items = [
        {
            "time": date(2021, 4, 12),
            "text": "Online class upto: 12, 4",
        },
        {
        	"time": date(2021, 4, 14),
        	"text": "Thesis pre-defence: April 14"
        },
        {
        	"time": date(2021, 5, 20),
        	"text": "Thesis final defence: May 20"
        },
        {
        	"time": date(2021, 3, 25),
        	"text": "CIP application due"
        },
        {
        	"time": date(2021, 4, 19),
        	"text": "CIP class start",
        	"episode":1
        },
        {
        	"time": date(2021, 5, 21),
        	"text": "CIP class end",
        	"episode": 1
        },
        {
        	"time": date(2021, 5, 13),
        	"text": "EID"
        },
        {
        	"time": date(2021, 3, 23),
        	"text": "today"
        },
        {
        	"time": date(2021, 3, 22),
        	"text": "DM Lab viva"
        },
        {
        	"time": date(2021, 3, 14),
        	"text": "DM Lab 3"
        },
    ]

    options = {
        "initialWidth": 804,
        "initialHeight": 160,
        "direction": "down",
        "dotColor": COLOR_10,
        "labelBgColor": COLOR_10,
        "linkColor": COLOR_10,
        "textFn": None,
        "labelPadding": {"left": 0, "right": 0, "top": 1, "bottom": 1},
        "margin": {"left": 20, "right": 20, "top": 30, "bottom": 20},
        "layerGap": 40,
        "labella": {
            "maxPos": 800,
        },
        "latex": {"reproducible": True}
    }

    tl = TimelineSVG(items, options=options)
    tl.export("timeline_kit_3.svg")

    tl = TimelineTex(items, options=options)
    tl.export("timeline_kit_3.tex")


if __name__ == "__main__":
    main()
