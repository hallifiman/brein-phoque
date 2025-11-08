import os
import sys

def translate_bfa_file(file_path: str, output_path: str = None):

    OPCODES = {
        0x07: "ENF",
        0x08: "EXF",
        0x00: "INC",
        0x01: "DEC",
        0x02: "PRT",
        0x03: "ICI",
        0x04: "DCI",
        0x05: "ENL",
        0x06: "EXL",
        0x09: "RNF",
        0x0A: "TUI",
    }

    print(f"Reading file: {file_path}")
    try:
        with open(file_path, "rb") as f:
            data = f.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    i = 0
    functions = {}
    main_code = []
    while i < len(data):
        instr = data[i]
        i += 1

        if instr not in OPCODES:
            print(f"Warning: Unknown opcode {instr:#04x} at position {i-1}, skipping.")
            continue

        op_name = OPCODES[instr]
        operand = None

        if op_name in ["INC", "DEC", "ICI", "DCI", "RNF", "ENF"]:
            if i >= len(data):
                print(f"Error: Missing operand for {op_name}")
                return
            operand = data[i]
            i += 1

        if op_name == "ENF":
            func_id = operand
            func_body = []
            while i < len(data):
                inner_instr = data[i]
                i += 1
                if inner_instr == 0x08:
                    break
                inner_op_name = OPCODES.get(inner_instr)
                inner_operand = None
                if inner_op_name in ["INC", "DEC", "ICI", "DCI", "RNF", "ENF"]:
                    if i >= len(data):
                        print(f"Error: Missing operand inside function {func_id}")
                        return
                    inner_operand = data[i]
                    i += 1
                func_body.append((inner_instr, inner_operand))
            functions[func_id] = func_body
            print(f"Defined function {func_id}")
        else:
            main_code.append((instr, operand))

    def translate(instructions):
        output = []
        for instr, operand in instructions:
            op_name = OPCODES[instr]

            if op_name == "INC":
                output.append("+" * operand)
            elif op_name == "DEC":
                output.append("-" * operand)
            elif op_name == "PRT":
                output.append(".")
            elif op_name == "ICI":
                output.append(">" * operand)
            elif op_name == "DCI":
                output.append("<" * operand)
            elif op_name == "ENL":
                output.append("[")
            elif op_name == "EXL":
                output.append("]")
            elif op_name == "TUI":
                output.append(",")
            elif op_name == "RNF":
                func_id = operand
                if func_id in functions:
                    output.append(translate(functions[func_id]))
        return "".join(output)

    print("Translating...")
    translated_code = translate(main_code)

    if output_path is None:
        base, _ = os.path.splitext(file_path)
        output_path = base + ".BF"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(translated_code)

    print(f"Translation complete.\nOutput written to: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(0)
    if not sys.argv[1].lower().endswith(".bfa"):
        print("Error: Please provide a .BFA file.")
        sys.exit(1)
    translate_bfa_file(sys.argv[1])