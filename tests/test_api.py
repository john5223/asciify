from asciify import api
from ujson import loads, dumps
import base64
import io

app = api.app

def test_health():
	request, response = app.test_client.get('/')
	data = loads(response.text)
	assert data == {'status': 'success'}


def dont_test_no_file_given():
	data = {}
	request, response = app.test_client.post('/art', data=dumps(data))
	data = loads(response.text)
	assert data == {'status': 'error', 'message': 'No file present in request'}


def image_payload(image, filename, boundary=None):
	#image = base64.b64encode(image)
	boundary = boundary or '----sanic'
	payload = io.BytesIO()
	payload.write(str.encode('--{}\r\n'.format(boundary)))
	payload.write(str.encode('Content-Disposition: form-data; ' \
				  'name=file; filename="{0}"\r\n\r\n'
				  .format(filename)
				  ))
	payload.write(image)
	payload.write(b'\r\n')
	payload.write(str.encode('--{boundary}--\r\n'.format(boundary=boundary)))
	payload.seek(0)
	return payload, boundary


def test_art():

	image = open('tests/images/earth.png', 'rb').read()

	payload, boundary = image_payload(image, 'earth.png')
	content_type = 'multipart/form-data; boundary={}'.format(boundary)
	headers = {'content-type': content_type}

	request, response = app.test_client.post('/art',
		data=payload,
		headers=headers
	)

	data = loads(response.text)

	assert data['status'] == 'success'
	assert data['name'] == 'earth.png'
