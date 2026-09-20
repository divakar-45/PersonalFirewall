\# Personal Firewall \& Network Traffic Filtering System



\## Project Overview



Personal Firewall is a Python-based network security project designed to monitor, analyze, and filter network traffic on a host system.



The project captures network packets, converts them into structured traffic events, evaluates those events against firewall rules, tracks connection states, records security events, and detects suspicious traffic patterns.



The current implementation is terminal-based and focuses on the core firewall and security-monitoring functionality.



\## Project Objective



The main objective of this project is to understand and implement the fundamental components of a host-based firewall from a cybersecurity perspective.



The system is designed to:



\- Monitor incoming and outgoing network traffic

\- Capture network packets

\- Parse packet information

\- Apply configurable firewall rules

\- Allow or block traffic

\- Track TCP connection states

\- Record firewall events

\- Detect repeated blocked activity

\- Detect excessive blocked traffic

\- Detect potential TCP port scanning activity

\- Prevent duplicate alert processing

\- Provide a terminal-based security dashboard

\- Provide a command-line interface for interacting with the firewall



\## Cybersecurity Concepts Covered



This project applies practical concepts related to:



\- Network traffic analysis

\- Packet inspection

\- Stateful firewall concepts

\- TCP connection states

\- Packet filtering

\- Inbound and outbound traffic

\- IP addressing

\- TCP and UDP protocols

\- Port-based filtering

\- Security event logging

\- Security alert detection

\- Port scan detection

\- Network security monitoring



\## Current Implementation



The current system provides the following major components:



\### Packet Capture



The packet capture layer collects network packets from the host system using Scapy.



\### Packet Parsing



Captured packets are converted into structured traffic information including:



\- Source IP

\- Destination IP

\- Protocol

\- Source port

\- Destination port

\- Traffic direction

\- TCP flags



\### Firewall Processing



The firewall evaluates traffic against configured rules and produces decisions such as:



\- `ALLOW`

\- `BLOCK`



\### Connection Tracking



TCP traffic is tracked using connection states such as:



\- `SYN\_SENT`

\- `SYN\_RECEIVED`

\- `ESTABLISHED`

\- `CLOSED`



This provides a basic stateful security layer rather than treating every packet independently.



\### Security Monitoring



The security monitoring subsystem analyzes firewall events and detects suspicious patterns.



Current detections include:



\- Excessive blocked traffic

\- Repeated blocked sources

\- Repeated blocked destinations

\- TCP port scanning



\### Alert Management



Detected alerts are given severity levels and stored using an alert-state mechanism to prevent the same alert from being repeatedly processed.



\### Security Dashboard



The terminal dashboard provides information such as:



\- Total events

\- Allowed traffic

\- Blocked traffic

\- Traffic direction

\- Protocol distribution

\- Detected security alerts

\- Recent alerts



\### Command-Line Interface



The project provides a CLI with commands for:



\- Firewall processing

\- Security monitoring

\- Dashboard display



\## Current Project Status



The core terminal-based firewall and security-monitoring system has been implemented and tested.



The project currently demonstrates an end-to-end flow:



```text

Network Traffic

&#x20;     ↓

Packet Capture

&#x20;     ↓

Packet Parsing

&#x20;     ↓

Firewall Rules

&#x20;     ↓

ALLOW / BLOCK

&#x20;     ↓

Event Logging

&#x20;     ↓

Security Monitoring

&#x20;     ↓

Alert Detection

&#x20;     ↓

Security Dashboard

