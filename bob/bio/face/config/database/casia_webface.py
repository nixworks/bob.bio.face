#!/usr/bin/env python

from bob.bio.face.database import CasiaWebFaceBioDatabase

casia_image_directory = "[YOUR_CASIA_WEBFACE_IMAGE_DIRECTORY]"

database = CasiaWebFaceBioDatabase(
    original_directory=casia_image_directory,
    original_extension=".png",

    protocol='pure_casia',
    models_depend_on_protocol=True,
)

