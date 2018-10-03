# ## this file is for houdini session module in houGilligan
# ## set up session module in: window->python source editor (the module source code is evaluated when the scene file is loaded, and is available to other Python code as hou.session)

import sys
# import gilligan lib
sys.path.append("/DPA/wookie/dpa/projects/jingcoz/share/")


# return node from node geom detail attribute
def node_from_path_attr(input_node, path_attr):
    # get wavesurfer sim node input
    geo = input_node.geometry()
    if geo.findGlobalAttrib(path_attr) is None:
        return None
    nodepath = geo.stringAttribValue(path_attr)
    node = hou.node(nodepath)

    return node


# store node current path into detail attribute
def store_node_path_attr(input_node, path_attr):
    geo = input_node.geometry()
    # create wavesurfer path detail attribute
    if geo.findGlobalAttrib(path_attr) is None:
        geo.addAttrib(hou.attribType.Global, path_attr, '')
    geo.setGlobalAttribValue(path_attr, input_node.path())
