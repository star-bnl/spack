# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Genfit(CMakePackage):
    """GenFit is an experiment-independent framework for track reconstruction in
        particle and nuclear physics"""

    homepage = "https://github.com/GenFit/"
    url      = "https://github.com/GenFit/GenFit/archive/master.tar.gz"

    version('master', branch='master')
    version('496504a', sha256='458bf2bb908b27621c331edcfb59bbc4a34714bff6200daf89f875f7eb117265')

    depends_on('root')
    depends_on('eigen')

    conflicts('root@6.18.00:', when='@496504a')
