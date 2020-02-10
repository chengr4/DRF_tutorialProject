import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc5NTEwNjg1LCJqdGkiOiI0NjU4YzJmYjJkMWU0MDQxODMwZjQxMjY5MjQ4NTUzMyIsInVzZXJfaWQiOjF9.9vuYxqqoiY0Uf1GK0tkOn--pWYld9zUlgQzIZ93nbAk'

r = requests.get('http://127.0.0.1:8000/paradigms', headers = headers)

print(r.text)