from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field


@dataclass
class RunningStartupResult:
    success: bool
    stdout: Optional[str] = None
    stderr: Optional[str] = None
    traceback: Optional[str] = None
    exception_name: Optional[str] = None
    exception_string: Optional[str] = None
    routes: List[str] = field(default_factory=lambda: [])
    configs: Optional[Dict[str, Any]] = None
