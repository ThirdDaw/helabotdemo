import PyPDF2
import PyPDF2 as p2
from PIL import Image
import scrapper.Scraping.Data


class Pdf:

    def __init__(self, path):
        self.path = path
        self.page = ''
        self.file = ''
        self.pdf_file = p2


    def get_page(self, page):  # Return page txt

        pdfReader = p2.PdfFileReader(self.path)
        pg = pdfReader.getPage(page)
        string = pg.extractText()
        ch_string = string.replace("\n", "")
        ch_string1 = ch_string.replace(":", "")
        return ch_string1

    def get_full_pdf(self):  # Getting full SDS PDF as txt file
        PDFfile = open(self.path, "rb")
        self.pdf_file = p2.PdfFileReader(PDFfile)
        number_of_page = self.pdf_file.getNumPages()  # Number of pages
        string = ""
        for page in range(number_of_page):
            pageObj = self.pdf_file.getPage(page)  # Get pages
            string = string + str(pageObj.extractText())

        PDFfile.close()
        ch_string = string.replace("\n", "").replace(")","<right>").replace("(","<left>")
        ch_string = ch_string+" END"
        return ch_string


    def get_images(self, num_page):

        pdf_reader = PyPDF2.PdfFileReader(self.pdf_file)

        # extracting images from the 1st page
        page0 = pdf_reader.getPage(num_page)

        if '/XObject' in page0['/Resources']:
            xObject = page0['/Resources']['/XObject'].getObject()

            for obj in xObject:
                if xObject[obj]['/Subtype'] == '/Image':
                    size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                    data = xObject[obj].getData()
                    if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                        mode = "RGB"
                    else:
                        mode = "P"

                    if '/Filter' in xObject[obj]:
                        if xObject[obj]['/Filter'] == '/FlateDecode':
                            img = Image.frombytes(mode, size, data)
                            img.save(obj[1:] + ".png")
                        elif xObject[obj]['/Filter'] == '/DCTDecode':
                            img = open(obj[1:] + ".jpg", "wb")
                            img.write(data)
                            img.close()
                        elif xObject[obj]['/Filter'] == '/JPXDecode':
                            img = open(obj[1:] + ".jp2", "wb")
                            img.write(data)
                            img.close()
                        elif xObject[obj]['/Filter'] == '/CCITTFaxDecode':
                            img = open(obj[1:] + ".tiff", "wb")
                            img.write(data)
                            img.close()
                    else:
                        img = Image.frombytes(mode, size, data)
                        img.save(obj[1:] + ".png")
        else:
            print("No image found.")
