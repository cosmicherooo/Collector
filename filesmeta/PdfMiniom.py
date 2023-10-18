from PyPDF2 import PdfReader

class PdfMinion():

    ex = ['pdf']

    def get_meta_inf(self, path):
        try:
            reader = PdfReader(path)
            pdf_title = {"Title": reader.metadata['/Title']}
            pdf_producer = {"Producer": reader.metadata['/Producer']}
            pdf_pages = {"Pages": len(reader.pages)}
            pdf_data = {**pdf_title, **pdf_producer, **pdf_pages}

            return pdf_data

        except:
            print(f"{path} is broken and cannot be read!")
            return None
