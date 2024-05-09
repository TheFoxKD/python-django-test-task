import os.path

from jinja2 import Environment, FileSystemLoader

from .settings.base import BASE_DIR


def environment(**options):
    env = Environment(**options)
    env.autoescape = True
    env.newline_sequence = '\n'
    env.loader = FileSystemLoader(os.path.join(BASE_DIR, 'jinja2_templates'))
    # env.bytecode_cache = MemcachedBytecodeCache()
    return env
