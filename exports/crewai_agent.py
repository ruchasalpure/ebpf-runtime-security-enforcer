from crewai import Agent

ebpf_runtime_security_enforcer = Agent(
    role="Ebpf Runtime Security Enforcer",
    goal="Deliver high-precision autonomous Ebpf Runtime Security Enforcer operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
