# Personal Firewall

A Python-based personal firewall and network security monitoring system designed to capture network traffic, evaluate firewall rules, track TCP connection states, log security events, detect suspicious activity, and provide a terminal-based security dashboard.

## Overview

Personal Firewall is a cybersecurity portfolio project focused on understanding how network traffic can be captured, analyzed, filtered, logged, and monitored from a defensive security perspective.

The system combines firewall traffic processing with security monitoring and alert detection capabilities.

The current implementation operates through the terminal and demonstrates practical concepts involving networking, packet filtering, traffic analysis, logging, detection logic, and security monitoring.

## Key Features

* Network packet capture
* Firewall rule evaluation
* Allow/block traffic decisions
* TCP connection state tracking
* Connection security validation
* Structured firewall event logging
* Excessive blocked-traffic detection
* Repeated blocked-source detection
* Repeated blocked-destination detection
* TCP port-scan detection
* Duplicate alert prevention
* Continuous security monitoring
* Terminal-based security dashboard
* Command-line interface
* Component-level testing
* End-to-end security validation

## Security Detection

The monitoring system currently detects several suspicious traffic patterns.

### Excessive Blocks

Detects when the number of blocked firewall events reaches the configured threshold.

### Repeated Blocked Source

Identifies source IP addresses that repeatedly generate blocked traffic.

### Repeated Blocked Destination

Identifies destination IP addresses that repeatedly appear in blocked traffic.

### TCP Port Scan

Identifies a source attempting connections to multiple different blocked TCP destination ports.

A port-scan alert represents a detected traffic pattern and does not by itself confirm malicious activity.

## Architecture

```text
                 Network Traffic
                       |
                       v
                +--------------+
                | Packet       |
                | Capture      |
                +------+-------+
                       |
                       v
                +--------------+
                | Traffic      |
                | Processing    |
                +------+-------+
                       |
                       v
                +--------------+
                | Firewall     |
                | Rules        |
                +------+-------+
                       |
                 +-----+-----+
                 |           |
              ALLOW         BLOCK
                 |           |
                 +-----+-----+
                       |
                       v
                +--------------+
                | Event        |
                | Logging      |
                +------+-------+
                       |
                       v
                +--------------+
                | Security     |
                | Monitoring   |
                +------+-------+
                       |
                       v
                +--------------+
                | Alert        |
                | Detection    |
                +------+-------+
                       |
                       v
                +--------------+
                | Alert        |
                | Management   |
                +------+-------+
                       |
                 +-----+-----+
                 |           |
                 v           v
          Alert Reporting  Dashboard
```

## Project Structure

```text
Personal-Firewall/
│
├── backends/
│   └── Firewall backend components
│
├── capture/
│   └── Network packet capture components
│
├── cli/
│   └── Command-line interface
│
├── config/
│   └── Firewall and monitoring configuration
│
├── core/
│   ├── firewall.py
│   ├── alert_detector.py
│   ├── alert_logger.py
│   ├── alert_manager.py
│   ├── alert_reporter.py
│   ├── dashboard.py
│   ├── log_analyzer.py
│   ├── monitor_engine.py
│   └── security_monitor.py
│
├── tests/
│   ├── test_alert_detector.py
│   ├── test_alert_manager.py
│   ├── test_connection_security.py
│   ├── test_connection_states.py
│   ├── test_end_to_end.py
│   ├── test_firewall_pipeline.py
│   ├── test_monitor_engine.py
│   ├── test_port_scan.py
│   ├── test_security_monitor.py
│   └── test_tcp_states.py
│
├── logs/
│   └── Runtime firewall and alert logs
│
├── docs/
│   └── Project documentation
│
├── .gitignore
├── main.py
├── monitor.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```powershell
git clone https://github.com/divakar-45/PersonalFirewall.git
cd PersonalFirewall
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the project:

```powershell
python -m pip install -e .
```

This installs the project and makes the `firewall` command available inside the virtual environment.

## Command-Line Usage

Display available commands:

```powershell
firewall --help
```

### Check Firewall Status

```powershell
firewall status
```

Displays the current firewall system status, loaded rules, monitoring availability, dashboard availability, and logging status.

### Start Traffic Processing

Capture and process network traffic:

```powershell
firewall start --count 10
```

The `--count` option controls the number of packets processed.

Example:

```powershell
firewall start --count 5
```

### Security Monitoring

Start the continuous security monitoring engine:

```powershell
firewall monitor
```

The monitor continuously checks the firewall log for new events and evaluates them for suspicious activity.

Press `Ctrl+C` to stop monitoring.

The monitoring interval can be changed:

```powershell
firewall monitor --interval 5
```

A different firewall log can also be specified:

```powershell
firewall monitor --log-file logs/firewall.log
```

### Security Dashboard

Display the security dashboard:

```powershell
firewall dashboard
```

The dashboard provides traffic statistics and detected security alerts.

## Example Dashboard

```text
==================================================
             FIREWALL SECURITY DASHBOARD
==================================================

TRAFFIC OVERVIEW
--------------------------------------------------
Total Events: 142
Allowed: 64
Blocked: 78

DIRECTION
--------------------------------------------------
OUTBOUND: 80
INBOUND: 62

PROTOCOLS
--------------------------------------------------
TCP: 89
UDP: 52

SECURITY ALERTS
--------------------------------------------------
Alerts Detected: 9
MEDIUM: 6
HIGH: 3
```

## TCP Connection Tracking

The project includes TCP connection-state handling.

Example state transitions:

```text
SYN       -> SYN_SENT
SYN-ACK   -> SYN_RECEIVED
ACK       -> ESTABLISHED
DATA      -> ESTABLISHED
FIN       -> CLOSED
```

The connection tracking component helps the firewall reason about TCP traffic based on connection state rather than treating every packet as an isolated event.

## Testing

The project contains tests for individual components as well as the complete security pipeline.

Run the port-scan detection test:

```powershell
python -m tests.test_port_scan
```

Run TCP state tests:

```powershell
python -m tests.test_tcp_states
python -m tests.test_connection_states
python -m tests.test_connection_security
```

Run firewall pipeline validation:

```powershell
python -m tests.test_firewall_pipeline
```

Run alert detection and management tests:

```powershell
python -m tests.test_alert_detector
python -m tests.test_alert_manager
```

Run security monitoring tests:

```powershell
python -m tests.test_security_monitor
python -m tests.test_monitor_engine
```

Run the complete end-to-end test:

```powershell
python -m tests.test_end_to_end
```

Python compilation can also be checked with:

```powershell
python -m compileall core config capture cli
```

## Security Model

The project currently implements user-space firewall decision logic and security monitoring.

Captured traffic is processed by the project, evaluated against configured rules, and assigned an `ALLOW` or `BLOCK` decision. Events are then logged and analyzed by the security monitoring components.

The current implementation should not be considered a replacement for the Windows operating-system firewall or a production network firewall.

## Future Scope

Future development can include:

* OS-level packet enforcement
* Windows Filtering Platform integration
* Linux firewall backend integration
* Cross-platform firewall backends
* Advanced traffic correlation
* Context-aware alert severity
* More sophisticated port-scan analysis
* Application-aware filtering
* Persistent background service
* Graphical user interface
* Configuration management interface
* Expanded security analytics
* Additional detection techniques
* Improved deployment and installation experience

## Project Goal

The goal of this project is to build a practical understanding of defensive network security by implementing the major stages of a firewall and security monitoring pipeline:

```text
Capture
   ↓
Parse
   ↓
Analyze
   ↓
Evaluate Rules
   ↓
ALLOW / BLOCK
   ↓
Log
   ↓
Detect
   ↓
Alert
   ↓
Monitor
   ↓
Report
```

This project is part of my cybersecurity portfolio and focuses on practical implementation of networking and defensive security concepts using Python.


