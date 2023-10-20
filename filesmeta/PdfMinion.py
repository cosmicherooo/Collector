from PyPDF2 import PdfReader

class PdfMinion:

    ex = ['pdf']

    def get_meta_inf(self, path):
        try:
            pdf_reader = PdfReader(path)

            pdf_data = {
                "Title": [pdf_reader.metadata['/Title']],
                "Author": [pdf_reader.metadata['/Producer']],
                "Pages": [len(pdf_reader.pages)],
                        }

            return pdf_data

        except:
            print(f"{path} is broken and cannot be read!")
            return None
