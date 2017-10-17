#!/bin/bash
set -e
set -a
source build.properties

mkdir -p build
aws s3 cp --recursive ${s3uri}schaerAdvect-btf-1000-linearUpwind build/schaerAdvect-btf-1000-linearUpwind
aws s3 cp --recursive ${s3uri}schaerAdvect-cutCell-1000-linearUpwind build/schaerAdvect-cutCell-1000-linearUpwind
aws s3 cp --recursive ${s3uri}schaerAdvect-btf-1000-cubicFit build/schaerAdvect-btf-1000-cubicFit
aws s3 cp --recursive ${s3uri}schaerAdvect-cutCell-1000-cubicFit build/schaerAdvect-cutCell-1000-cubicFit
aws s3 cp --recursive ${s3uri}schaerAdvect-btf-linearUpwind-collated build/schaerAdvect-btf-linearUpwind-collated
aws s3 cp --recursive ${s3uri}schaerAdvect-cutCell-linearUpwind-collated build/schaerAdvect-cutCell-linearUpwind-collated
aws s3 cp --recursive ${s3uri}schaerAdvect-btf-cubicFit-collated build/schaerAdvect-btf-cubicFit-collated
aws s3 cp --recursive ${s3uri}schaerAdvect-cutCell-cubicFit-collated build/schaerAdvect-cutCell-cubicFit-collated

aws s3 cp --recursive ${s3uri}tfAdvect-btf-1000-linearUpwind build/tfAdvect-btf-1000-linearUpwind
aws s3 cp --recursive ${s3uri}tfAdvect-cutCell-1000-linearUpwind build/tfAdvect-cutCell-1000-linearUpwind
aws s3 cp --recursive ${s3uri}tfAdvect-btf-1000-cubicFit build/tfAdvect-btf-1000-cubicFit
aws s3 cp --recursive ${s3uri}tfAdvect-cutCell-1000-cubicFit build/tfAdvect-cutCell-1000-cubicFit
aws s3 cp --recursive ${s3uri}tfAdvect-btf-linearUpwind-collated build/tfAdvect-btf-linearUpwind-collated
aws s3 cp --recursive ${s3uri}tfAdvect-cutCell-linearUpwind-collated build/tfAdvect-cutCell-linearUpwind-collated
aws s3 cp --recursive ${s3uri}tfAdvect-btf-cubicFit-collated build/tfAdvect-btf-cubicFit-collated
aws s3 cp --recursive ${s3uri}tfAdvect-cutCell-cubicFit-collated build/tfAdvect-cutCell-cubicFit-collated

aws s3 cp --recursive ${s3uri}deformationSphere-mesh-hex-4 build/deformationSphere-mesh-hex-4
aws s3 cp --recursive ${s3uri}deformationSphere-mesh-hex-9 build/deformationSphere-mesh-hex-9
aws s3 cp --recursive ${s3uri}deformationSphere-gaussians-hex-8-cubicFit build/deformationSphere-gaussians-hex-8-cubicFit
aws s3 cp --recursive ${s3uri}deformationSphere-gaussians-hex-linearUpwind-collated build/deformationSphere-gaussians-hex-linearUpwind-collated
aws s3 cp --recursive ${s3uri}deformationSphere-gaussians-hex-cubicFit-collated build/deformationSphere-gaussians-hex-cubicFit-collated
aws s3 cp --recursive ${s3uri}deformationSphere-gaussians-cubedSphere-linearUpwind-collated build/deformationSphere-gaussians-cubedSphere-linearUpwind-collated
aws s3 cp --recursive ${s3uri}deformationSphere-gaussians-cubedSphere-cubicFit-collated build/deformationSphere-gaussians-cubedSphere-cubicFit-collated

aws s3 cp --recursive ${s3uri}mountainAdvect-h0-btf-1000-linearUpwind-collated build/mountainAdvect-h0-btf-1000-linearUpwind-collated
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-btf-1000-cubicFit-collated build/mountainAdvect-h0-btf-1000-cubicFit-collated
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-cutCell-1000-linearUpwind-collated build/mountainAdvect-h0-cutCell-1000-linearUpwind-collated
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-cutCell-1000-cubicFit-collated build/mountainAdvect-h0-cutCell-1000-cubicFit-collated
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-slantedCell-1000-linearUpwind-collated build/mountainAdvect-h0-slantedCell-1000-linearUpwind-collated
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-slantedCell-1000-cubicFit-collated build/mountainAdvect-h0-slantedCell-1000-cubicFit-collated
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-btf-1000-5000m-linearUpwind build/mountainAdvect-h0-btf-1000-5000m-linearUpwind
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-btf-1000-5000m-cubicFit build/mountainAdvect-h0-btf-1000-5000m-cubicFit
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-cutCell-1000-5000m-linearUpwind build/mountainAdvect-h0-cutCell-1000-5000m-linearUpwind
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-cutCell-1000-5000m-cubicFit build/mountainAdvect-h0-cutCell-1000-5000m-cubicFit
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-slantedCell-1000-5000m-linearUpwind build/mountainAdvect-h0-slantedCell-1000-5000m-linearUpwind
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-slantedCell-1000-5000m-cubicFit build/mountainAdvect-h0-slantedCell-1000-5000m-cubicFit
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-btf-1000-0m-linearUpwind build/mountainAdvect-h0-btf-1000-0m-linearUpwind
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-btf-1000-3000m-linearUpwind build/mountainAdvect-h0-btf-1000-3000m-linearUpwind
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-btf-1000-4000m-linearUpwind build/mountainAdvect-h0-btf-1000-4000m-linearUpwind
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-btf-1000-6000m-linearUpwind build/mountainAdvect-h0-btf-1000-6000m-linearUpwind
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-cutCell-1000-0m-linearUpwind build/mountainAdvect-h0-cutCell-1000-0m-linearUpwind
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-cutCell-1000-3000m-linearUpwind build/mountainAdvect-h0-cutCell-1000-3000m-linearUpwind
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-cutCell-1000-4000m-linearUpwind build/mountainAdvect-h0-cutCell-1000-4000m-linearUpwind
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-cutCell-1000-6000m-linearUpwind build/mountainAdvect-h0-cutCell-1000-6000m-linearUpwind
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-slantedCell-1000-0m-linearUpwind build/mountainAdvect-h0-slantedCell-1000-0m-linearUpwind
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-slantedCell-1000-3000m-linearUpwind build/mountainAdvect-h0-slantedCell-1000-3000m-linearUpwind
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-slantedCell-1000-4000m-linearUpwind build/mountainAdvect-h0-slantedCell-1000-4000m-linearUpwind
aws s3 cp --recursive ${s3uri}mountainAdvect-h0-slantedCell-1000-6000m-linearUpwind build/mountainAdvect-h0-slantedCell-1000-6000m-linearUpwind
aws s3 cp --recursive ${s3uri}mountainAdvect-maxdt-btf-6000m-cubicFit-collated build/mountainAdvect-maxdt-btf-6000m-cubicFit-collated
aws s3 cp --recursive ${s3uri}mountainAdvect-maxdt-cutCell-6000m-cubicFit-collated build/mountainAdvect-maxdt-cutCell-6000m-cubicFit-collated
aws s3 cp --recursive ${s3uri}mountainAdvect-maxdt-slantedCell-6000m-cubicFit-collated build/mountainAdvect-maxdt-slantedCell-6000m-cubicFit-collated

aws s3 cp --recursive ${s3uri}resting-mesh-btf-6000m build/resting-mesh-btf-6000m
aws s3 cp --recursive ${s3uri}resting-mesh-sleve-6000m build/resting-mesh-sleve-6000m
aws s3 cp --recursive ${s3uri}resting-mesh-cutCell-6000m build/resting-mesh-cutCell-6000m
aws s3 cp --recursive ${s3uri}resting-mesh-slantedCell-6000m build/resting-mesh-slantedCell-6000m
aws s3 cp --recursive ${s3uri}resting-btf-1000m-cubicFit build/resting-btf-1000m-cubicFit
aws s3 cp --recursive ${s3uri}resting-sleve-1000m-cubicFit build/resting-sleve-1000m-cubicFit
aws s3 cp --recursive ${s3uri}resting-cutCell-1000m-cubicFit build/resting-cutCell-1000m-cubicFit
aws s3 cp --recursive ${s3uri}resting-slantedCell-1000m-cubicFit build/resting-slantedCell-1000m-cubicFit
aws s3 cp --recursive ${s3uri}resting-btf-cubicFit-collated build/resting-btf-cubicFit-collated
aws s3 cp --recursive ${s3uri}resting-sleve-cubicFit-collated build/resting-sleve-cubicFit-collated
aws s3 cp --recursive ${s3uri}resting-cutCell-cubicFit-collated build/resting-cutCell-cubicFit-collated
aws s3 cp --recursive ${s3uri}resting-slantedCell-cubicFit-collated build/resting-slantedCell-cubicFit-collated

aws s3 cp --recursive ${s3uri}schaerWaves-btf-300dz-linearUpwind build/schaerWaves-btf-300dz-linearUpwind
aws s3 cp --recursive ${s3uri}schaerWaves-btf-300dz-cubicFit build/schaerWaves-btf-300dz-cubicFit
aws s3 cp --recursive ${s3uri}schaerWaves-cutCell-300dz-cubicFit build/schaerWaves-cutCell-300dz-cubicFit
aws s3 cp --recursive ${s3uri}schaerWaves-slantedCell-300dz-cubicFit build/schaerWaves-slantedCell-300dz-cubicFit

aws s3 cp --recursive ${s3uri}schaerWavesCP-btf-300dz build/schaerWavesCP-btf-300dz

aws s3 cp --recursive ${s3uri}arakawaKonor-uniform-lorenz build/arakawaKonor-uniform-lorenz
aws s3 cp --recursive ${s3uri}arakawaKonor-uniform-cp build/arakawaKonor-uniform-cp
