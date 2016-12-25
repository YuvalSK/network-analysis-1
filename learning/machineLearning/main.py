import os
import sys
import LearningPhase
import FeturesMatrix

def import_path(fullpath):
    """
    Import a file with full path specification. Allows one to
    import from anywhere, something __import__ does not do.
    """
    path, filename = os.path.split(fullpath)
    filename, ext = os.path.splitext(filename)
    sys.path.append(path)
    module = __import__(filename)
    reload(module) # Might be out of date
    del sys.path[-1]
    return module


currentDirectory = str(os.getcwd())
f = import_path(currentDirectory + r'.\..\..\graph-fetures\fetures.py')

# 1 - Degrees
# 2 - betweenes
# 3 - closeness
# 4 - bfs moments
# 5 - flow
# 6 - A.B
# 7 - motif3
# 8 - motif4
# 9 - k-core
# 10 - louvain


result  = f.calc_fetures(file_input = r'c:\users\keren\Documents\github\network-analysis\data\roi-graph.txt'
                        ,motif_path = r'C:\Users\Keren\Documents\GitHub\network-analysis\graph-fetures\algo\motifVariations'
                       ,outputDirectory=r'c:\users\keren\Documents\github\network-analysis\graph-fetures'
                       ,directed=True
                       ,weighted=False
                       ,fetures_list=['general','closeness','bfsmoments','flow','ab','motif3','kcore'])


fileNameTags = r'c:\users\keren\Documents\github\network-analysis\data\roi-graph_tags.txt'

gnx = result[0]
map_fetures = result[1]
print map_fetures[1]
print map_fetures[3]
matrix = FeturesMatrix.build_matrix_with_tags(gnx,map_fetures,fileNameTags)
l = LearningPhase.learningPhase(matrix[:,1:],matrix[:,0])

l.implementLearningMethod()