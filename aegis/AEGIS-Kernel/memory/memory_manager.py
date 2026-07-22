# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import json
import os
import time

class MemoryHierarchy:
    def __init__(self, workspace_path):
        self.workspace = workspace_path
        self.L1_working = {}   # Active task context
        self.L2_context = {}   # Broader project state
        self.L3_knowledge = {} # Engineering rules and patterns
        self.L4_experience = {} # Past failures and successes
        self.L5_genome = {}    # The Engineering Genome
        
    def mount(self):
        print("Mounting L0-L5 Memory Hierarchy...")
        # In a real system, these load from the physical workspace
        self.L1_working = {"current_task": "None", "start_time": time.time()}
        self.L2_context = {"project_type": "AEGIS Core Ecosystem", "files_scanned": 0}
        self.L3_knowledge = self._load_json_if_exists('knowledge.graph.json', {})
        self.L4_experience = self._load_json_if_exists('FAILURE_DB.json', {})
        self.L5_genome = {"version": "v12.0", "mutation_rate": 0.01}
        
    def _load_json_if_exists(self, filename, default):
        path = os.path.join(self.workspace, filename)
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return default
        return default
        
    def write_l1(self, key, value):
        self.L1_working[key] = value
        
    def read_l3(self):
        return self.L3_knowledge
        
    def update_l4_experience(self, log):
        if 'logs' not in self.L4_experience:
            self.L4_experience['logs'] = []
        self.L4_experience['logs'].append(log)
        
    def dump_state(self):
        return {
            "L1": self.L1_working,
            "L2": self.L2_context,
            "L3_keys": list(self.L3_knowledge.keys())[:5] if isinstance(self.L3_knowledge, dict) else [],
            "L4_logs_count": len(self.L4_experience.get('logs', [])) if isinstance(self.L4_experience, dict) else 0,
            "L5": self.L5_genome
        }
