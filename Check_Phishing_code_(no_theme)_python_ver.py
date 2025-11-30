import re
Fish = r"""
⠀⠀⢀⣠⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⡼⠋⠁⣠⣄⡀⠈⢹⡗⢦⣤⠶⠛⢳⡄⠀⠀⠀⠀⠀⠀
⢸⠁⠀⠘⣧⣨⠇⠀⣸⠁⠀⠈⠳⣄⠀⠹⡆⠀⠀⠀⠀⠀
⢸⡓⠶⠆⠀⠀⠀⣰⠋⠀⢀⡿⠀⠘⢧⡀⠹⣆⠀⠀⠀⠀
⠘⣧⣀⣀⣠⡴⠞⠁⠀⠙⠉⠀⠀⡆⠈⢧⠀⢙⡆⠀⠀⠀
⠀⠘⣏⠁⠀⠀⢀⡿⠀⠀⠀⠒⠚⠁⠀⢸⡟⠋⠀⠀⠀⠀
⠀⠀⠙⣦⠀⠐⠚⠃⠀⢰⡆⠀⠀⣴⠀⠈⣧⣀⠀⠀⠀⠀
⠀⠀⠀⠈⠳⢦⣀⠐⠛⠋⠀⠐⠒⠋⠀⢀⡀⠉⠙⠓⢲⡄
⠀⠀⠀⠀⠀⠀⠉⠓⠶⠤⣤⣤⡀⠀⢤⠈⠙⠓⠀⠀⣠⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠈⠓⠀⣠⠖⠋⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⣰⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠚⠁⠀⠀⠀⠀⠀"""
def check_phishing(url):
    if len(url) > 75:
        return f" Warning: The URL is too long and may be a phishing attempt!𓆝 ⋆.\n{Fish}"    
    if re.search(r'http://', url):
        return f" Warning: The URL is not secure and may be a phishing attempt!.𖦹˚ 𓆝 ｡𖦹°‧\n{Fish}"
    if re.search(r'@', url):
        return f" Warning: The URL may be a phishing URLs!⋆⭒𓆟⋆｡˚𖦹𓆜✩⋆\n{Fish}"
    if re.search(r'//.+//', url):
        return f" Warning: The URL may be a phishing attempt!𓆝 ⋆.𓆟⋆\n{Fish}"
    if re.search(r'\.(tk|ml|cf|ga|gq)', url):
        return f" Warning: The URL may be a phishing URLs!⋆⭒𓆟⋆｡˚𖦹𓆜✩⋆\n{Fish}"
    else:
        return " The URL appears to be safe. 😌☕️🧸"