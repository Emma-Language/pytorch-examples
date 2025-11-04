import os
import sys

def main():
    data_dir = os.environ.get("DATA_DIRECTORY")
    if not data_dir:
        print("ERROR: DATA_DIRECTORY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    if not os.path.isdir(data_dir):
        print(f"ERROR: DATA_DIRECTORY is not a directory or is not accessible: {data_dir}", file=sys.stderr)
        sys.exit(1)

    def onerror(err):
        # Print permission or traversal errors to stderr but keep going
        print(f"WARNING: {err}", file=sys.stderr)

    for root, dirs, files in os.walk(data_dir, topdown=True, followlinks=False, onerror=onerror):
        for name in files:
            print(os.path.join(root, name))

if __name__ == "__main__":
    main()
