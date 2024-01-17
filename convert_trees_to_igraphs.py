#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 11:35:45 2023

@author: muhkham
"""


from igraph import Graph
import pandas as pd
import json
import os

df = pd.read_pickle(r"/home/muhkham/ppg_shlomchik/df_spl.pkl")


subjects_dict = {   
                    #1: 'D221',
                    2: 'D228',
                    #3: 'D250',
                    4: 'D315',
                    5: 'D328',   
                }

#functions of building the igraph from json_tree:
def add_node(graph, node_data):
    graph.add_vertex(**node_data)
    return graph.vs[-1].index

def add_edges(graph, parent_idx, children_data):
    for child_data in children_data:
        child_idx = add_node(graph, child_data['data'])
        graph.add_edge(parent_idx, child_idx)
        if child_data.get('children'):
            add_edges(graph, child_idx, child_data['children'])



for subject_id, subject_name in subjects_dict.items():
    list_igraphs = []
    #df_sub = df.loc[ df['subject_id'] == subject_id ]
    # # Your JSON data
    # json_data = '{"info": {"min_count": 1, "min_samples": 1, "exclude_stops": false}, "tree": {"data": {"subsets": "", "copy_number": 0, "tissues": "", "mutations": [], "ig_classes": "", "seq_ids": {}}, "children": [{"data": {"subsets": [], "copy_number": 0, "tissues": [], "mutations": [{"to": "T", "from": "G", "pos": 226}], "ig_classes": [], "seq_ids": {}}, "children": [{"data": {"subsets": [], "copy_number": 0, "tissues": [], "mutations": [{"to": "C", "from": "G", "pos": 172}], "ig_classes": [], "seq_ids": {}}, "children": [{"data": {"subsets": [], "copy_number": 0, "tissues": [], "mutations": [{"to": "A", "from": "G", "pos": 303}, {"to": "T", "from": "C", "pos": 211}, {"to": "T", "from": "C", "pos": 279}, {"to": "T", "from": "C", "pos": 339}, {"to": "T", "from": "C", "pos": 271}], "ig_classes": [], "seq_ids": {}}, "children": [{"data": {"subsets": [], "copy_number": 0, "tissues": [], "mutations": [{"to": "T", "from": "C", "pos": 86}, {"to": "T", "from": "C", "pos": 105}, {"to": "C", "from": "G", "pos": 107}, {"to": "A", "from": "T", "pos": 114}, {"to": "G", "from": "A", "pos": 129}, {"to": "C", "from": "G", "pos": 119}, {"to": "T", "from": "C", "pos": 108}, {"to": "T", "from": "C", "pos": 104}], "ig_classes": [], "seq_ids": {}}, "children": [{"data": {"subsets": ["CD19+CD27+CD45RB-CD69-"], "copy_number": 2, "tissues": ["SPL"], "mutations": [{"to": "C", "from": "T", "pos": 109}], "ig_classes": [null], "seq_ids": {"M03592:64:000000000-B94YH:1:2115:15646:19210": {"subset": "CD19+CD27+CD45RB-CD69-", "ig_class": null, "copy_number": 1, "tissue": "SPL", "sample_name": "D328-SP-MBC-P13-rep1-150ng_S4_2017-07-28"}, "M03592:64:000000000-B94YH:1:2113:28599:9862": {"subset": "CD19+CD27+CD45RB-CD69-", "ig_class": null, "copy_number": 1, "tissue": "SPL", "sample_name": "D328-SP-MBC-P13-rep2-150ng_S15_2017-07-28"}}}, "children": []}, {"data": {"subsets": ["CD19+CD27+CD45RB+CD69-", "CD19+CD27+CD45RB-CD69-"], "copy_number": 38, "tissues": ["SPL"], "mutations": [{"to": "C", "from": "T", "pos": 75}], "ig_classes": [null], "seq_ids": {"M03592:64:000000000-B94YH:1:2104:9870:23209": {"subset": "CD19+CD27+CD45RB-CD69-", "ig_class": null, "copy_number": 24, "tissue": "SPL", "sample_name": "D328-SP-MBC-P13-rep2-150ng_S15_2017-07-28"}, "M03592:64:000000000-B94YH:1:2117:23535:11521": {"subset": "CD19+CD27+CD45RB+CD69-", "ig_class": null, "copy_number": 1, "tissue": "SPL", "sample_name": "D328-SP-MBC-P11-rep2-150ng_S13_2017-07-28"}, "M03592:64:000000000-B94YH:1:2118:13293:13309": {"subset": "CD19+CD27+CD45RB+CD69-", "ig_class": null, "copy_number": 2, "tissue": "SPL", "sample_name": "D328-SP-MBC-P11-rep1-150ng_S2_2017-07-28"}, "M03592:64:000000000-B94YH:1:2115:21518:5564": {"subset": "CD19+CD27+CD45RB-CD69-", "ig_class": null, "copy_number": 11, "tissue": "SPL", "sample_name": "D328-SP-MBC-P13-rep1-150ng_S4_2017-07-28"}}}, "children": []}]}, {"data": {"subsets": ["CD19+CD27+CD45RB-CD69-"], "copy_number": 2, "tissues": ["SPL"], "mutations": [{"to": "C", "from": "T", "pos": 75}, {"to": "A", "from": "C", "pos": 108}, {"to": "T", "from": "C", "pos": 84}, {"to": "T", "from": "A", "pos": 115}, {"to": "G", "from": "A", "pos": 103}, {"to": "G", "from": "C", "pos": 87}, {"to": "G", "from": "C", "pos": 105}], "ig_classes": [null], "seq_ids": {"M03592:64:000000000-B94YH:1:1104:6999:15964": {"subset": "CD19+CD27+CD45RB-CD69-", "ig_class": null, "copy_number": 2, "tissue": "SPL", "sample_name": "D328-SP-MBC-P13-rep2-150ng_S15_2017-07-28"}}}, "children": []}]}, {"data": {"subsets": [], "copy_number": 0, "tissues": [], "mutations": [{"to": "T", "from": "C", "pos": 86}, {"to": "G", "from": "A", "pos": 337}, {"to": "C", "from": "G", "pos": 107}, {"to": "C", "from": "T", "pos": 109}, {"to": "T", "from": "C", "pos": 84}, {"to": "T", "from": "C", "pos": 249}, {"to": "C", "from": "G", "pos": 119}, {"to": "G", "from": "C", "pos": 329}, {"to": "T", "from": "C", "pos": 104}], "ig_classes": [], "seq_ids": {}}, "children": [{"data": {"subsets": ["CD19+CD27+CD45RB-CD69-"], "copy_number": 46, "tissues": ["SPL"], "mutations": [{"to": "A", "from": "G", "pos": 284}, {"to": "A", "from": "G", "pos": 210}, {"to": "T", "from": "G", "pos": 303}, {"to": "G", "from": "A", "pos": 209}, {"to": "T", "from": "A", "pos": 85}, {"to": "A", "from": "C", "pos": 120}, {"to": "A", "from": "G", "pos": 301}, {"to": "T", "from": "G", "pos": 147}, {"to": "C", "from": "T", "pos": 186}, {"to": "A", "from": "T", "pos": 189}, {"to": "C", "from": "A", "pos": 265}, {"to": "T", "from": "C", "pos": 211}, {"to": "C", "from": "A", "pos": 327}, {"to": "G", "from": "T", "pos": 114}, {"to": "T", "from": "C", "pos": 255}, {"to": "G", "from": "C", "pos": 87}, {"to": "T", "from": "C", "pos": 264}], "ig_classes": [null], "seq_ids": {"M03592:64:000000000-B94YH:1:2115:5701:15638": {"subset": "CD19+CD27+CD45RB-CD69-", "ig_class": null, "copy_number": 39, "tissue": "SPL", "sample_name": "D328-SP-MBC-P13-rep1-150ng_S4_2017-07-28"}, "M03592:64:000000000-B94YH:1:2110:26344:14951": {"subset": "CD19+CD27+CD45RB-CD69-", "ig_class": null, "copy_number": 7, "tissue": "SPL", "sample_name": "D328-SP-MBC-P13-rep2-150ng_S15_2017-07-28"}}}, "children": [{"data": {"subsets": ["CD19+CD27+CD45RB-CD69-"], "copy_number": 2, "tissues": ["SPL"], "mutations": [{"to": "A", "from": "T", "pos": 75}], "ig_classes": [null], "seq_ids": {"M03592:64:000000000-B94YH:1:1101:10191:13276": {"subset": "CD19+CD27+CD45RB-CD69-", "ig_class": null, "copy_number": 1, "tissue": "SPL", "sample_name": "D328-SP-MBC-P13-rep1-150ng_S4_2017-07-28"}, "M03592:64:000000000-B94YH:1:2119:13704:5961": {"subset": "CD19+CD27+CD45RB-CD69-", "ig_class": null, "copy_number": 1, "tissue": "SPL", "sample_name": "D328-SP-MBC-P13-rep2-150ng_S15_2017-07-28"}}}, "children": []}]}, {"data": {"subsets": [], "copy_number": 0, "tissues": [], "mutations": [{"to": "A", "from": "G", "pos": 303}, {"to": "C", "from": "G", "pos": 73}, {"to": "T", "from": "C", "pos": 87}], "ig_classes": [], "seq_ids": {}}, "children": [{"data": {"subsets": ["CD19+CD27+CD45RB-CD69-"], "copy_number": 12, "tissues": ["SPL"], "mutations": [{"to": "T", "from": "C", "pos": 211}, {"to": "C", "from": "T", "pos": 150}, {"to": "A", "from": "G", "pos": 254}, {"to": "T", "from": "C", "pos": 198}, {"to": "C", "from": "A", "pos": 129}, {"to": "T", "from": "C", "pos": 177}], "ig_classes": [null], "seq_ids": {"M03592:64:000000000-B94YH:1:2102:13661:23613": {"subset": "CD19+CD27+CD45RB-CD69-", "ig_class": null, "copy_number": 12, "tissue": "SPL", "sample_name": "D328-SP-MBC-P13-rep2-150ng_S15_2017-07-28"}}}, "children": []}, {"data": {"subsets": ["CD19+CD27+CD45RB+CD69-", "CD19+CD27+CD45RB-CD69+", "CD19+CD27+CD45RB-CD69-"], "copy_number": 57, "tissues": ["SPL"], "mutations": [{"to": "T", "from": "C", "pos": 117}, {"to": "A", "from": "G", "pos": 241}, {"to": "C", "from": "G", "pos": 147}, {"to": "C", "from": "G", "pos": 284}], "ig_classes": [null], "seq_ids": {"M03592:64:000000000-B94YH:1:2114:4840:13900": {"subset": "CD19+CD27+CD45RB-CD69+", "ig_class": null, "copy_number": 9, "tissue": "SPL", "sample_name": "D328-SP-MBC-P14-rep2-150ng_S16_2017-07-28"}, "M03592:64:000000000-B94YH:1:1113:10409:10218": {"subset": "CD19+CD27+CD45RB-CD69-", "ig_class": null, "copy_number": 15, "tissue": "SPL", "sample_name": "D328-SP-MBC-P13-rep2-150ng_S15_2017-07-28"}, "M03592:64:000000000-B94YH:1:1105:2091:12286": {"subset": "CD19+CD27+CD45RB-CD69-", "ig_class": null, "copy_number": 30, "tissue": "SPL", "sample_name": "D328-SP-MBC-P13-rep1-150ng_S4_2017-07-28"}, "M03592:64:000000000-B94YH:1:2104:14622:1495": {"subset": "CD19+CD27+CD45RB-CD69-", "ig_class": null, "copy_number": 1, "tissue": "SPL", "sample_name": "D328-SP-MBC-P13-rep2-150ng_S15_2017-07-28"}, "M03592:64:000000000-B94YH:1:2106:3426:12405": {"subset": "CD19+CD27+CD45RB+CD69-", "ig_class": null, "copy_number": 2, "tissue": "SPL", "sample_name": "D328-SP-MBC-P11-rep1-150ng_S2_2017-07-28"}}}, "children": [{"data": {"subsets": ["CD19+CD27+CD45RB-CD69-"], "copy_number": 2, "tissues": ["SPL"], "mutations": [{"to": "T", "from": "A", "pos": 54}, {"to": "T", "from": "C", "pos": 69}, {"to": "C", "from": "T", "pos": 45}, {"to": "A", "from": "G", "pos": 61}, {"to": "C", "from": "G", "pos": 55}, {"to": "G", "from": "C", "pos": 51}, {"to": "A", "from": "C", "pos": 50}], "ig_classes": [null], "seq_ids": {"M03592:64:000000000-B94YH:1:2113:7063:11743": {"subset": "CD19+CD27+CD45RB-CD69-", "ig_class": null, "copy_number": 1, "tissue": "SPL", "sample_name": "D328-SP-MBC-P13-rep1-150ng_S4_2017-07-28"}, "M03592:64:000000000-B94YH:1:2114:15562:5976": {"subset": "CD19+CD27+CD45RB-CD69-", "ig_class": null, "copy_number": 1, "tissue": "SPL", "sample_name": "D328-SP-MBC-P13-rep2-150ng_S15_2017-07-28"}}}, "children": []}]}]}]}]}, {"data": {"subsets": [], "copy_number": 0, "tissues": [], "mutations": [{"to": "C", "from": "G", "pos": 303}, {"to": "T", "from": "C", "pos": 339}, {"to": "C", "from": "G", "pos": 119}, {"to": "C", "from": "G", "pos": 107}, {"to": "C", "from": "T", "pos": 109}], "ig_classes": [], "seq_ids": {}}, "children": [{"data": {"subsets": ["CD19+CD27+CD45RB+CD69+"], "copy_number": 11, "tissues": ["SPL"], "mutations": [{"to": "T", "from": "C", "pos": 86}, {"to": "C", "from": "G", "pos": 278}, {"to": "T", "from": "C", "pos": 211}, {"to": "T", "from": "A", "pos": 295}, {"to": "T", "from": "C", "pos": 231}, {"to": "G", "from": "A", "pos": 206}, {"to": "A", "from": "G", "pos": 270}, {"to": "G", "from": "A", "pos": 327}, {"to": "A", "from": "G", "pos": 221}, {"to": "T", "from": "C", "pos": 177}, {"to": "T", "from": "C", "pos": 104}, {"to": "C", "from": "T", "pos": 189}], "ig_classes": [null], "seq_ids": {"M03592:64:000000000-B94YH:1:1109:27096:15537": {"subset": "CD19+CD27+CD45RB+CD69+", "ig_class": null, "copy_number": 11, "tissue": "SPL", "sample_name": "D328-SP-MBC-P12-rep2-150ng_S14_2017-07-28"}}}, "children": []}, {"data": {"subsets": ["CD19+CD27+CD45RB-CD69+"], "copy_number": 25, "tissues": ["SPL"], "mutations": [{"to": "G", "from": "C", "pos": 261}, {"to": "T", "from": "C", "pos": 342}, {"to": "G", "from": "A", "pos": 225}, {"to": "G", "from": "A", "pos": 209}, {"to": "A", "from": "C", "pos": 120}, {"to": "A", "from": "C", "pos": 86}, {"to": "T", "from": "G", "pos": 221}, {"to": "C", "from": "T", "pos": 201}, {"to": "C", "from": "A", "pos": 103}, {"to": "G", "from": "T", "pos": 114}], "ig_classes": [null], "seq_ids": {"M03592:64:000000000-B94YH:1:2118:28409:13401": {"subset": "CD19+CD27+CD45RB-CD69+", "ig_class": null, "copy_number": 25, "tissue": "SPL", "sample_name": "D328-SP-MBC-P14-rep2-150ng_S16_2017-07-28"}}}, "children": []}]}]}]}}'
    # json_data = json.loads(json_data)
    
        

    for clone_id in set( df['clone_id'].loc[df["subject_id"] == subject_id].tolist() ):
        #if pd.isna( set(df['tree'].loc[df['clone_id'] == clone_id]) ) == True:
            #continue
        #else: 
            json_data = df['tree'].loc[df["clone_id"] == clone_id].tolist()[0] #taking first tree (all trees the same for each clone)
            json_data = json.loads(json_data)
            
            tree_graph = Graph(directed=True)
            root_idx = add_node(tree_graph, json_data['tree'])
            add_edges(tree_graph, root_idx, json_data['tree']['children'])
            
            
            
            for vertex in tree_graph.vs:
                if vertex['subsets'] is None:
                    continue
                elif len( vertex['subsets'] ) > 0:
                    vertex['subset'] = ",".join( set([x[10:22] for x in vertex['subsets']]) )
                    vertex['tissue'] = vertex['tissues'][0] 
                vertex['clone_id'] = clone_id
            #append each igraph to the list
            list_igraphs.append(tree_graph)
            
            # for v in tree_graph.vs:
            #     print(f"Vertex {v.index}:")
            #     for attr_name, attr_value in v.attributes().items():
            #         print(f"{attr_name}: {attr_value}")
            #     print("\n") 
            
    #Save each graph to a separate GraphML file
    # Directory to save GraphML files
    output_dir = "/home/muhkham/ppg_shlomchik/results/sub_{}_graphs".format(subject_id)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    for i, graph in enumerate(list_igraphs):
        # Define the output file path (e.g., output_graphml/graph0.graphml)
        output_file = os.path.join(output_dir, f"graph{i}.graphml")
        
        # Save the graph to the GraphML file
        graph.write_graphml(output_file)
        
        print(f"Graph {i} saved to {output_file}")  

print("finished")

#tree_graph.save("/home/muhkham/ppg_shlomchik/sub_{}_graphs/tree_graph.graphml".format(subject_id), format="graphml")