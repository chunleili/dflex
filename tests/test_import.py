#!/usr/bin/env python3
"""Test if dflex can be imported successfully"""

try:
    import dflex
    print("✅ dflex installed successfully!")
    print(f"📁 Location: {dflex.__file__}")
    print(f"✨ Ready to use dflex!")
except Exception as e:
    print(f"❌ Import failed: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
