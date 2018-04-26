# ## this file is for houdini session module in houGilligan

import sys
# import gilligan lib
sys.path.append("/DPA/wookie/dpa/projects/jingcoz/share/")


# return node from node geom detail attribute
def node_from_path_attr(input_node, path_attr):
    # get wavesurfer sim node input
    geo = input_node.geometry()
    if geo.findGlobalAttrib(path_attr) is None:
        raise hou.NodeError("Invalid input {}".format(path_attr))
    nodepath = geo.stringAttribValue(path_attr)
    node = hou.node(nodepath)
    if node is None:
        raise hou.NodeError("Invalid input {}".format(path_attr))
    return node


# store node current path into detail attribute
def store_node_path_attr(input_node, path_attr):
    geo = input_node.geometry()
    # create wavesurfer path detail attribute
    if geo.findGlobalAttrib(path_attr) is None:
        geo.addAttrib(hou.attribType.Global, path_attr, '')
    geo.setGlobalAttribValue(path_attr, input_node.path())
