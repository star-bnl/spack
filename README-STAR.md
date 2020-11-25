# Bootstrap by installing gcc@4.8.5 first

    git clone --branch v0.16-star-1 git@github.com:star-bnl/spack.git
    source spack/share/spack/setup-env.sh
    spack install gcc@4.8.5 target=x86_64
    SPGCC=$(spack location --install-dir gcc); cat share/spack/templates/compilers.yaml | sed -e "s|@SPACK_PATH_TO_GCC@|${SPGCC}|g" > ~/.spack/linux/compilers.yaml


# Install packages

Install root@6.16.00 with table, vc, tmva, ... and without vmc as it will be installed
as standalone package by geant4-vmc

    spack install root@6.16.00+vc+table+pythia6+mysql+tmva~vmc+mlp+fftw+vdt+veccore+roofit%gcc@4.8.5 target=x86_64 ^ftgl%gcc@4.8.5 target=x86_64 ^mesa~llvm swr=none %gcc@4.8.5 target=x86_64

Install Geant4

    spack install geant4@10.4.0 %gcc@4.8.5 target=x86_64
    # Geant4 @10.3.3 does not work with currently available versions of geant4-vmc
    # spack install geant4@10.3.3 %gcc@4.8.5 target=x86_64

Install Geant4-vmc. 3fbnfbw represent the spec of ROOT as installed above

    spack install geant4-vmc@4-0-p3 %gcc@4.8.5 target=x86_64 ^/3fbnfbw ^geant4@10.4.0 %gcc@4.8.5 target=x86_64


# Expose installed packages in a spack view

    spack view -v --dependencies=no hardlink spack-view root geant4 geant4-vmc
