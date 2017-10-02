#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

"""
  CasiaWebFace database implementation of bob.bio.base.database.BioDatabase interface.
  It is an extension of the database interface, which directly talks to CasiaWebFace database, for
  verification experiments (good to use in bob.bio.base framework).
"""

from .database import FaceBioFile
from bob.bio.base.database import BioDatabase, BioFileSet
import os


class CasiaWebFaceBioFile(FaceBioFile):
  def __init__(self, f):
    super(CasiaWebFaceBioFile, self).__init__(client_id=f.client_id, path=f.path, file_id=f.id)
    self.f = f

  def make_path(self, directory, extension):
    # add file ID to the path, so that a unique path is generated (there might be several identities in each physical file)
    return str(os.path.join(directory or '', self.path + "-" + str(self.client_id) + (extension or '')))


class CasiaWebFaceBioDatabase(BioDatabase):
  """
    CasiaWebFace database implementation of :py:class:`bob.bio.base.database.BioDatabase` interface.
    It is an extension of an SQL-based database interface, which directly talks to CasiaWebFace database, for
    verification experiments (good to use in bob.bio.base framework).
  """

  def __init__(
      self,
      original_directory=None,
      annotations_directory=None,
      lfw_directory=None,
      original_extension=None,
      **kwargs
  ):
    # call base class constructors to open a session to the database
    super(CasiaWebFaceBioDatabase, self).__init__(
            name='casia-webface',
            models_depend_on_protocol=False,
            training_depends_on_protocol=False,
            original_directory=original_directory,
            original_extension=original_extension,
            **kwargs)

    from bob.db.casia_webface.query import Database as LowLevelDatabase
    self._db = LowLevelDatabase(original_directory, annotations_directory, original_extension)

  def uses_probe_file_sets(self):
    return False

  def model_ids_with_protocol(self, groups=None, protocol="pure_casia", **kwargs):
    return self._db.model_ids(groups=groups, protocol=protocol)

  def objects(self, groups=None, protocol="pure_casia", purposes=None, model_ids=None, **kwargs):
    return [CasiaWebFaceBioFile(f) for f in self._db.objects(groups=groups, protocol=protocol, purposes=purposes, model_ids=model_ids, **kwargs)]

  def annotations(self, biofile):
    pass

  def client_id_from_model_id(self, model_id, group='dev'):
    return self._db.get_client_id_from_model_id(model_id)
