#!/usr/bin/env python
"""Test backend after argon2-cffi fix."""
import time
import requests
import random

base = 'https://biomatricverificationfingerprint-4.onrender.com'

print('Waiting 60 seconds for Render to deploy argon2-cffi fix...')
time.sleep(60)

print('\n' + '='*70)
print('TEST 1: Admin Login')
print('='*70)

try:
    r = requests.post(
        f'{base}/api/auth/admin/login',
        json={'username': 'admin', 'password': 'admin123'},
        timeout=15
    )
    print(f'Status: {r.status_code}')
    if r.status_code == 200:
        print('✓ SUCCESS - Admin login working!')
        data = r.json()
        token = data.get('access_token', '')[:50]
        print(f'Token: {token}...')
    else:
        print(f'✗ FAILED: {r.text[:300]}')
except Exception as e:
    print(f'✗ ERROR: {e}')

print('\n' + '='*70)
print('TEST 2: Student Register')
print('='*70)

try:
    r = requests.post(
        f'{base}/api/auth/student/register',
        json={
            'roll_number': f'TEST{random.randint(10000, 99999)}',
            'full_name': 'Test User',
            'email': f'test{random.randint(1000, 9999)}@test.com',
            'phone': '9999999999',
            'department': 'CS',
            'semester': 1,
            'password': 'Test123Pass'
        },
        timeout=15
    )
    print(f'Status: {r.status_code}')
    if r.status_code == 200:
        print('✓ SUCCESS - Student registration working!')
        data = r.json()
        print(f'Student ID: {data.get("student_id", "N/A")}')
    else:
        print(f'✗ FAILED: {r.text[:300]}')
except Exception as e:
    print(f'✗ ERROR: {e}')

print('\n' + '='*70)
