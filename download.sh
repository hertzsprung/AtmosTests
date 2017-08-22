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
aws s3 cp --recursive ${s3uri}tfAdvect-btf-linearUpwind-collated build/tfAdvect-btf-linearUpwind-collated
aws s3 cp --recursive ${s3uri}tfAdvect-cutCell-linearUpwind-collated build/tfAdvect-cutCell-linearUpwind-collated
aws s3 cp --recursive ${s3uri}tfAdvect-btf-cubicFit-collated build/tfAdvect-btf-cubicFit-collated
aws s3 cp --recursive ${s3uri}tfAdvect-cutCell-cubicFit-collated build/tfAdvect-cutCell-cubicFit-collated
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
