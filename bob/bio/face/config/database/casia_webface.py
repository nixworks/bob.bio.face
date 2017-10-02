#!/usr/bin/env python

from bob.bio.face.database import CasiaWebFaceBioDatabase

casia_webface_directory = "[YOUR_CASIA_WEBFACE_DIRECTORY]"

database = CasiaWebFaceBioDatabase(
  original_directory=casia_webface_directory,
  protocol='pure_casia'
)
