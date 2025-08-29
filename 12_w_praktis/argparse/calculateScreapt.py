import argparse
import sys
from datetime import datetime

def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero!")
        return num1 / num2
    else:
        raise ValueError(f"Unknown operation: {operation}")

def read_input_file(file_path):
    operations = []
    with open(file_path, 'r') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):  # skip empty lines or comments
                continue
            try:
                parts = line.split(',')
                if len(parts) != 3:
                    raise ValueError(f"Invalid format: expected 'operation,num1,num2'")
                operation, num1_str, num2_str = [p.strip() for p in parts]
                num1 = float(num1_str)
                num2 = float(num2_str)
                operations.append((num1, num2, operation))
            except Exception as e:
                print(f"Error parsing line {line_num}: {line} -> {e}")
                sys.exit(1)
    return operations

def log_result(message, log_file):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a') as f:
        f.write(f"[{timestamp}] {message}\n")

def main():
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("num1", type=float, nargs='?', help="First number (ignored if --file is used)")
    parser.add_argument("num2", type=float, nargs='?', help="Second number (ignored if --file is used)")
    parser.add_argument("-o", "--operation", help="Operation to perform: add, subtract, multiply, divide")
    parser.add_argument("--file", help="Input file with operations (format: operation,num1,num2)")
    parser.add_argument("--log", help="Log file to save results")

    args = parser.parse_args()

    results = []

    # Check if file is provided
    if args.file:
        operations = read_input_file(args.file)
        for num1, num2, op in operations:
            try:
                result = calculate(num1, num2, op)
                output = f"Result of {op}({num1}, {num2}): {result}"
                print(output)
                results.append(output)
            except Exception as e:
                error_msg = f"Error in {op}({num1}, {num2}): {e}"
                print(error_msg)
                results.append(error_msg)
    else:
        # Use command-line arguments
        if args.operation is None:
            print("Error: --operation is required when --file is not used.")
            sys.exit(1)
        try:
            result = calculate(args.num1, args.num2, args.operation)
            output = f"Result of {args.operation}: {result}"
            print(output)
            results.append(output)
        except Exception as e:
            error_msg = f"Error: {e}"
            print(error_msg)
            results.append(error_msg)

    # Log results if --log is specified
    if args.log:
        for res in results:
            log_result(res, args.log)
        print(f"Results logged to {args.log}")

if __name__ == "__main__":
    main()