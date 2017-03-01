from lxml import etree

html = '''
    <head></head>
    <body>
        <ul id="useful">
            <li>AAA</li>
            <li>BBB</li>
            <li>CCC</li>
        </ul>
        <ul id="unusefuls">
            <li>DDD</li>
            <li>FFFF</li>
            <li>EEE</li>
        </ul>
        <a id="ddd">BBDFDASd</a>
        <a href="www.baidu.com"></a>
        <a href="www.jikexuyuan.com"></a>
    </body>

'''
select = etree.HTML(html)
content = select.xpath('//ul[@id="useful"]/li/text()')
print(content)
for li in content:
    print(content, li)

link = select.xpath('//a/@href')
for l in link:
    print(l)
