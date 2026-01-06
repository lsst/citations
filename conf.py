# See the documenteer.toml for overrides of the Rubin user guide presets

from documenteer.conf.guide import *  # noqa: F401, F403

# Ignore links that trigger bot protection
linkcheck_ignore = [
    r'https://iopscience\.iop\.org/article/10\.3847/1538-3881/aafece',
]

linkcheck_ignore = [ r'https://zenodo\.org/.*', ]
