
import os
# import sys
from functions import *

DIR = os.path.dirname(os.path.realpath(__file__))

rainmeter = """

[Rainmeter]
Update=1000
AccurateText=1
DynamicWindowSize=1

"""

variables = """

[variables]
RECSHAPE = 50,50,400,50,10
NORMALCOLOR = 0,0,0,190
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
MouseOverAction=[!SetOption MeterShapes{index} Shape "Rectangle #RECSHAPE# | Fill Color #HOVERCOLOR# | StrokeWidth 0"][!SetOption MeterIcon{index} FontColor #ICONHOVERCOLOR#][!SetOption MeterText{index} FontColor #TEXTHOVERCOLOR#][!UpdateMeter MeterShapes{index}][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
MouseLeaveAction=[!SetOption MeterShapes{index} Shape "Rectangle #RECSHAPE# | Fill Color #NORMALCOLOR# | StrokeWidth 0"][!SetOption MeterIcon{index} FontColor #ICONCOLOR#][!SetOption MeterText{index} FontColor #TEXTCOLOR#][!UpdateMeter MeterShapes{index}][!UpdateMeter MeterIcon{index}][!UpdateMeter MeterText{index}][!Redraw]
LeftMouseUpAction=["{path}"]
Y={Y}

"""
# ;MouseOverAction=[!SetOption MeterText Text "{icon0} {text}"][!SetOption MeterShapes Shape "Rectangle 50,50,500,100,10 | Fill Color #RED# | StrokeWidth 0"][!UpdateMeter MeterText][!UpdateMeter MeterShapes][!Redraw]
# ;MouseLeaveAction=[!SetOption MeterText Text "{icon1} {text}"][!SetOption MeterShapes Shape "Rectangle 50,50,500,100,10 | Fill Color #WHITE# | StrokeWidth 0"][!UpdateMeter MeterText][!UpdateMeter MeterShapes][!Redraw]


metericon = """

[MeterIcon{index}]
Meter=String
FontFace=Hack NF
FontSize=24
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
FontSize=12
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


yshift = 60
ytextshift = 65
yiconshift = 55
xtextshift=95
xiconshift=60

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

def main():
    # save(test.format(v='hello'),os.path.join(DIR,'hello.ini'))
    # pass
    rm = rainmeter
    rm += variables

    files = get_files(r'C:\Users\JGarza\Desktop',add_root=True)
    print(*files,sep='\n')

    for index,f in enumerate(files):

        Y = yshift*index

        shape = metershape
        shape = shape.format(index=index,path=f,Y=Y)

        icon = metericon
        icon = icon.format(index=index,Y=(Y+yiconshift),X=xiconshift,icon=get_icon(f,icon_map_00))

        text = metertext
        text = text.format(index=index,Y=(Y+ytextshift),X=xtextshift,text=get_text(f))

        rm += shape
        rm += icon
        rm += text
    
    save(rm,os.path.join(DIR,'desktoplist_small.ini'))



if __name__ == "__main__":
    main()
