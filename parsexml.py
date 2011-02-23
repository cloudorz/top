#
import xml.dom.minidom

def xml2dict(xmlstring):
	doc = xml.dom.minidom.parseString(xmlstring)
	remove_whilespace_nodes(doc)
	return nodeToDic(doc)

class NotTextNodeError(Exception):
    pass

def getTextFromNode(node):
    """
    scans through all children of node and gathers the
    text. if node has non-text child-nodes, then
    NotTextNodeError is raised.
    """
    t = ""
    for n in node.childNodes:
	if n.nodeType == n.TEXT_NODE:
	    t += n.nodeValue
	else:
	    raise NotTextNodeError
    return t

def nodeToDic(node):

    dic = {}
    multlist = {} # holds temporary lists where there are multiple children
    multiple = False
    for n in node.childNodes:
        if n.nodeType != n.ELEMENT_NODE:
            continue

        # find out if there are multiple records
        if len(node.getElementsByTagName(n.nodeName)) > 1:
            multiple = True
            # and set up the list to hold the values
            if not multlist.has_key(n.nodeName):
                multlist[n.nodeName] = []

        try:
            #text node
            text = getTextFromNode(n)
        except NotTextNodeError:
            if multiple:
                # append to our list
                multlist[n.nodeName].append(nodeToDic(n))
                dic.update({n.nodeName:multlist[n.nodeName]})
                continue
            else:
                # 'normal' node
                dic.update({n.nodeName:nodeToDic(n)})
                continue

        # text node
        if multiple:
            multlist[n.nodeName].append(text)
            dic.update({n.nodeName:multlist[n.nodeName]})
        else:
            dic.update({n.nodeName:text})
    return dic

def remove_whilespace_nodes(node, unlink=True):
	remove_list = []
	for child in node.childNodes:
		if child.nodeType == xml.dom.Node.TEXT_NODE and not child.data.strip():
			remove_list.append(child)
		elif child.hasChildNodes():
			remove_whilespace_nodes(child, unlink)
	for node in remove_list:
		node.parentNode.removeChild(node)
		if unlink:
			node.unlink()

# the second way to do this 
# because it can know list or single
def elementtodict(parent):
	child = parent.firstChild
	if (not child):
		return None
	elif (child.nodeType == xml.dom.minidom.Node.TEXT_NODE):
		return child.nodeValue
	
	d={}
	while child is not None:
		if (child.nodeType == xml.dom.minidom.Node.ELEMENT_NODE):
                    try:
                        d[child.tagName]
                    except KeyError:
                		d[child.tagName]=[]
                    d[child.tagName].append(elementtodict(child))
		child = child.nextSibling
	return d

