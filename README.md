# Nmap Simulation

A Python-based simulation of the core functionalities of Nmap using socket programming.

This project demonstrates the implementation of fundamental network scanning techniques, including host discovery, port scanning, service detection, latency measurement, and simple client-server communication.

## Overview

The goal of this project is to simulate several core features of the Nmap network scanner to better understand how network reconnaissance tools work internally.

Rather than relying on external libraries, the scanner is implemented using Python sockets and standard networking concepts.

## Features

* Host availability detection
* TCP port scanning
* Open port discovery
* Service identification
* Port response latency measurement
* Custom GET request handling
* Custom POST request handling
* Interactive command-line interface


## Implemented Functionalities

### Host Discovery

Determines whether a target host is online by attempting TCP connections.

### Port Scanning

Scans a user-defined range of ports and identifies which ports are open.

### Service Detection

Maps open ports to their corresponding standard services using Python's socket library.

### Latency Measurement

Measures the average response time of a selected port over multiple connection attempts.

### Custom Request Handling

Implements simple GET and POST request communication using TCP sockets.


## How to Run

Run the program:

```bash
python scanner.py
```

Example:

```text
Enter IP: 127.0.0.1
Enter start port: 1
Enter end port: 1024
```

## Available Operations

* Check whether a host is online
* Scan open ports
* Detect common services
* Measure port latency
* Send custom GET requests
* Send custom POST requests
