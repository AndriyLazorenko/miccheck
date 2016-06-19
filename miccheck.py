import os

from flask import Flask, jsonify, render_template, request
# from flask_uwsgi_websocket import GeventWebSocket

app = Flask(__name__)
# ws = GeventWebSocket(app)

# @ws.route('/websocket')
# def audio(ws):
#    first_message = True
#    total_msg = ""
#    sample_rate = 0
#
#    while True:
#       msg = ws.receive()
#
#       if first_message and msg is not None: # the first message should be the sample rate
#          sample_rate = getSampleRate(msg)
#          first_message = False
#          continue
#       elif msg is not None:
#          audio_as_int_array = numpy.frombuffer(msg, 'i2')
#          doSomething(audio_as_int_array)
#       else:
#          break

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
