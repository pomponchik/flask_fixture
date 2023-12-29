from typing import List, Dict, Optional, Any
from dataclasses import dataclass


@dataclass
class RunningStartupResult:
    success: bool
    stdout: Optional[str] = None
    stderr: Optional[str] = None
    traceback: Optional[str] = None
    exception_name: Optional[str] = None
    exception_string: Optional[str] = None
    routes: Optional[List[str]] = None
    configs: Dict[str, Any] = None
