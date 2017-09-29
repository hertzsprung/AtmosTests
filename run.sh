#!/bin/bash
set -e

ninja $@ build/{schaer,tf}Advect-{btf,cutCell}-1000-{linearUpwind,cubicFit}/10000/l{2,inf}errorT.txt
ninja $@ build/{schaer,tf}Advect-{btf,cutCell}-1000-linearUpwind/dt.txt
ninja $@ build/{schaer,tf}Advect-{btf,cutCell}-{linearUpwind,cubicFit}-collated/10000/l{2,inf}errorT.txt
ninja $@ build/deformationSphere-mesh-hex-{4,8,9}/averageEquatorialSpacing.txt
ninja $@ build/deformationSphere-gaussians-hex-8-cubicFit/{0,518400,1036800}/T
ninja $@ build/deformationSphere-{cosBells,gaussians}-{hex,cubedSphere}-{linearUpwind,cubicFit}-collated/1036800/l{2,inf}errorT.txt
ninja $@ build/mountainAdvect-h0-{btf,cutCell,slantedCell}-1000-5000m-linearUpwind/constant/polyMesh/{points,faces,owner,neighbour,boundary}
ninja $@ build/mountainAdvect-h0-{btf,cutCell,slantedCell}-1000-5000m-linearUpwind/system/controlDict
ninja $@ build/mountainAdvect-h0-{btf,cutCell,slantedCell}-1000-5000m-{linearUpwind,cubicFit}/10000/l{2,inf}errorT.txt
ninja $@ build/mountainAdvect-h0-{btf,cutCell,slantedCell}-1000-{linearUpwind,cubicFit}-collated/10000/l2errorT.txt
ninja $@ build/mountainAdvect-h0-{btf,cutCell,slantedCell}-1000-{0,3000,4000,5000,6000}m-linearUpwind/dt.txt
ninja $@ build/mountainAdvect-maxdt-{btf,cutCell,slantedCell}-6000m-cubicFit-collated/{dt,co}.txt
ninja $@ build/mountainAdvect-h0-slantedCell-1000-6000m-linearUpwind/co.txt
ninja $@ build/mountainAdvect-h0-{btf,cutCell,slantedCell}-1000-5000m-linearUpwind/10000/{T,T_analytic,T_diff}
ninja $@ build/resting-{btf,sleve,cutCell,slantedCell}-{linearUpwind,cubicFit}-collated/maxw.txt
ninja $@ build/schaerWaves-btf-300dz-linearUpwind/18000/Uf
ninja $@ build/schaerWaves-btf-50dz-cubicFit/18000/theta_diff
ninja $@ build/thermalAdvect-{btf,cutCell,slantedCell}-{500,300,250,200,150,125,100,75,50}dz-cubicFit/18000/T_diff.sampleLine.dat
