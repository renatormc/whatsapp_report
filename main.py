import argparse
import os
import actions as act

parser = argparse.ArgumentParser()
parser.add_argument("--workkdir", "-w", default=".", help="Work dir")
subparsers = parser.add_subparsers(dest="command", required=True, help='Command to be used')

p_render = subparsers.add_parser("render")
p_render.add_argument("folder", default=".")

p_update = subparsers.add_parser("update")

p_code = subparsers.add_parser("code")


args = parser.parse_args()
os.chdir(args.workkdir)
if args.command == "render":
    act.render(args.folder)
elif args.command == "update":
    act.update()
elif args.command == "code":
    act.code()

