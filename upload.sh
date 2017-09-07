#!/bin/bash
set -e

./singularity.ninja.sh $@ build/{schaer,tf}Advect-{btf,cutCell}-1000-{linearUpwind,cubicFit}/10000/{l2,linf}errorT.txt
./singularity.ninja.sh $@ build/{schaer,tf}Advect-{btf,cutCell}-1000-linearUpwind/dt.txt
./singularity.ninja.sh $@ build/{schaer,tf}Advect-{btf,cutCell}-1000-{linearUpwind,cubicFit}/s3.uploaded
./singularity.ninja.sh $@ build/{schaer,tf}Advect-{btf,cutCell}-{linearUpwind,cubicFit}-collated/s3.uploaded

#./singularity.ninja.sh $@ build/deformationSphere-gaussians-{hex,cubedSphere}-{linearUpwind,cubicFit}-collated/s3.uploaded
#./singularity.ninja.sh $@ build/deformationSphere-gaussians-hex-8-cubicFit/s3.uploaded

./singularity.ninja.sh $@ build/mountainAdvect-h0-{btf,cutCell,slantedCell}-1000-{linearUpwind,cubicFit}-collated/10000/l2errorT.txt
./singularity.ninja.sh $@ build/mountainAdvect-h0-{btf,cutCell,slantedCell}-1000-5000m-{linearUpwind,cubicFit}/10000/l{2,inf}errorT.txt
./singularity.ninja.sh $@ build/mountainAdvect-h0-{btf,cutCell,slantedCell}-1000-{0,3000,4000,5000,6000}m-linearUpwind/dt.txt
./singularity.ninja.sh $@ build/mountainAdvect-h0-slantedCell-1000-6000m-linearUpwind/co.txt
./singularity.ninja.sh $@ build/mountainAdvect-maxdt-{btf,cutCell,slantedCell}-6000m-cubicFit-collated/{dt,co}.txt

./singularity.ninja.sh $@ build/mountainAdvect-h0-{btf,cutCell,slantedCell}-1000-{linearUpwind,cubicFit}-collated/s3.uploaded
./singularity.ninja.sh $@ build/mountainAdvect-h0-{btf,cutCell,slantedCell}-1000-5000m-{linearUpwind,cubicFit}/s3.uploaded
./singularity.ninja.sh $@ build/mountainAdvect-h0-{btf,cutCell,slantedCell}-1000-{0,3000,4000,5000,6000}m-linearUpwind/s3.uploaded
./singularity.ninja.sh $@ build/mountainAdvect-maxdt-{btf,cutCell,slantedCell}-6000m-cubicFit-collated/s3.uploaded

