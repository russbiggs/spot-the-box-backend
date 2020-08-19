# Spot the Box Serverless API


## About

Backend service for the [Spot the Box](https://spot-the-box.us). Frontend repo [here](https://github.com/russbiggs/spot-the-box).

## Usage

A simple REST API to receive form input, and return everything stored.
* `curl -X POST https://khab7rvd6c.execute-api.us-east-1.amazonaws.com/dev/mailbox --data '{"status":"present","outlet":"1"}`
* `curl -X GET https://khab7rvd6c.execute-api.us-east-1.amazonaws.com/dev/mailbox`

