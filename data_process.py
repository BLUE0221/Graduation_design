from xml.dom.minidom import parse
import xml.dom.minidom

def get_xml_data(file_name):
    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse(file_name)
    collection = DOMTree.documentElement
    DOCS=collection.getElementsByTagName("Doc")
    data=[]
    for DOC in DOCS:
        doc=[]
        doc_content=''
        Sentences=DOC.getElementsByTagName('Sentence')
        for Sentence in Sentences:
            try:
                if Sentence.hasAttribute('label'):
                    label=eval(Sentence.getAttribute('label'))
                    doc.append((Sentence.childNodes[0].data,label))
            except:
                continue
            doc_content+=Sentence.childNodes[0].data
        [data.append((d,doc_content)) for d in doc]
    sents=[temp[0][0] for temp in data]
    contexts=[temp[1] for temp in data]
    labels=[temp[0][1] for temp in data]
    
    return sents,contexts,labels