# Duties and Responsibilities for eBPF Runtime Security Enforcer Agent

## Dual-Control Architecture
Maker:
syscall-hook-enforcer

Checker:
privilege-escalation-checker

## Operational Workflow
1. The Maker (syscall-hook-enforcer) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (privilege-escalation-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
