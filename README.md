# pdf_processor
利用pdf_processor可以对pdf进行一些简单的操作
基于reportlab和PyPDF2。
免去麻烦的img2pdf和pdf2img的安装，不经过图片处理，就是简单的pdf合并。
如：
加密
加水印
分割
合并


如果出现报错：

    UnicodeEncodeError: 'latin-1' codec can't encode characters in position 8-9: ordinal not in range(256)
需要将
site-packages\PyPDF2\utils.py中的：

    r = s.encode('latin-1')
替换为

    try:
        r = s.encode('latin-1')
        if len(s) < 2:
            bc[s] = r
        return r
    except Exception as e:
        print(s)
        r = s.encode('utf-8')
        if len(s) < 2:
            bc[s] = r
        return r

