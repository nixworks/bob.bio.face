import bob.bio.face

preprocessor = bob.bio.face.preprocessor.HistogramEqualization(
  face_cropper = 'face-crop-eyes'
)
