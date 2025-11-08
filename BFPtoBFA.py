import sys
import os

BYTE_TABLE = {
    "INC": 0x00,
    "DEC": 0x01,
    "PRT": 0x02,
    "ICI": 0x03,
    "DCI": 0x04,
    "ENL": 0x05,
    "EXL": 0x06,
    "ENF": 0x07,
    "EXF": 0x08,
    "RNF": 0x09,
    "TUI": 0x0A
}

def convert_bfp_to_bfa(input_path):
    base_name = os.path.splitext(input_path)[0]
    output_path = base_name + ".BFA"

    output_bytes = []

    with open(input_path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1):
            parts = line.strip().split()
            if not parts:
                continue

            instruction = parts[0].upper()

            if instruction in BYTE_TABLE:
                output_bytes.append(BYTE_TABLE[instruction])
                if len(parts) > 1 and parts[1].startswith('$'):
                    try:
                        num = int(parts[1][1:], 16)
                        output_bytes.append(num)
                    except ValueError:
                        print(f"Line {line_num}: Invalid number format '{parts[1]}'")
            elif instruction.startswith('$'):
                try:
                    num = int(instruction[1:], 16)
                    output_bytes.append(num)
                except ValueError:
                    print(f"Line {line_num}: Invalid number format '{instruction}'")
            else:
                print(f"Line {line_num}: Unknown instruction '{instruction}'")

    with open(output_path, 'wb') as f_out:
        f_out.write(bytes(output_bytes))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(0)
    else:
        for file_path in sys.argv[1:]:
            convert_bfp_to_bfa(file_path)

