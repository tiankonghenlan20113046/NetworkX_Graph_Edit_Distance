
import math
from cost_functions import CostFunctions

class GRECCostFunctions(CostFunctions):

    def __init__(self):
        super(CostFunctions, self).__init__()

    def node_substitution_cost(self, start, end): #定义节点替换代价
        if(start["type"]==end["type"]):#节点类型相同时候，节点替换代价为俩个点的欧式距离
            x_start, y_start = float(start["x"]), float(start["y"])
            x_end, y_end = float(end["x"]), float(end["y"])
            distance =  math.sqrt(math.pow((x_end - x_start), 2.)
                                + math.pow((y_end - y_start), 2.))
            return 0.5 * distance
        else: #节点的类型不同时，节点的替换代价为90
            return  90

    def node_deletion_cost(self, start):#定义节点的删除代价，45
        return 45

    def node_insertion_cost(self, end):#定义节点的插入代价：45
        return 45

    def edge_substitution_cost(self, start,end):
        start_frequency, end_frequency = float(start["frequency"]), float(end["frequency"])
        if (start_frequency == 1 and end_frequency == 1):
            start_type = start["type0"]
            end_type = end["type0"]
            if (start_type==end_type):
                return 0
            else:
                return 15
        elif(start_frequency == 2 and end_frequency == 2):
            return 0
        else:
            return 7.5


    def edge_deletion_cost(self, start):
        return 7.5 * float(start["frequency"])


    def edge_insertion_cost(self, end):
        return 7.5 * float(end["frequency"])
