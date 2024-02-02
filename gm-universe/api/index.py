
from flask import Flask, request, send_from_directory, redirect
import os
import io
import json
from sufficient.frames import FrameAppRunner
from frame import app as frame_app


app = Flask(__name__, instance_relative_config=True)

static_dir = os.path.abspath("frame/static")
templates_dir = os.path.abspath("frame/templates")
# data_dir = app.instance_path
data_dir = "/tmp/data"

runner = FrameAppRunner(frame_app, static_dir,
                        templates_dir, data_dir=data_dir)
try:
    os.makedirs(data_dir)
except OSError:
    pass


@app.route('/')
def frame_index():
    framelet = runner.start()
    return runner.gen_frame_html(framelet, request.host_url, og=True)


@app.route('/static/<string:path>')
def frame_static(path):
    return send_from_directory(static_dir, path)


@app.route('/view/<string:path>')
def frame_image(path):
    return send_from_directory(data_dir, path)


@app.route('/<string:page>/click', methods=['POST'])
def frame_click(page):
    tag, value = runner.click(page, request.json)
    if tag == "framelet":
        return runner.gen_frame_html(value, request.host_url)
    elif tag == "redirection":
        return redirect(value, code=302)
