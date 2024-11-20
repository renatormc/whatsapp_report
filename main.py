import argparse

from renderer import render


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", required=True, help='Command to be used')

p_render = subparsers.add_parser("render")
p_render.add_argument("folder")

args = parser.parse_args()
if args.command == "render":
    render(args.folder)

