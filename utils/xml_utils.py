import logging
from lxml import etree

# Настройка логирования
logger = logging.getLogger('uvicorn.error')

def modify_uri(response_content: bytes) -> bytes:
    """
    Функция для модификации URI в ответе ONVIF.
    Добавляет порт 554 к URI, если он отсутствует.
    """
    resp = response_content
    try:
        root = etree.fromstring(response_content)
        namespaces = {'tr2': "http://www.onvif.org/ver20/media/wsdl"}
        uri_element = root.find(".//tr2:Uri", namespaces)

        if uri_element is not None and uri_element.text:
            parts = uri_element.text.split('/')
            logger.debug(f"URI parts before modification: {parts}")
            if len(parts) > 2 and ':' not in parts[2]:
                parts[2] = f"{parts[2]}:554"
                uri_element.text = '/'.join(parts)
            resp = etree.tostring(root,
                                  pretty_print=False,
                                  xml_declaration=True,
                                  encoding="utf-8")
    except etree.XMLSyntaxError as parse_error:
        logger.error(f"Parse failed XML с lxml: {parse_error}")
    except Exception as e:
        logger.error(f"Parse failed: {e}")
    return resp

def extract_pantilt_values(response_content: bytes) -> dict[str, str]:
    """
    Извлекает координаты Pan/Tilt из XML-ответа.
    Возвращает словарь с координатами x, y и статусом PanTilt.
    """
    attributes = {'x': '0', 'y': '0', 'PanTilt': "Stop"}
    try:
        root = etree.fromstring(response_content)
        namespaces = {
            's': "http://www.w3.org/2003/05/soap-envelope",
            'ptz': "http://www.onvif.org/ver20/ptz/wsdl",
            'schema': "http://www.onvif.org/ver10/schema"
        }

        pantilt_elements = root.findall(".//schema:PanTilt", namespaces)
        # Найденные координаты команд PTZ (например, движение влево и т.д.)
        for elem in pantilt_elements:
            if elem is not None:
                attributes['x'] = elem.attrib.get('x')
                attributes['y'] = elem.attrib.get('y')
                attributes['PanTilt'] = "Start"
                logger.debug(f"Found PanTilt: x={attributes['x']}, y={attributes['y']}")
    except etree.XMLSyntaxError as parse_error:
        logger.error(f"Parse failed XML с lxml: {parse_error}")
    except Exception as e:
        logger.error(f"Parse failed: {e}")
    return attributes
