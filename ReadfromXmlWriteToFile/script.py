import xml.etree.cElementTree as ET

tree = ET.ElementTree(file='input.xml')
root = tree.getroot()

for books in root:
    if(books.tag=='book'):
        fo = open(books.get('id') + '.txt', 'wb')
        #print 'Book iD : ' + books.get('id')
        #print '---------------'
        for attr in books:
            if (attr.tag=='author' or attr.tag=='title' or attr.tag=='price' ):
                #print (attr.text)
                fo.write(attr.tag + ' : ' +attr.text)
                fo.write('\n\n')
        #print ('************')
