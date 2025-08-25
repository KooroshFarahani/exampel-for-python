import argparse

def PowerNumber():
    try:
        parser = argparse.ArgumentParser(description="Calculate power of a number")
        
        # Positional arguments
        parser.add_argument("base", type=float, help="Base number")
        parser.add_argument("exponent", type=float, help="Exponent number")
        
        # Optional arguments
        parser.add_argument("-v", "--verbose", action="store_true", help="Show verbose output")
        parser.add_argument("-r", "--round", type=int, help="Number of decimal places", default=None)  # None means no rounding

        args = parser.parse_args()

        result = args.base ** args.exponent

        # Apply rounding if specified
        if args.round is not None:
            result = round(result, args.round)

        if args.verbose:
            print(f"Calculating {args.base} raised to the power of {args.exponent}...")
            print(f"Result: {result}")
        else:
            print(f"Result: {result}")

    except Exception as e:
        print("Your input is not valid:", e)

PowerNumber()