from flask import Flask, request, jsonify, session
# from grpc import insecure_channel, ChannelArguments
import grpc
import base64
import api_pb2
import api_pb2_grpc
# from grpc.experimental import (
#     initialize_channel,
#     load_balanced_channel,
#     RoundRobin,
#     HealthCheckServiceStub,
#     healthcheck
# )

app = Flask(__name__)
app.secret_key = 'AABBCCaabbcc'

# channel_args = ChannelArguments()
# channel_args.service_config = '{"loadBalancingPolicy":"round_robin"}'

# channel = insecure_channel(
#     target='colorization-server-service:8080',
#     options=[('grpc.lb_policy_name', 'round_robin')],
#     channel_args=channel_args,
# )

# initialize_channel(channel)
# channel = load_balanced_channel(channel, RoundRobin())

# # Create the gRPC client
channel = grpc.insecure_channel('colorization-server-service:8080')
client = api_pb2_grpc.ImageManipStub(channel)

@app.route('/colorize', methods=['POST'])
def colorize():
    try:
        data = request.get_json()
        request_message = api_pb2.Request(
            op=data['op'],
            image=base64.b64decode(data['image'])
        )
    except KeyError as e:
        return jsonify({'error': f'Missing field: {e}'}), 400
    except base64.binascii.Error as e:
        return jsonify({'error': 'Invalid base64 encoding'}), 400
    try:
        response = client.GetResponse(request_message)
        response_json = {
            'ip': response.Ip,
            'created': str(response.created.seconds),
            'image': base64.b64encode(response.image).decode('utf-8')
        }
        return response_json
    except grpc.RpcError as e:
        return jsonify({'error': str(e)}), 500

@app.after_request
def after_request(response):
    session.clear()  # Clear session after each request
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)