from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from myapp.forms import EmployeeForm


class EmployeeImageUploadTests(TestCase):
    def test_employee_form_accepts_image_file(self):
        form = EmployeeForm(
            {
                'eid': 'E-101',
                'ename': 'Alice',
                'eemail': 'alice@example.com',
                'econtact': '1234567890',
            },
            {
                'eimage': SimpleUploadedFile(
                    'avatar.png',
                    b'fake-image-data',
                    content_type='image/png',
                )
            },
        )

        self.assertTrue(form.is_valid(), form.errors)
        self.assertIn('eimage', form.fields)
