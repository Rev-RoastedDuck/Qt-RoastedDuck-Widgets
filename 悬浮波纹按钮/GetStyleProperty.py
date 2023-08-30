from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget

def get_property(widget: QWidget) -> dict:
    style_sheet = widget.styleSheet().replace("\t", "").replace("\n", "")
    style_sheet_dict = {}
    for obejct_style in style_sheet.split("}"):
        if not obejct_style.strip():
            continue
        object_name, content = obejct_style.split("{")
        object_name = object_name.strip()
        content_dict = {prop.split(":")[0].strip(): prop.split(":")[1].strip() for prop in content.split(";") if prop.strip()}
        style_sheet_dict[object_name] = content_dict
    return style_sheet_dict

def transfer_type(s:str,to:str):
    match to:
        case "color":
            return str_to_qcolor(s)
        case "pixel":
            return str_to_pixel(s)

def str_to_qcolor(s:str):
    if "rgb" in s:
        return QColor(*[int(v) for v in s.replace("rgb(", "").replace(")", "").split(",")])
    elif "rgba" in s:
        return QColor(*[int(v) for v in s.replace("rgba(", "").replace(")", "").split(",")])
    elif "#" in s:
        return QColor(s)
    else:
        return QColor(s)

def str_to_pixel(s:str):
    return int(s.replace("px","").replace(" ",""))






