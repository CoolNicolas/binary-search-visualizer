import gradio as gr

# Helper: generate HTML bars
def render_bars(state, highlight_mid=False):
    arr = state["arr"]
    left = state["left"]
    right = state["right"]
    mid = state["mid"]
    found_index = state["found_index"]
    target = state["target"]

    html = '<div style="display:flex; align-items:flex-end; gap:5px; height:250px;">'
    for i, val in enumerate(arr):

        # ----- NEW: clamp heights -----
        clamped = max(1, min(val, 19))   # restrict to 1–19
        scaled_height = clamped * 10     # each unit = 10px

        color = "skyblue"
        if found_index == i:
            color = "green"
        elif i < left or i > right:
            color = "lightgray"
        elif highlight_mid and i == mid:
            color = "red"

        pointer = ""
        if i == left:
            pointer += "&#x25B2; L<br>"
        if i == right:
            pointer += "&#x25B2; R<br>"
        if highlight_mid and i == mid:
            pointer += "&#x25B2; M<br>"

        html += f'''
            <div style="text-align:center;">
                <div style="
                    background-color:{color};
                    width:40px;
                    height:{scaled_height}px;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    color:white;
                ">{val}</div>
                {pointer}
            </div>
        '''
    html += '</div>'
    return html


# Start search
def start_search(list_text, target_text):
    # Parse inputs safely
    try:
        arr = [int(x) for x in list_text.strip().split()]
        target = int(target_text.strip())
    except:
        # Invalid input handling
        arr = []
        target = None
        return (
            "<p style='color:red'>Invalid input! Enter integers only.</p>",
            {"arr": [], "target": None, "left": None, "right": None,
             "mid": None, "found_index": None, "phase": 0},
            "Invalid input"
        )

    # Enforce size limits
    if len(arr) < 2 or len(arr) > 20:
        return (
            "<p style='color:red'>List must have 2–20 integers.</p>",
            {"arr": arr, "target": target, "left": None, "right": None,
             "mid": None, "found_index": None, "phase": 0},
            "Invalid length"
        )

    # Sort the array before binary search
    arr.sort()
    left, right = 0, len(arr) - 1
    mid = (left + right) // 2

    # Store everything in a state dictionary
    state = {
        "arr": arr, "target": target,
        "left": left, "right": right, "mid": mid,
        "found_index": None, "phase": 0
    }

    # Render the initial visual
    html = render_bars(state)
    return html, state, "Search initialized"


# Next step
def next_step(state):
    # Retrieve stored search values
    arr = state["arr"]
    if not arr:
        return "<p style='color:red'>Initialize search first.</p>", state, "No data"

    left = state["left"]
    right = state["right"]
    mid = state["mid"]
    found_index = state["found_index"]
    target = state["target"]
    phase = state["phase"]

    # If already found, simply show state again
    if found_index is not None:
        html = render_bars(state)
        return html, state, "Target already found"

    # Cannot search further
    if left > right:
        html = render_bars(state)
        return html, state, "Target not found"

    # Phase 0: compute new mid after adjusting left/right range
    if phase == 0:
        mid = (left + right) // 2
        state["mid"] = mid
        state["phase"] = 1
        html = render_bars(state, highlight_mid=True)
        return html, state, f"Middle is {arr[mid]}"

    # Phase 1: compare arr[mid] with target
    if arr[mid] == target:
        state["found_index"] = mid
        html = render_bars(state)
        state["phase"] = 0
        return html, state, f"Middle {arr[mid]} is the target! Found at index {mid}"

    # Adjust search boundaries
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

    # Update state for next iteration
    state.update({"left": left, "right": right, "phase": 0})
    html = render_bars(state)
    return html, state, f"Middle {arr[mid]} is not the target"


# Reset search
def reset_search():
    # Restore empty/initial state
    state = {
        "arr": [], "target": None,
        "left": None, "right": None, "mid": None,
        "found_index": None, "phase": 0
    }
    return "<p>Search reset</p>", state, "Reset"


# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Binary Search Visualizer")
    gr.Markdown("Enter a list of integers (space-separated) and a single target number.")

    # Inputs for list + target
    with gr.Row():
        list_input = gr.Textbox(label="List of integers (space-separated)")
        target_input = gr.Textbox(label="Target integer")

    # The main visual output + hidden search state
    html_output = gr.HTML(label="Binary Search")
    state_store = gr.State()
    message = gr.Textbox(label="Message", interactive=False)

    # Buttons for controlling the visualization
    btn_start = gr.Button("Start Search")
    btn_next = gr.Button("Next Step")
    btn_reset = gr.Button("Reset")

    # Link buttons to functions
    btn_start.click(start_search, inputs=[list_input, target_input],
                    outputs=[html_output, state_store, message])
    btn_next.click(next_step, inputs=state_store,
                   outputs=[html_output, state_store, message])
    btn_reset.click(reset_search, outputs=[html_output, state_store, message])

demo.launch()



# AI Disclaimer: All HTML and CSS code used in this project, including the visual layout and styling, was generated with the assistance of ChatGPT-5. The design and implementation decisions are based on suggestions provided by the AI.
