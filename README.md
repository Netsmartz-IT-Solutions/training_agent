# training_agent - Microsoft 365 Declarative Agent

This repository contains the source code (instructions and manifests) for the M365 Declarative Agent. 
It is configured with strict security overrides to prevent code generation and scope drift.

## How to Build
To modify the agent's behavior, edit `appPackage/instruction.txt`. 
When you are ready to package the agent for deployment, simply run:

```bash
python3 build.py
```

This will resolve the instruction macros and generate an `agent_package.zip` file that you can directly upload to Microsoft Teams Admin Center.
