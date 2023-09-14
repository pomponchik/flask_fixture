import json
from typing import Optional
from dataclasses import dataclass, asdict


@dataclass
class RunningStartupResult:
    success: bool
    stdout: Optional[str] = None
    stderr: Optional[str] = None
    traceback: Optional[str] = None
    exception_name: Optional[str] = None
    exception_string: Optional[str] = None
    routes: Optional[list[str]] = None
