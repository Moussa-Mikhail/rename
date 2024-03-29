import os
import re

dirpath = os.getcwd()


def main():

    # There might be a problem with not using raw strings here
    # but for now this will do.
    match = input("Match:").strip()

    repl = input("Replacement:").strip()

    for filename in os.listdir(dirpath):

        new_filename = re.sub(match, repl, filename)

        src = f"{dirpath}/{filename}"

        dst = f"{dirpath}/{new_filename}"

        if src != dst:
            os.rename(src, dst)


if __name__ == "__main__":
    main()
