from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


def rescale_image(self, img):
    # Opening the uploaded image
    size = (128, 128)
    im = Image.open(img)

    output = BytesIO()

    # Resize/modify the image
    im = im.resize((650, 350))

    # after modifications, save it to the output
    im.save(output, format='JPEG', quality=100)
    output.seek(0)

    im = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.service_image1.name.split('.')[
        0], 'image/jpeg', sys.getsizeof(output), None)

    return im
