import base64
import numpy as np
from PIL import Image
import io
import matplotlib.pyplot as plt


def base64_to_numpy(base64_string):
    decoded = base64.b64decode(base64_string)
    img = Image.open(io.BytesIO(decoded))
    numpy_img = np.array(img)

    img_gray = numpy_img[:,:,3]
    img_gray_norm = img_gray / 255.0

    img_gray_norm_batch = np.expand_dims(img_gray_norm, 0)

    # plt.imshow(img_gray_norm_batch[0, :, :])
    # plt.colorbar()
    # plt.show()

    return img_gray_norm_batch