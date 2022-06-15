import os
import re

DIR = os.path.dirname(os.path.realpath(__file__))

def save(contents, file_path):
    """saves the rainmeter .ini file

    Args:
        text (str): contents of the file
        file_path (str): location to save the file
    """
    with open(file_path,'w',encoding="utf-16") as f:
        f.write(contents)

def get_files(root,add_root = False,exclude_pattern=''):
    """gets the files from the desktop

    Args:
        root (str): the directory root
        add_root (str): weather to add root to list

    Returns:
        list: list of files
    """
    result = []

    if add_root:
        result.append(root)
    
    for i in os.listdir(root):
        if i.startswith('~') or i.endswith('.ini') or i.endswith('.tmp'):
            pass
        elif re.match(pattern=exclude_pattern,string=i):
            pass
        else:
            result.append(os.path.join(root,i))

    # result.insert(0,root)
    return result

# https://docs.rainmeter.net/tips/launching-windows-special-folders/
def get_recycle_bin_link():
    return '::{645FF040-5081-101B-9F08-00AA002F954E}'

def get_run_refresh(file):
    return 'python ' + file

def get_icon(path,icon_map):
    """returns an unicode icon from nerd fronts

    Args:
        path (str): the path of the file

    Returns:
        str: a unicode icon
    """
    result = '\ue5ff' #folder

    print(path)

    for pi in icon_map:
        if re.search(pi,path):
            result = icon_map[pi]
            break;

    return result 

    # if path.endswith('Desktop'):
    #     return '\uf108'
    # if '.py' in path:
    #     return '\ue235'
    # if '.bat' in path:
    #     return '\ue795'
    # if path.endswith('.wt.lnk'):
    #     return '\ue795'
    # if path.endswith(' - Shortcut.lnk'):
    #     return '\uf482'
    # if path.endswith('.lnk'):
    #     return '\uf481'
    # if path.endswith('.url'):
    #     return '\uf465'
    
    # return '\ue5ff'


def get_text(path,max_chars=35):
    """gets text from the path

    Args:
        path (str): the path of a while

    Returns:
        str: a small string that describes the file
    """
    result = path.split('\\')[-1]
    result = result.replace(" - Shortcut.lnk", "")
    result = result.replace(".lnk", "")
    return result[:max_chars]

if __name__ == '__main__':


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

    #testing get icon
    for f in get_files(r'C:\Users\JGarza\Desktop',add_root=True):
        print(get_icon(f,icon_map_00))