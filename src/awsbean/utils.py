from storages.backends.s3boto import S3BotoStorage


StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static') #bucket name / static 
MediaRootS3BotoStorage  = lambda: S3BotoStorage(location='media') #bucket name / media 
# ProtectedRootS3BotoStorage  = lambda: S3BotoStorage(location='protected') #bucket name / protected 