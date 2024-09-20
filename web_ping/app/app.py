#!/usr/bin/env python3
import subprocess
import ipaddress
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'OPTIONS'])
def ping():
    user_supplied_IP = request.args.get('IP', '')
    try:
        myIPaddress = ipaddress.ip_address(user_supplied_IP)
    except ValueError:
        custom_error_msg = 'You supplied an invalid IP address'
        return render_template('index.html', result=custom_error_msg)

    command_to_execute = f'ping -c 2 {myIPaddress}'
    print(command_to_execute, flush=True)
    try:
        results = subprocess.check_output(['/bin/sh', '-c', command_to_execute], timeout=8)
        return render_template('index.html', result=results.decode('utf-8'))
    except subprocess.TimeoutExpired:
        custom_error_msg = 'Request Timed Out!'
        return render_template('index.html', result=custom_error_msg)
    except subprocess.CalledProcessError:
        custom_error_msg = 'An error occured'
        return render_template('index.html', result=custom_error_msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
