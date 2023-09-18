import argparse
import os

parser = argparse.ArgumentParser()

if os.environ.get('IGNORE_CMD_ARGS_ERRORS', None) is None:
    cmd_opts = parser.parse_args()
else:
    cmd_opts, _ = parser.parse_known_args()


cmd_opts.disable_extension_access = any([cmd_opts.share, cmd_opts.listen, cmd_opts.ngrok, cmd_opts.server_name]) and not cmd_opts.enable_insecure_extension_access
