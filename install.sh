#!/bin/bash
# Installation script for AEGIS v5.1 on macOS/Linux

TARGET_DIR="$HOME/.gemini/config/skills/aegis"

echo "Installing AEGIS v5.1 global skill..."
mkdir -p "$TARGET_DIR"

cp -r aegis/* "$TARGET_DIR/"

echo "Successfully installed AEGIS v5.1 to $TARGET_DIR"
echo "Restart your AI agent or IDE to reload the custom skills."
