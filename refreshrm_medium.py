
import os
# import sys
from functions import *

DIR = os.path.dirname(os.path.realpath(__file__))

rainmeter = """

[Rainmeter]
Update=1000
AccurateText=1
DynamicWindowSize=1
blur=1

"""

variables = """

[variables]
RECSHAPE = 50,50,600,75,10
;NORMALCOLOR = 31,31,31,225
NORMALCOLOR = 0,0,0,200
HOVERCOLOR = 66, 156, 227,255
;HOVERCOLOR = 43, 103, 150,255
ICONCOLOR = 255,255,255,255
ICONHOVERCOLOR = 255,255,255,255
TEXTCOLOR = 255,255,255,255
TEXTHOVERCOLOR = 255,255,255,255

"""

metershape = """

[MeterShapes{index}]
Meter=Shape
Shape=Rectangle #RECSHAPE# | Fill Color #NORMALCOLOR# | StrokeWidth 0
;MouseOverAction=[!SetOption MeterShapes{index} Shape "Rectangle #RECSHAPE# | Fill Color {HOVERCOLOR} | StrokeWidth 0"][!SetOption MeterIcon{index} FontColor #ICONHOVERCOLOR#][!SetOption MeterText{index} FontColor #TEXTHOVERCOLOR#][!UpdateMeter MeterShapes{index}][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
;MouseLeaveAction=[!SetOption MeterShapes{index} Shape "Rectangle #RECSHAPE# | Fill Color #NORMALCOLOR# | StrokeWidth 0"][!SetOption MeterIcon{index} FontColor #ICONCOLOR#][!SetOption MeterText{index} FontColor #TEXTCOLOR#][!UpdateMeter MeterShapes{index}][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
MouseOverAction=[!SetOption MeterIcon{index} FontColor {HOVERCOLOR}][!SetOption MeterText{index} FontColor {HOVERCOLOR}][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
MouseLeaveAction=[!SetOption MeterIcon{index} FontColor #ICONCOLOR#][!SetOption MeterText{index} FontColor #TEXTCOLOR#][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
LeftMouseUpAction=["{path}"]
Y={Y}


"""
# ;MouseOverAction=[!SetOption MeterText Text "{icon0} {text}"][!SetOption MeterShapes Shape "Rectangle 50,50,500,100,10 | Fill Color #RED# | StrokeWidth 0"][!UpdateMeter MeterText][!UpdateMeter MeterShapes][!Redraw]
# ;MouseLeaveAction=[!SetOption MeterText Text "{icon1} {text}"][!SetOption MeterShapes Shape "Rectangle 50,50,500,100,10 | Fill Color #WHITE# | StrokeWidth 0"][!UpdateMeter MeterText][!UpdateMeter MeterShapes][!Redraw]


metericon = """

[MeterIcon{index}]
Meter=String
FontFace=Hack NF
FontSize=48
FontColor=#ICONCOLOR#
SolidColor=47,47,47,0
;Padding=32,32,32,32
AntiAlias=1
Y={Y}
X={X}
Text="{icon}"

"""


metertext = """

[MeterText{index}]
Meter=String
FontFace=Hack NF
;FontFace=Comic Sans MS
FontSize=24
FontColor=#TEXTCOLOR#
SolidColor=47,47,47,0
;Padding=32,32,32,32
AntiAlias=1
Y={Y}
X={X}
Text="{text}"

"""
# ;FontFace=Comic Sans MS
#FontFace=Hack NF


yshift = 100
ytextshift = 70
yiconshift = 50
xtextshift= 125
xiconshift=70

# regex patters that map to nerd font icons
icon_map_00 = {
    # 'Desktop$':'\uf108 - desktop',
    # '\.py':'\ue235 - python',
    # '\.bat':'\ue795 - bat',
    # '\.wt(\.|)':'\ue795 - winterminal',
    # '\.url$':'\uf465 - url',
    # ' - Shortcut\.lnk':'\uf482 - folderlink',
    'Desktop$':'\uf108',
    '\.py':'\ue235',
    '\.bat':'\ue795',
    '\.wt(\.|)':'\ue795',
    '\.vbs(\.|)':'\uf481',
    '\.url$':'\uf465',
    ' - Shortcut\.lnk':'\uf482',
    '\.txt':'\uf15c',
}

# COLORS = [
#             "244, 0, 95,255",
#             "152, 224, 36,255",
#             "250, 132, 25,255",
#             "157, 101, 255,255",
#             "88, 209, 235,255"
#         ]

# COLORS = ["66, 156, 227,255"]
COLORS = [
    "102,217,239,255",
    "166,226,46,255",
    "249,38,114,255",
    "253,151,31,255",
    "174,129,255,255"
    ]


def main():
    # save(test.format(v='hello'),os.path.join(DIR,'hello.ini'))
    # pass
    rm = rainmeter
    rm += variables

    files = get_files(r'C:\Users\JGarza\Desktop',add_root=True,exclude_pattern='^(__|@|\.)')
    # files = get_files(r'C:\Users\JGarza',add_root=True,exclude_pattern='^(__|@|\.)')
    print(*files,sep='\n')

    for index,f in enumerate(files):

        Y = yshift*index

        shape = metershape
        shape = shape.format(index=index,path=f,Y=Y,HOVERCOLOR=COLORS[index % len(COLORS)])



        icon = metericon
        icon = icon.format(index=index,Y=(Y+yiconshift),X=xiconshift,icon=get_icon(f,icon_map_00))

        text = metertext
        text = text.format(index=index,Y=(Y+ytextshift),X=xtextshift,text=get_text(f,25))

        rm += shape
        rm += icon
        rm += text


    
    save(rm,os.path.join(DIR,'desktoplist_medium.ini'))



if __name__ == "__main__":
    main()
