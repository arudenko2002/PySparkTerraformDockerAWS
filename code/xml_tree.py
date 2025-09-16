import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    print("ELEM", elem, level)
    if len(elem)==0:
        if level >= maxdepth:
            maxdepth = level+1
            return
    # your code goes here
    for el in elem:
        depth(el,level+1)

if __name__ == '__main__':
    #n = int(input())
    xml = """<feed xml:lang='en'>
  <title>HackerRank</title>
  <subtitle lang='en'>Programming challenges</subtitle>
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
  <updated>2013-12-25T12:00:00</updated>
</feed>"""
    xml2 = """<feed xml:lang='en'>
  <title>HackerRank</title>
  <subtitle lang='en'>Programming challenges</subtitle>
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
  <updated>2013-12-25T12:00:00</updated>
  <entry>
  	<author gender='male'>Harsh</author>
    <question type='hard'>XML 1</question>
    <description type='text'>This is related to XML parsing</description>
  </entry>
</feed>"""
    #print(xml)
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)