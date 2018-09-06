
from graphviz import Digraph

f = Digraph('finite_state_machine', filename='dijikstra.gv')
f.attr(rankdir='LR', size='8,5')

#f.attr('node', shape='doublecircle')
#f.node('LR_0')
#f.node('LR_3')
#f.node('LR_4')
#f.node('LR_8')

f.attr('node', shape='circle')
f.edge('A', 'E', label='6')
f.edge('A', 'D', label='8')
f.edge('C', 'B', label='4')
f.edge('C', 'D', label='4')
f.edge('C', 'E', label='2')
f.edge('D', 'B', label='3')
f.edge('D', 'C', label='4')
f.edge('E', 'C', label='2')
f.edge('E', 'A', label='6')
f.edge('B', 'C', label='4')
f.edge('B', 'D', label='3')


f.view()
