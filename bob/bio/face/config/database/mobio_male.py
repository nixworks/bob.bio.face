#!/usr/bin/env python

from bob.bio.db import MobioBioDatabase

mobio_image_directory = "[YOUR_MOBIO_IMAGE_DIRECTORY]"
mobio_annotation_directory = "[YOUR_MOBIO_ANNOTATION_DIRECTORY]"

database = MobioBioDatabase(
    original_directory=mobio_image_directory,
    original_extension=".png",
    annotation_directory=mobio_annotation_directory,

    protocol='male',
    models_depend_on_protocol = True,

    all_files_options={'gender': 'male'},
    extractor_training_options={'gender': 'male'},
    projector_training_options={'gender': 'male'},
    enroller_training_options={'gender': 'male'},
    z_probe_options={'gender': 'male'}
)

