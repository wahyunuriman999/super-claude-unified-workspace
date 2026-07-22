# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import time

class EventDispatcher:
    def __init__(self, isa_executor):
        self.isa_executor = isa_executor
        # Default 4-Tick pipeline sequence
        self.pipeline_sequence = [
            {"opcode": "0x01", "name": "OBSERVE"},
            {"opcode": "0x04", "name": "PLAN"},
            {"opcode": "0x07", "name": "EXECUTE"},
            {"opcode": "0x08", "name": "REFLECT"}
        ]
        
    def dispatch(self, task_name):
        print(f"\n--- INCOMING EVENT: {task_name} ---")
        start_time = time.time()
        
        for instr in self.pipeline_sequence:
            opcode = instr["opcode"]
            name = instr["name"]
            
            # Delegate to ISA Executor
            self.isa_executor.execute_instruction(opcode, name, task_name)
            
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"\n[KERNEL] Event Loop Completed Successfully. Process Terminated in {elapsed:.2f} seconds.")
