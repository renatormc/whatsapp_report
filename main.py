import argparse
import os

from renderer import render


parser = argparse.ArgumentParser()
parser.add_argument("--workkdir", "-w", default=".", help="Work dir")
subparsers = parser.add_subparsers(dest="command", required=True, help='Command to be used')

p_render = subparsers.add_parser("render")
p_render.add_argument("folder")

args = parser.parse_args()
os.chdir(args.workkdir)
if args.command == "render":
    render(args.folder)

