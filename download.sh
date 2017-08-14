#!/bin/bash
set -e
set -a
source build.properties

mkdir -p build
aws s3 cp --recursive ${s3uri}schaerAdvect-btf-1000-linearUpwind build/schaerAdvect-btf-1000-linearUpwind
aws s3 cp --recursive ${s3uri}schaerAdvect-cutCell-1000-linearUpwind build/schaerAdvect-cutCell-1000-linearUpwind
aws s3 cp --recursive ${s3uri}schaerAdvect-btf-1000-cubicFit build/schaerAdvect-btf-1000-cubicFit
aws s3 cp --recursive ${s3uri}schaerAdvect-cutCell-1000-cubicFit build/schaerAdvect-cutCell-1000-cubicFit
aws s3 cp --recursive ${s3uri}tfAdvect-btf-1000-linearUpwind build/tfAdvect-btf-1000-linearUpwind
aws s3 cp --recursive ${s3uri}tfAdvect-cutCell-1000-linearUpwind build/tfAdvect-cutCell-1000-linearUpwind
aws s3 cp --recursive ${s3uri}tfAdvect-btf-1000-cubicFit build/tfAdvect-btf-1000-cubicFit
aws s3 cp --recursive ${s3uri}tfAdvect-cutCell-1000-cubicFit build/tfAdvect-cutCell-1000-cubicFit
aws s3 cp --recursive ${s3uri}schaerAdvect-btf-linearUpwind-collated build/schaerAdvect-btf-linearUpwind-collated
aws s3 cp --recursive ${s3uri}schaerAdvect-cutCell-linearUpwind-collated build/schaerAdvect-cutCell-linearUpwind-collated
aws s3 cp --recursive ${s3uri}schaerAdvect-btf-cubicFit-collated build/schaerAdvect-btf-cubicFit-collated
aws s3 cp --recursive ${s3uri}schaerAdvect-cutCell-cubicFit-collated build/schaerAdvect-cutCell-cubicFit-collated
