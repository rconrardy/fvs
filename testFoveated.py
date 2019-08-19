from test import testFoveated
import src as fvs
import os

dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\vid'

print(dir_path + '\\testslow1.mp4')

print("\\begin{figure}")
print("\t\\centering")
print("\t\\begin{tabular}{ l | l l l l }")
print("\tSpeed & Axis", "&", "Frames", "&", "Time (s)", "&", "Time/Iteration (s)", "&", "Accuracy", "\\\\", "\\hline")
print("\t\\hline")
numFrames, detFrames, totTime = testFoveated(dir_path + '\\testslow1.mp4', 'exp', 6, 48, 'area')
print("\tSlow XY", "&", numFrames, "&", totTime, "&", totTime/numFrames, "&", detFrames/numFrames, "\\\\")
