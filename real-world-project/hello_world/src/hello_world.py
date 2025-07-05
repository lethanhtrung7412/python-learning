import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Say a cheerful greeting.")
    parser.add_argument("--who", default="World", help="The name of the person to greet.")
    return parser.parse_args()

def greeting(who):
    return f"Hello, {who}!"

def main():
    args = parse_args()
    message = greeting(args.who)
    print(message)

if __name__ == "__main__":
    main()
