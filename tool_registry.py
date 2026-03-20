# C:\Users\yabid\jarvis-operator\jarvis_network\tool_registry.py

def run_tool(name: str, **kwargs):
    tool_name = name.upper()

    if tool_name == "WEBSITE_BUILDER":
        from jarvis_network.autocoder_bridge import build_website_from_prompt

        prompt = kwargs.get("prompt") or kwargs.get("original_prompt")
        if not prompt:
            raise ValueError("WEBSITE_BUILDER requires 'prompt'.")
        return build_website_from_prompt(prompt)

    raise NotImplementedError(f"Tool '{name}' is not wired yet.")
