# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from distutils import version


__version__ = '1.0.0'
version_info = version.StrictVersion(__version__).version

default_app_config = 'debreach.apps.DebreachConfig'
