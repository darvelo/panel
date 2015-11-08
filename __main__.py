#!/usr/bin/env python3

import os
import sys
from libinstall import FileInstaller, PackageInstaller


dir = os.path.dirname(__file__)

if not FileInstaller.has_executable('bspwm'):
    print('Missing bspwm! Exiting...')
    sys.exit(1)
if not FileInstaller.has_executable('sxhkd'):
    print('Missing sxhkd! Exiting...')
    sys.exit(1)

# Debian packages
PackageInstaller.try_install('python3-pyqt5')     # for panel
PackageInstaller.try_install('python3-pyqt5.qtwebkit')     # for panel
PackageInstaller.try_install('python3-psutil')       # CPU usage
PackageInstaller.try_install('python3-xlib') # window titles
PackageInstaller.try_install('suckless-tools')            # program executor
PackageInstaller.try_install('feh')              # wallpaper renderer

# Pip packages
PackageInstaller.try_install('pyalsaaudio', method='pip')  # system volume
PackageInstaller.try_install('python-mpd2', method='pip')  # mpd interaction
# PackageInstaller.try_install('psutil', method='pip')       # CPU usage
# PackageInstaller.try_install('python3-xlib', method='pip') # window titles

# Files to link
# FileInstaller.create_symlink(os.path.join(dir, 'sxhkdrc'), '~/.config/sxhkd/sxhkdrc')
# FileInstaller.create_symlink(os.path.join(dir, 'bspwmrc'), '~/.config/bspwm/bspwmrc')
# FileInstaller.create_symlink(os.path.join(dir, 'toggle-fullscreen'), '~/.config/bspwm/toggle-fullscreen')
# FileInstaller.create_symlink(os.path.join(dir, 'rules'), '~/.config/bspwm/rules')
# FileInstaller.create_symlink(os.path.join(dir, 'panel'), '~/.config/bspwm/panel')
