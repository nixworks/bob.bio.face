#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Manuel Guenther <Manuel.Guenther@idiap.ch>
# @date: Thu May 24 10:41:42 CEST 2012
#
# Copyright (C) 2011-2012 Idiap Research Institute, Martigny, Switzerland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import bob.ip.base

import numpy
from .Base import Base
from .utils import load_cropper
from bob.bio.base.preprocessor import Preprocessor

class INormLBP (Base):
  """Performs I-Norm LBP on the given image"""

  def __init__(
      self,
      face_cropper,
      radius = 2,  # Radius of the LBP
      is_circular = True, # use circular LBP?
      compare_to_average = False,
      elbp_type = 'regular',
      **kwargs
  ):

    """Parameters of the constructor of this preprocessor:

    face_cropper : str or `bob.bio.face.preprocessor.FaceCrop` or `bob.bio.face.preprocessor.FaceDetect`
      The face image cropper that should be applied to the image.
      It might be specified as a registered resource, a configuration file, or an instance of a preprocessor.

      .. note:: The given class needs to contain a ``crop_face`` method.

    radius : int
      The radius of the LBP features to extract

    is_circular : bool
      Whether to extract circular LBP features, or square features

    compare_to_average : bool
      Compare to the average value of all pixels, or to the central one

    elbp_type : str
      The way, LBP features are extracted, see :py:class:`bob.ip.base.LBP` for more details.

    kwargs
      Remaining keyword parameters passed to the :py:class:`Base` constructor, such as ``color_channel`` or ``dtype``.
    """

    # call base class constructors
    Base.__init__(self, **kwargs)

    Preprocessor.__init__(
        self,
        face_cropper = face_cropper,
        radius = radius,
        is_circular = is_circular,
        compare_to_average = compare_to_average,
        elbp_type = elbp_type
    )

    # lbp extraction
    self.lbp_extractor = bob.ip.base.LBP(
        neighbors = 8,
        radius = radius,
        circular = is_circular,
        to_average = compare_to_average,
        add_average_bit = False,
        uniform = False,
        elbp_type = elbp_type,
        border_handling = 'wrap'
    )

    self.cropper = load_cropper(face_cropper)


  def i_norm(self, image):
    """Computes the I-Norm-LBP normalization on the given image"""
    # perform normalization
    return self.lbp_extractor(image)


  def __call__(self, image, annotations = None):
    """Crops the face using the specified face cropper and extracts the LBP features from the given image."""
    image = self.color_channel(image)
    if self.cropper is not None:
      image = self.cropper.crop_face(image, annotations)
    image = self.i_norm(image)
    return self.data_type(image)
