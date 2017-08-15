#!/bin/bash
set -e

./singularity.ninja.sh $@ build/{schaer,tf}Advect-{btf,cutCell}-1000-{linearUpwind,cubicFit}/10000/{l2,linf}errorT.txt
./singularity.ninja.sh $@ build/schaerAdvect-{btf,cutCell}-1000-linearUpwind/dt.txt
./singularity.ninja.sh $@ build/{schaer,tf}Advect-{btf,cutCell}-1000-{linearUpwind,cubicFit}/s3.uploaded
./singularity.ninja.sh $@ build/{schaer,tf}Advect-{btf,cutCell}-{linearUpwind,cubicFit}-collated/s3.uploaded
