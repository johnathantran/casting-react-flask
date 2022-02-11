import os

# Set environment variables
os.environ['DATABASE_URL'] = 'postgres://jtcgcqaotpgbck:e53001ad10fea4d82db2cda28e53bf85e1b2a8b0ee73b12270378c28dc113f71@ec2-18-235-114-62.compute-1.amazonaws.com:5432/dd2svdj0rf6f1i'
os.environ['EXCITED'] = 'true'

os.environ['AUTH0_DOMAIN'] = 'dev-rpk21ij6.us.auth0.com"'
os.environ['API_AUDIENCE'] = 'casting'
os.environ['AUTH0_CALLBACK_URL'] = 'http://localhost:3000/'
os.environ['AUTH0_LOGIN_URL'] = 'http://localhost:3000/'
os.environ['AUTH0_LOGOUT_URL'] = 'http://localhost:3000/'

os.environ['producer_token'] = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlljTHNYanJFc1RhV2pwQV82S1RoMyJ9.eyJpc3MiOiJodHRwczovL2Rldi1ycGsyMWlqNi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjIwNGMzMGY3ZjI3OWIwMDZjZDliNDczIiwiYXVkIjpbImNhc3RpbmciLCJodHRwczovL2Rldi1ycGsyMWlqNi51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjQ0NTMwODAzLCJleHAiOjE2NDQ2MTcyMDMsImF6cCI6IndqQUVjMzlaeUI1Z0hFdTVHWW9hQkg5S1I3V0Z4NkhCIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.b98CVQP1swdpf3qgkfxi6rMZIBOnS7BfB9RVyZkURp58njRGX4xFOIeGzTh7VrhHmNkz7YoU2-2emQc_VFLDlZYMlJ1V6rrmk_RaA-fsyT5ey0rnOYal4mr2Ne7qzsVFRQNo2O5azN1OOodJqIsKIw-H28WtwxKNIm3uR1FTUpGG7YbzSpppFgJgZd0pSkXoOcoENNWVYMNeYF37xfseemY9h-Mpjx_3Uodzxym3R-jPG8Bck130bNaNxmOKhpe_nS0WF2KG4VeENdcRJejkoiQJiPILfHKJvJ_-8T-nLevDgy7D15Wpr6tNVfIlKbSSTi-92h5MbnyfkW4m9MF0Ag'
os.environ['PASSWORD'] = 'Hien3045'

print("Env variables set!")