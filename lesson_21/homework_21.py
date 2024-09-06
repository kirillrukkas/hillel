from datetime import datetime

def analyze_log(input_file, output_file, key):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    previous_timestamp = None

    filtered_log = []
    for line in lines:
        if key in line:
            filtered_log.append(line)

    filtered_log.reverse()

    with open(output_file, 'w') as log_file:
        for line in filtered_log:
            current_timestamp = datetime.strptime(line.split()[10], "%H:%M:%S")
            if previous_timestamp:
                heartbeat = (current_timestamp - previous_timestamp).total_seconds()
                if 31 < heartbeat < 33:
                    log_file.write(f'WARNING: Heartbeat is {heartbeat} seconds at {current_timestamp.time()}\n')
                elif heartbeat >= 33:
                    log_file.write(f'ERROR: Heartbeat is {heartbeat} seconds at {current_timestamp.time()}\n')
            previous_timestamp = current_timestamp

# Виклик функції
analyze_log(
    "lesson_21/hblog.txt", "lesson_21/hb_test.logs", "TSTFEED0300|7E3E|0400"
)
