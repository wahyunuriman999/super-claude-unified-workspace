# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import time

class BaseProvider:
    def execute(self, prompt, context):
        raise NotImplementedError("Providers must implement execute()")

class MockProvider(BaseProvider):
    def __init__(self, name):
        self.name = name
        
    def execute(self, prompt, context):
        # Simulate network latency and response
        time.sleep(1.0)
        return f"[{self.name}] Synthesized output for prompt: '{prompt}'"

class ProviderManager:
    def __init__(self):
        self.providers = {}
        
    def register_provider(self, name, provider_instance):
        self.providers[name] = provider_instance
        
    def route_request(self, provider_name, prompt, context):
        if provider_name not in self.providers:
            print(f"Warning: Provider '{provider_name}' not found. Using fallback.")
            provider_name = list(self.providers.keys())[0] if self.providers else None
            
        if provider_name:
            provider = self.providers[provider_name]
            return provider.execute(prompt, context)
        return "ERROR: No providers registered."
