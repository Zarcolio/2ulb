#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import subprocess

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile", help="Input file")
    parser.add_argument("-f", "--force", action="store_true",
                        help="Force symlink creation")
    args = parser.parse_args()

    if os.geteuid() != 0:
        print("You need to have root privileges to run this script.")
        print("Please try again using the sudo command.")
        return

    scriptname = os.path.splitext(os.path.basename(args.inputfile))[0]
    scriptfullpath = os.path.abspath(args.inputfile)
    symlink_path = f"/usr/local/bin/{scriptname}"

    if os.path.exists(symlink_path):
        if args.force:
            os.remove(symlink_path)
        else:
            response = input(f"Symlink already exists: {symlink_path}. Do you want to overwrite it? (y/n): ")
            if response.lower() == "y":
                args.force = True
            else:
                print("Operation canceled.")
                return

    chmodcmd = f"chmod +x \"{scriptfullpath}\""
    subprocess.run(chmodcmd, shell=True, check=True)

    lncmd = f"ln {'-f' if args.force else ''} -s \"{scriptfullpath}\" \"{symlink_path}\""
    subprocess.run(lncmd, shell=True, check=True)

if __name__ == "__main__":
    main()
