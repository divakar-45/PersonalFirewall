\# Personal Firewall



A Python-based personal firewall and network security monitoring system designed to capture network traffic, evaluate firewall rules, track TCP connection states, log security events, detect suspicious activity, and provide a terminal-based security dashboard.



\## Overview



Personal Firewall is a cybersecurity portfolio project focused on understanding how network traffic can be captured, analyzed, filtered, logged, and monitored from a defensive security perspective.



The system combines firewall traffic processing with security monitoring and alert detection capabilities.



The current implementation operates through the terminal and is designed as a practical cybersecurity project demonstrating networking, packet filtering, logging, detection logic, and security monitoring concepts.



\## Key Features



\* Network packet capture

\* Firewall rule evaluation

\* Allow/block traffic decisions

\* TCP connection state tracking

\* Connection security validation

\* Structured firewall event logging

\* Excessive blocked-traffic detection

\* Repeated blocked-source detection

\* Repeated blocked-destination detection

\* TCP port-scan detection

\* Duplicate alert prevention

\* Security monitoring

\* Terminal-based security dashboard

\* Command-line interface

\* Component-level testing

\* End-to-end security validation



\## Security Detection



The monitoring system currently detects several suspicious traffic patterns.



\### Excessive Blocks



Detects when the number of blocked firewall events reaches the configured threshold.



\### Repeated Blocked Source



Identifies source IP addresses that repeatedly generate blocked traffic.



\### Repeated Blocked Destination



Identifies destination IP addresses that repeatedly appear in blocked traffic.



\### TCP Port Scan



Identifies a source attempting connections to multiple different blocked TCP destination ports.



\## Architecture



```text

&#x20;                Network Traffic

&#x20;                      |

&#x20;                      v

&#x20;               +--------------+

&#x20;               | Packet       |

&#x20;               | Capture      |

&#x20;               +------+-------+

&#x20;                      |

&#x20;                      v

&#x20;               +--------------+

&#x20;               | Traffic      |

&#x20;               | Processing   |

&#x20;               +------+-------+

&#x20;                      |

&#x20;                      v

&#x20;               +--------------+

&#x20;               | Firewall     |

&#x20;               | Rules        |

&#x20;               +------+-------+

&#x20;                      |

&#x20;                +-----+-----+

&#x20;                |           |

&#x20;             ALLOW         BLOCK

&#x20;                |           |

&#x20;                +-----+-----+

&#x20;                      |

&#x20;                      v

&#x20;               +--------------+

&#x20;               | Event        |

&#x20;               | Logging      |

&#x20;               +------+-------+

&#x20;                      |

&#x20;                      v

&#x20;               +--------------+

&#x20;               | Security     |

&#x20;               | Monitoring   |

&#x20;               +------+-------+

&#x20;                      |

&#x20;                      v

&#x20;               +--------------+

&#x20;               | Alert        |

&#x20;               | Detection    |

&#x20;               +------+-------+

&#x20;                      |

&#x20;                      v

&#x20;               +--------------+

&#x20;               | Alert        |

&#x20;               | Management   |

&#x20;               +------+-------+

&#x20;                      |

&#x20;                +-----+-----+

&#x20;                |           |

&#x20;                v           v

&#x20;         Alert Reporting  Dashboard

```



\## Project Structure



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

│   ├── alert\_detector.py

│   ├── alert\_logger.py

│   ├── alert\_manager.py

│   ├── alert\_reporter.py

│   ├── dashboard.py

│   ├── log\_analyzer.py

│   ├── monitor\_engine.py

│   └── security\_monitor.py

│

├── tests/

│   ├── test\_alert\_detector.py

│   ├── test\_alert\_manager.py

│   ├── test\_connection\_security.py

│   ├── test\_connection\_states.py

│   ├── test\_end\_to\_end.py

│   ├── test\_firewall\_pipeline.py

│   ├── test\_monitor\_engine.py

│   ├── test\_port\_scan.py

│   ├── test\_security\_monitor.py

│   └── test\_tcp\_states.py

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

└── README.md

```



\## Installation



Clone the repository and enter the project directory.



Create a virtual environment:



```powershell

python -m venv .venv

```



Activate it on Windows:



```powershell

.venv\\Scripts\\Activate.ps1

```



Install the required dependencies:



```powershell

pip install -r requirements.txt

```



\## Usage



The project provides a command-line interface.



Display available commands:



```powershell

python -m cli.main --help

```



\### Firewall



Capture and process network traffic:



```powershell

python -m cli.main firewall --count 5

```



\### Security Monitor



Start the security monitoring engine:



```powershell

python -m cli.main monitor

```



Press `Ctrl+C` to stop the monitor.



\### Dashboard



Display the firewall security dashboard:



```powershell

python -m cli.main dashboard

```



\## Example Dashboard



```text

==================================================

&#x20;            FIREWALL SECURITY DASHBOARD

==================================================



TRAFFIC OVERVIEW

\--------------------------------------------------

Total Events: 142

Allowed: 64

Blocked: 78



DIRECTION

\--------------------------------------------------

OUTBOUND: 80

INBOUND: 62



PROTOCOLS

\--------------------------------------------------

TCP: 89

UDP: 52



SECURITY ALERTS

\--------------------------------------------------

Alerts Detected: 9

MEDIUM: 6

HIGH: 3

```



\## TCP Connection Tracking



The project includes TCP connection-state handling.



Example state transitions:



```text

SYN       -> SYN\_SENT

SYN-ACK   -> SYN\_RECEIVED

ACK       -> ESTABLISHED

DATA      -> ESTABLISHED

FIN       -> CLOSED

```



\## Testing



The project contains tests for individual components as well as the complete security pipeline.



Run the main tests with:



```powershell

python -m tests.test\_port\_scan

python -m tests.test\_tcp\_states

python -m tests.test\_connection\_states

python -m tests.test\_connection\_security

python -m tests.test\_firewall\_pipeline

python -m tests.test\_alert\_detector

python -m tests.test\_alert\_manager

python -m tests.test\_security\_monitor

python -m tests.test\_monitor\_engine

python -m tests.test\_end\_to\_end

```



Python compilation can also be checked with:



```powershell

python -m compileall core config capture cli tests

```



The completed project has successfully passed the implemented component tests and the end-to-end security validation.



\## Current Status



The current terminal-based firewall and security monitoring implementation is complete and demonstrable.



The project currently demonstrates practical implementation of:



\* Network packet capture

\* Firewall rule processing

\* Packet filtering

\* TCP connection-state tracking

\* Security event logging

\* Security alert detection

\* Port-scan detection

\* Duplicate alert prevention

\* Continuous monitoring

\* Terminal-based security reporting

\* Command-line operation

\* End-to-end validation



\## Future Scope



The following capabilities are reserved for future development:



\* Advanced security investigation

\* Event correlation

\* Incident investigation workflows

\* More sophisticated threat detection

\* Additional behavioral detection rules

\* Threat-intelligence integration

\* SIEM integration

\* Centralized security logging

\* Advanced reporting and visualization

\* Automated incident response

\* Web-based dashboard

\* Desktop/application interface

\* Cross-platform firewall integration

\* Authentication and access control

\* Production-oriented deployment



These capabilities are future scope and are not represented as implemented functionality in the current project.



\## Security Disclaimer



This project is intended for educational, research, and portfolio demonstration purposes.



Network packet capture and firewall functionality should only be used on systems and networks where you have appropriate authorization.



\## Author



\*\*Divakar Pathak\*\*



Cybersecurity-focused BCA student building practical projects around networking, defensive security, security monitoring, and SOC-oriented technologies.



\## License



This project is licensed under the MIT License.



