#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

# Grant user exec permissions on manage.py
subprocess.call(['chmod', 'u+x', 'manage.py'])

# Start git repository for project
subprocess.call(['git', 'init'])

# Save initial commit
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m"Initial commit"'])
