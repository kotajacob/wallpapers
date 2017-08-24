#!/usr/bin/env python3

import os
import subprocess

INPUT_DIR = 'in'
OUTPUT_DIR = 'out'

def main():
    # get current directory
    cwd = os.getcwd()
    # get the directory of the input folder and output folder
    inDir = os.path.join(cwd, INPUT_DIR)
    outDir = os.path.join(cwd, OUTPUT_DIR)

    # loop through the files in the folder
    for f in os.listdir(inDir):
        if f.endswith(".jpg"):
            inFile = os.path.join(inDir, f)
            outFile = f[:-4] + ".png"
            outFile = os.path.join(outDir, outFile)
            subprocess.run(["ffmpeg", "-i", inFile, outFile])
        elif f.endswith(".jpeg"):
            inFile = os.path.join(inDir, f)
            outFile = f[:-5] + ".png"
            outFile = os.path.join(outDir, outFile)
            subprocess.run(["ffmpeg", "-i", inFile, outFile])
    print("Done")

if __name__ == '__main__':
    main()
