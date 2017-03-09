import io
from asciify.tasks import image_to_ascii

from sanic import Sanic
from sanic.response import json, text
from sanic.log import log

app = Sanic(__name__)


@app.route('/')
async def home(request):
    ret  = {"status": "success"}
    return json(ret)


@app.post('/art')
async def art(request):

    if 'file' not in request.files:
        ret = {'status': 'error', 'message': 'No file present in request'}
        return json(ret)
    else:
        image = request.files.get('file')
        img = io.BytesIO(image.body)

        kwargs = {
            'scale': request.args.get('scale'),
            'factor': request.args.get('factor'),
            'max_height': request.args.get('max_height'),
        }
        art = image_to_ascii(img, **kwargs)

        if request.args.get('format') == 'text':
            return text(art)
        else:
            ret  = {'status': 'success', 'name': image.name, 'art': art}
            return json(ret)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
