# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import os
import re
import json
import time

class KnowledgeCompiler:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.nodes = {}
        
    def _parse_markdown(self, file_path):
        """Real Markdown parsing to extract knowledge nodes."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract headers as nodes
            headers = re.findall(r'#+\s*(.*)', content)
            
            node_id = os.path.basename(file_path).replace('.md', '')
            return {
                "id": node_id,
                "file": file_path,
                "headers": headers,
                "content_length": len(content)
            }
        except Exception as e:
            print(f"Failed to parse {file_path}: {e}")
            return None

    def compile_directory(self, target_dir):
        """Scan directory and parse all markdown files."""
        dir_path = os.path.join(self.root_dir, target_dir)
        if not os.path.exists(dir_path):
            print(f"Warning: Directory {dir_path} not found.")
            return

        print(f"Scanning directory: {target_dir}...")
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    node = self._parse_markdown(file_path)
                    if node:
                        self.nodes[node["id"]] = node

    def generate_graph(self):
        """Generate Directed Acyclic Graph (DAG) JSON from parsed nodes."""
        graph = {
            "metadata": {
                "compiler_version": "v12.0",
                "timestamp": time.time(),
                "total_nodes": len(self.nodes)
            },
            "nodes": self.nodes
        }
        
        output_path = os.path.join(self.root_dir, 'knowledge.graph.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(graph, f, indent=2)
            
        print(f"Compiled {len(self.nodes)} markdown files into {output_path}")
        return output_path
