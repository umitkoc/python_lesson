from json import dump
from operator import itemgetter
from os import listdir, mkdir, path, remove
from time import sleep

import fitz
from docx2pdf import convert
# from PDFNetPython3 import *  ----> python version 3.5-3.8 with working
# from PDFNetPython3.PDFNetPython import Element, Image, PDFDoc, Point
from PyPDF2 import PdfFileReader, generic
from tabula import read_pdf

# site.addsitedir("../../../PDFNetC/Lib")


def sonuclar():
    print("analiz sonuçlarını yazıyoruz")
    _file = listdir(".")
    if not path.isdir("sonuc"):
        mkdir("sonuc")
    _font = ""
    _baslik = ""
    _about = ""
    with open("info.txt", "r", encoding="utf-8") as about:
        _about = about.read()
        about.close()
    with open("font.txt", "r", encoding="utf-8") as font:
        _font = font.read()
    with open("baslik.txt", "r", encoding="utf-8") as baslik:
        _baslik = baslik.read()
        baslik.close()
    with open("sonuc/sonuç.txt", "w", encoding="utf-8") as sonuc:
        sonuc.write(_font)
        sonuc.write(_baslik)
        sonuc.write(_about)
        sonuc.close()
    files = listdir(".")
    for file in files:
        if file.endswith(".txt") or file.endswith(".json"):
            remove(file)


def fonts(doc, granularity=False):
    styles = {}
    font_counts = {}

    for page in doc:
        blocks = page.getText("dict")["blocks"]
        for b in blocks:
            if b['type'] == 0:
                for l in b["lines"]:
                    for s in l["spans"]:
                        if granularity:
                            identifier = "{0}_{1}_{2}_{3}".format(
                                s['size'], s['flags'], s['font'], s['color'])
                            styles[identifier] = {'size': s['size'], 'flags': s['flags'], 'font': s['font'],
                                                  'color': s['color']}
                        else:
                            identifier = "{0}".format(s['size'])
                            styles[identifier] = {
                                'size': s['size'], 'font': s['font']}

                        font_counts[identifier] = font_counts.get(
                            identifier, 0) + 1  # count the fonts usage

    font_counts = sorted(font_counts.items(), key=itemgetter(1), reverse=True)

    if len(font_counts) < 1:
        raise ValueError("Zero discriminating fonts found!")

    return font_counts, styles


def font_tags(font_counts, styles):
    p_style = styles[font_counts[0][0]]
    p_size = p_style['size']
    font_sizes = []
    for (font_size, count) in font_counts:
        font_sizes.append(float(font_size))
    font_sizes.sort(reverse=True)
    idx = 0
    size_tag = {}
    for size in font_sizes:
        idx += 1
        if size == p_size:
            idx = 0
            size_tag[size] = '<p>'
        if size > p_size:
            size_tag[size] = '<h{0}>'.format(idx)
        elif size < p_size:
            size_tag[size] = '<s{0}>'.format(idx)

    return size_tag


def headers_para(doc, size_tag):
    header_para = []
    first = True
    previous_s = {}

    for page in doc:
        blocks = page.getText("dict")["blocks"]
        for b in blocks:
            if b['type'] == 0:

                block_string = ""
                for l in b["lines"]:
                    for s in l["spans"]:
                        if s['text'].strip():
                            if first:
                                previous_s = s
                                first = False
                                block_string = size_tag[s['size']] + s['text']
                            else:
                                if s['size'] == previous_s['size']:

                                    if block_string and all((c == "\n") for c in block_string):
                                        block_string = size_tag[s['size']
                                                                ] + s['text']
                                    if block_string == "":
                                        block_string = size_tag[s['size']
                                                                ] + s['text']
                                    else:
                                        block_string += " " + s['text']

                                else:
                                    header_para.append(block_string)
                                    block_string = size_tag[s['size']
                                                            ] + s['text']

                                previous_s = s

                    block_string += "\n"

                header_para.append(block_string)

    return header_para


def Header(file):
    document = file
    doc = fitz.open(document)
    font_counts, styles = fonts(doc, granularity=False)
    size_tag = font_tags(font_counts, styles)
    element = ""
    elements = headers_para(doc, size_tag)
    with open("h3.txt", "w", encoding="utf-8") as h3:
        for element in elements:
            if element.startswith("<h1>"):
                element = element.replace("<h1>", "\n")
                h3.write(element)
            elif element.startswith("<h2>"):
                element = element.replace("<h2>", "\n")
                h3.write(element)
            elif element.startswith("<h3>"):
                element = element.replace("<h3>", "\n")
                h3.write(element)
            elif element.startswith("<h4>"):
                element = element.replace("<h4>", "\n")
                h3.write(element)
    h3.close()

    with open("doc.json", 'w') as json_out:
        dump(elements, json_out)
    json_out.close()


def HeaderControl():
    basliklar = ""
    h3 = ["beyan", "önsöz", "içindekiler", "özet", "abstract", "şekiller listesi", "tablolar listesi",
          "ekler listesi", "simgeler ve kısaltmalar", "giriş", "sonuçlar", "öneriler", "kaynaklar", "ekler", "özgeçmiş"]

    with open("h3.txt", "r", encoding="utf-8") as header3:
        basliklar = header3.read()
        basliklar = basliklar.split("\n")
    header3.close()
    i = 0
    sayac = False
    with open("baslik.txt", "w", encoding="utf-8") as hatalar:
        while i < len(h3):
            j = 0
            while j < len(basliklar):
                if basliklar[j].lower == h3[i]:
                    sayac = True
                    break
                j += 1
            if not sayac:
                hatalar.write(h3[i] + ":başlık hatası bulundu\n")
                sayac = False

            i += 1
    hatalar.close()


def Tables(file):
    tables = read_pdf(file, pages="all")
    folder_name = "tables"
    if not path.isdir(folder_name):
        mkdir(folder_name)
    for i, table in enumerate(tables, start=1):
        table.to_excel(path.join(folder_name, "table_" +
                       str(i)+".xlsx"), index=False)


def walk(obj, fnt, emb):
    if not hasattr(obj, 'keys'):
        return None, None
    fontkeys = {'/FontFile', '/FontFile2', '/FontFile3'}
    if '/BaseFont' in obj:
        fnt.add(obj['/BaseFont'])
    if '/FontName' in obj:
        if [x for x in fontkeys if x in obj]:  # test to see if there is FontFile
            emb.add(obj['/FontName'])

    for k in obj.keys():
        walk(obj[k], fnt, emb)

    return fnt, emb  # return the sets for each page


def Font(file):
    data = []
    pdf = PdfFileReader(file)
    fonts = set()
    embedded = set()
    for page in pdf.pages:
        obj = page.getObject()
        if type(obj) == generic.ArrayObject:  # You can also do ducktyping here
            for i in obj:
                if hasattr(i, 'keys'):
                    f, e = walk(i, fonts, embedded)
                    fonts = fonts.union(f)
                    embedded = embedded.union(e)
        else:
            f, e = walk(obj['/Resources'], fonts, embedded)
            fonts = fonts.union(f)
            embedded = embedded.union(e)

    unembedded = fonts - embedded
    data.append('Kullanılmış Fontlar')
    font = ""
    for font in fonts:
        font = font.replace("/ABCDEE+", "")
        font = font.replace("/", "")
        data.append(font)
    return data


# Resim yolları resim çıkarma dosyasına yollanır


# def ImageExtractPath(file):
#     doc = PDFDoc(file)
#     doc.InitSecurityHandler()
#     counter = 0
#     cos_doc = doc.GetSDFDoc()
#     num_objs = cos_doc.XRefSize()
#     i = 1
#     while i < num_objs:
#         obj = cos_doc.GetObj(i)
#         if obj is not None and not obj.IsFree() and obj.IsStream():

#             # Process only images
#             itr = obj.Find("Type")

#             if not itr.HasNext() or not itr.Value().GetName() == "XObject":
#                 i = i + 1
#                 continue

#             itr = obj.Find("Subtype")
#             if not itr.HasNext() or not itr.Value().GetName() == "Image":
#                 i = i + 1
#                 continue
#             image = Image(obj)
#             counter += 1
#             print("--> Image: " + str(counter))
#             print("    Width: " + str(image.GetImageWidth()))
#             print("    Height: " + str(image.GetImageHeight()))
#             print("    BPC: " + str(image.GetBitsPerComponent()))
#             fname = "image_extract_" + str(counter)
#             _files = listdir(".")
#             if not path.isdir("images"):
#                 mkdir("images")
#             _path = path.abspath("images") + "\\" + fname
#             image.Export(_path)
#         i = i + 1
#     doc.Close()
#     print("Done.")
#     print("resimler başarılı bir şekilde çekildi")
#     print("----------------------------------")


# counter = 0


# # resimleri buradan çıkarmaya çalışır


# def ImageExtract(reader):
#     element = reader.Next()
#     while element is not None:
#         if (element.GetType() == Element.e_image or
#                 element.GetType() == Element.e_inline_image):
#             global counter
#             counter += 1
#             print("--> Image: " + str(counter))
#             print("    Width: " + str(element.GetImageWidth()))
#             print("    Height: " + str(element.GetImageHeight()))
#             print("    BPC: " + str(element.GetBitsPerComponent()))

#             ctm = element.GetCTM()
#             x2 = 1
#             y2 = 1
#             pt = Point(x2, y2)
#             point = ctm.Mult(pt)
#             print("    Coords: x1=%.2f, y1=%.2f, x2=%.2f, y2=%.2f" %
#                   (ctm.m_h, ctm.m_v, point.x, point.y))

#             if element.GetType() == Element.e_image:
#                 image = Image(element.GetXObject())

#                 fname = "image_" + str(counter)
#                 _path = path.abspath("images") + "\\" + fname
#                 image.Export(_path)

#         elif element.GetType() == Element.e_form:
#             reader.FormBegin()
#             ImageExtract(reader)
#             reader.End()
#         element = reader.Next()


# paragrafları Empty(),Punctuation() ve Quotation()  fonksiyonuna yollar hataları listeler


def PdfReader(_files):
    pdfFileObj = open(_files, 'rb')
    pdfReader = PdfFileReader(pdfFileObj)
    i = pdfReader.numPages
    data5 = Font(_files)
    with open("font.txt", "w", encoding="utf-8") as file:
        for item in data5:
            file.write(str(item) + "\n")
        file.write("---------------------------------------\n")
    file.close()
    pdfFileObj.close()


def About(files):
    with open(files, "rb") as file:
        reader = PdfFileReader(file)
        info = reader.getDocumentInfo()
        with open("info.txt", "w", encoding="utf-8") as _file:
            _file.write("---------------------------------------")
            _file.write("\nDosya Hakkında\n")
            _file.write("yazar: "+info.author+"\n")
            _file.write("Program aracı : "+info.creator+"\n")
            _file.write("üretici: "+info.producer+"\n")
            _file.write("Sayfa sayısı: "+str(reader.getNumPages())+"\n")
        _file.close()
    file.close()


def run():
    _files = listdir(".")
    _file = ""
    for file in _files:
        if file.endswith(".pdf"):
            _file = file
            break
    # ImageExtractPath(_file)
    PdfReader(_file)
    Tables(_file)
    Header(_file)
    About(_file)
    HeaderControl()
    sonuclar()
    print("işlemlerimiz tamamlandı")
    sleep(1)
    exit()


def control():
    _files = listdir(".")
    _file = ""
    for file in _files:
        if file.endswith(".docx") or file.endswith(".pdf"):
            _file = file
            break
    return _file


page = """
                 *************  **********  ***********
                      ***       **                  **
                      ***       *****             **
                      ***       **             **
                      ***       **********    ***********

                     Tez Control Sistemine Hosteled
                            Sürüm 12.08.2020645198
                                                                Software Engineer Ümit KOÇ

    Not:Tez Sistemine başlatabilmemiz için lütfen word dosyanızı belirli bir klasöre yerleştiriniz.
                                [E]=e,      [H]=h

    """


def main():
    while True:
        print(page)
        answer = input("listede .docx veya .pdf uzantılı dosyanız kontrol edilsin mi?")
        if answer.lower() == "e":
            files = control()
            if files != "":
                while True:
                    print("Analiz edilecek dosya  :        "+files+"        ")
                    sleep(2)
                    print("""
                                1-resimleri ayrıştıracak
                                2-tabloları ayrıştıracak
                                3-kullanılmış yazı tipleri listelenecektir
                                4-dokuman hakkında bilgileri listelenecektir
                                6-Hataları dosyaya yazdırılacaktır
                                """)
                    sleep(1)
                    answer = input("işlem başlatılsın mı?")
                    if answer.lower() == "e":
                        if not files.endswith(".pdf"):
                            print(files)
                            convert(files)
                            sleep(1)
                        run()
                    elif answer.lower() == "h":
                        print("iyi günler...")
                        sleep(2)
                        exit()
                    else:
                        print("hatalı komut verdiniz tekrar deneyiniz ☻")

        elif answer.lower() == "h":
            print("iyi günler...")
            sleep(2)
            exit()
        else:
            print("hatalı komut verdiniz tekrar deneyiniz ☻")


if __name__ == "__main__":
    main()
