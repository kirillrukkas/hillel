import json
import logging

LOG_FILE = 'login_system.log'

LOCALIZATION_EN = r"work_with_json\localizations_en.json"
LOCALIZATION_RU = r"work_with_json\localizations_ru.json"
LOGIN = r"work_with_json\login.json"
SWAGGER = r"work_with_json\swagger.json"

LIST_OF_JSON_FILES = [LOCALIZATION_EN,
                      LOCALIZATION_RU,
                      LOGIN,
                      SWAGGER
                      ]


def main():
    for file_name in LIST_OF_JSON_FILES:
        with open(file_name, 'r', encoding="utf8") as file:
            try:
                data = json.load(file)                
            except json.decoder.JSONDecodeError as exp:
                print(f"JSON_{file_name.split("\\")[-1].replace(".", "_")}.log")
                print(f"File {file_name} is not correct json file. Error: {exp}")
                logging.basicConfig(
                        filename=f"JSON_{file_name.split("\\")[-1].replace(".", "_")}.log",
                        level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        force=True
                        )
                logger = logging.getLogger("log_event")
                logger.error(f"File {file_name} is not correct json file. Error: {exp}")
                with open(file_name, 'r', encoding="utf8") as file:
                    lines = [line.rstrip() for line in file]
                for line in lines:
                    logger.error(line)



if __name__ == '__main__':
    main()
    print ("All done")



