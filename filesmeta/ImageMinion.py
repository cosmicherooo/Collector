from PIL import Image
from PIL.ExifTags import TAGS

class ImageMinion():

    #exts = Image.registered_extensions()
    # supported_extensions = [ex for ex, f in exts.items() if f in Image.OPEN]
    # print(supported_extensions) -->

    ex = ['.blp', '.bmp', '.dib', '.bufr',
          '.cur', '.pcx', '.dcx', '.dds', '.ps',
          '.eps', '.fit', '.fits', '.fli', '.flc',
          '.ftc', '.ftu', '.gbr', '.gif', '.grib',
          '.h5', '.hdf', '.png', '.apng', '.jp2',
          '.j2k', '.jpc', '.jpf', '.jpx', '.j2c',
          '.icns', '.ico', '.im', '.iim', '.jfif',
          '.jpe', '.jpg', '.jpeg', '.mpg', '.mpeg',
          '.tif', '.tiff', '.msp', '.pcd', '.pxr',
          '.pbm', '.pgm', '.ppm', '.pnm', '.psd',
          '.qoi', '.bw', '.rgb', '.rgba', '.sgi',
          '.ras', '.tga', '.icb', '.vda', '.vst',
          '.webp', '.wmf', '.emf', '.xbm', '.xpm']

    def get_meta_inf(self, path):

        try:

            image_reader = Image.open(path)

            image_data = {
                "Image_height": image_reader.height,
                "Image_width": image_reader.width,
                "Image_format": image_reader.format,
                "Image_mode": image_reader.mode,
                "Image_is_animated": getattr(image_reader, "is_animated", False),
                "Frames_in_image": getattr(image_reader, "n_frames", 1)
            }

            return image_data

        except:
            print(f"{path} is broken and cannot be read!")
            return None
