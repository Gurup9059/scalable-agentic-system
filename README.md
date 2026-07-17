# scalable-agentic-system
Problem
Attaching hundreds of tools directly to an LLM causes degraded tool-selection accuracy, parameter hallucination, and increased latency.
Proposed Architecture
Planner / Intent Classifier – Understands the user request.
Tool Router – Selects the top 3–5 relevant tools instead of exposing all tools to the LLM.
Domain Tool Groups – PayPal APIs are grouped into invoice, payment, dispute, reporting, etc.
Execution Engine – Executes the selected APIs.
Observability Layer – Captures logs, traces, metrics, and failures.
