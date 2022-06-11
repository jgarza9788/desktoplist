    if path.endswith('Desktop'):
        return ''
    if '.py' in path:
        return ''
    if '.bat' in path:
        return ''
    if path.endswith('.wt.link'):
        return ''
    if path.endswith(' - Shortcut.link'):
        return ''
    if path.endswith('.link'):
        return ''
    if path.endswith('.url'):
        return ''