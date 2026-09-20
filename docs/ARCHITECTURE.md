\# System Architecture



\## 1. Overview



Personal Firewall is a terminal-based network security system designed to monitor network traffic, apply firewall rules, record traffic decisions, and detect suspicious activity.



The project follows a modular architecture so that the core security logic can remain independent from operating-system-specific firewall implementations.



\---



\## 2. High-Level Architecture



```text

&#x20;                   NETWORK TRAFFIC

&#x20;                          |

&#x20;                          v

&#x20;                 +-------------------+

&#x20;                 |  Packet Capture   |

&#x20;                 |     Layer         |

&#x20;                 +-------------------+

&#x20;                          |

&#x20;                          v

&#x20;                 +-------------------+

&#x20;                 |  Packet Parser    |

&#x20;                 +-------------------+

&#x20;                          |

&#x20;                          v

&#x20;                 +-------------------+

&#x20;                 | Traffic Model     |

&#x20;                 +-------------------+

&#x20;                          |

&#x20;                          v

&#x20;                 +-------------------+

&#x20;                 | Firewall Engine   |

&#x20;                 +-------------------+

&#x20;                          |

&#x20;                   +------+------+

&#x20;                   |             |

&#x20;                 ALLOW          BLOCK

&#x20;                   |             |

&#x20;                   +------+------+

&#x20;                          |

&#x20;                          v

&#x20;                 +-------------------+

&#x20;                 |   Event Logger    |

&#x20;                 +-------------------+

&#x20;                          |

&#x20;                          v

&#x20;                 +-------------------+

&#x20;                 |   Log Analyzer    |

&#x20;                 +-------------------+

&#x20;                          |

&#x20;                          v

&#x20;                 +-------------------+

&#x20;                 | Alert Detection   |

&#x20;                 +-------------------+

&#x20;                          |

&#x20;                          v

&#x20;                 +-------------------+

&#x20;                 | Security Monitor  |

&#x20;                 +-------------------+

&#x20;                          |

&#x20;                          v

&#x20;                 +-------------------+

&#x20;                 | Terminal Dashboard|

&#x20;                 +-------------------+

