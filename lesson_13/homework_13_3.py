import xml.etree.ElementTree as ET
import logging

GROUPS = r"work_with_xml\groups.xml"

INCOMMING ="incoming" 

def main():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    
    # Завантаження XML-файлу
    tree = ET.parse(GROUPS)
    root = tree.getroot()

   # Пошук елементу incoming у timingExbytes для кожної групи
    for group in root.findall('group'):
        timing_exbytes = group.find('timingExbytes')
        if timing_exbytes is not None:
            incoming = timing_exbytes.find(INCOMMING)
            if incoming is not None:
                logging.info("Group: %s, %s: %s", group.find('name').text, INCOMMING, incoming.text)
            else:
                logging.error("Group: %s, %s: %s", group.find('name').text, INCOMMING, "Не знайдено")



if __name__ == '__main__':
    main()
    print ("All done")



