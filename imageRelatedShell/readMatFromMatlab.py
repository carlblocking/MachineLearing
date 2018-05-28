import scipy.io as scio

# dataFile="D:/weakalign/datasets/proposal-flow-pascal/PF-dataset-PASCAL/Annotations/car/2008_002704.mat"
dataFile="D:/weakalign/datasets/proposal-flow-pascal/PF-dataset-PASCAL/parsePascalVOC.mat"
data=scio.loadmat(dataFile)
print(data)
