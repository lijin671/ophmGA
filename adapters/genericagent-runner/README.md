# GenericAgent Runner Adapter

This adapter will hand validated packets to a project-local GenericAgent runtime.

Current posture: skeleton only. It must not auto-install GenericAgent.

Before a real runner exists, require:

- explicit GenericAgent install path
- explicit browser profile name
- Web SOP / browser bridge readiness check
- scheduler/L4 expectation check when memory is part of the evaluation
- per-run permission packet
- cleanup command or manual cleanup checklist

