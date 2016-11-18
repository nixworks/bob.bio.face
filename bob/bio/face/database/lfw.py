#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>
# Sat 20 Aug 15:43:10 CEST 2016

"""
  LFW database implementation of bob.bio.base.database.Database interface.
  It is an extension of an SQL-based database interface, which directly talks to LFW database, for
  verification experiments (good to use in bob.bio.base framework).
"""


from .database import FaceBioFileWithAnnotations, FaceBioDatabaseWithAnnotations


class LFWBioDatabase(FaceBioDatabaseWithAnnotations):
  """
  Implements verification API for querying LFW database.
  """

  def __init__(self,**kwargs):
    # call base class constructors to open a session to the database
    from bob.db.lfw.query import Database as LowLevelDatabase
    super(LFWBioDatabase, self).__init__(name='lfw', database = LowLevelDatabase(), **kwargs)


  def model_ids_with_protocol(self, groups=None, protocol=None, **kwargs):
    return self._database.model_ids(groups=groups, protocol=protocol)

  def objects(self, groups=None, protocol=None, purposes=None, model_ids=None, **kwargs):
    retval = self._database.objects(groups=groups, protocol=protocol, purposes=purposes, model_ids=model_ids, **kwargs)
    return [FaceBioFileWithAnnotations(f, client_id=f.client_id) for f in retval]
