#!/usr/bin/env python
"""
Simple test script to verify patient deletion functionality
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'makimotion.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from core.models import Patient
from django.urls import reverse

def test_patient_delete():
    # Get test user and patient
    try:
        user = User.objects.get(username='testuser')
        patient = Patient.objects.get(user=user, full_name='Juan Pérez')
        
        print(f"Found user: {user.username}")
        print(f"Found patient: {patient.full_name} (ID: {patient.id})")
        
        # Create test client
        client = Client()
        
        # Login
        login_success = client.login(username='testuser', password='testpass123')
        print(f"Login successful: {login_success}")
        
        if login_success:
            # Test GET request to delete confirmation page
            delete_url = reverse('patient_delete', args=[patient.id])
            print(f"Delete URL: {delete_url}")
            
            response = client.get(delete_url)
            print(f"GET response status: {response.status_code}")
            
            if response.status_code == 200:
                print("✅ Delete confirmation page loads successfully")
                
                # Test POST request to actually delete
                response = client.post(delete_url)
                print(f"POST response status: {response.status_code}")
                
                if response.status_code == 302:  # Redirect after successful delete
                    print("✅ Delete POST request successful (redirected)")
                    
                    # Check if patient was actually deleted
                    try:
                        Patient.objects.get(id=patient.id)
                        print("❌ Patient still exists after delete")
                    except Patient.DoesNotExist:
                        print("✅ Patient successfully deleted")
                else:
                    print(f"❌ Delete POST failed with status {response.status_code}")
            else:
                print(f"❌ Delete confirmation page failed with status {response.status_code}")
        else:
            print("❌ Login failed")
            
    except User.DoesNotExist:
        print("❌ Test user not found")
    except Patient.DoesNotExist:
        print("❌ Test patient not found")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    test_patient_delete()