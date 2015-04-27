MAKEFLAGS += --no-builtin-rules
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:
.PHONY: clean

all::

clean:
	rm -rf build

include make/gmsl
include make/globals/Makefile
include make/globals/Makefile-OpenFOAM
include make/executables/Makefile
include make/executables/Makefile-OpenFOAM
include make/templates/Makefile-FileSystem
include make/templates/Makefile-OpenFOAM
include make/templates/Makefile-Diagnostics
include make/templates/Makefile-Sample
include make/templates/Makefile-BlockMesh
include make/templates/Makefile-TerrainFollowingMesh
include make/templates/Makefile-CutCellMesh
include make/templates/Makefile-Advection
include make/Makefile-Advection

