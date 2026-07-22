# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import time

class ISAExecutor:
    def __init__(self, memory_hierarchy, provider_manager):
        self.memory = memory_hierarchy
        self.provider = provider_manager
        
    def execute_instruction(self, opcode, name, task):
        print(f"[Tick {opcode}: {name}] Executing opcode...")
        
        if name == "OBSERVE":
            self._observe(task)
        elif name == "PLAN":
            self._plan(task)
        elif name == "EXECUTE":
            self._execute(task)
        elif name == "REFLECT":
            self._reflect(task)
        else:
            time.sleep(0.5)
            print(f"  -> Instruction {name} executed.")

    def _observe(self, task):
        time.sleep(0.5)
        self.memory.write_l1("current_task", task)
        self.memory.write_l1("context_gathered", True)
        print("  -> Context gathered and loaded into L1 Working Memory.")
        
    def _plan(self, task):
        time.sleep(0.5)
        context = self.memory.dump_state()
        print("  -> Invoking Model Orchestrator (Capability: core.planning)")
        response = self.provider.route_request("OpenAI (GPT-4o)", f"Create plan for: {task}", context)
        self.memory.write_l1("current_plan", response)
        print(f"  -> Plan generated: {response}")
        
    def _execute(self, task):
        time.sleep(0.8)
        plan = self.memory.L1_working.get("current_plan", "No plan found")
        print("  -> Invoking Model Orchestrator (Capability: infrastructure.routing)")
        response = self.provider.route_request("9Router (Gateway)", f"Execute plan: {plan}", plan)
        self.memory.write_l1("execution_result", response)
        print(f"  -> Execution result: {response}")
        
    def _reflect(self, task):
        time.sleep(0.5)
        result = self.memory.L1_working.get("execution_result", "No result")
        print("  -> Evaluating execution against L3 Knowledge Base rules...")
        self.memory.update_l4_experience(f"Reflected on task: {task}, Result: {result}")
        print("  -> Reflection saved to L4 Experience Memory.")
