# ComfyUI Filename Tools

Custom nodes for ComfyUI to extract and optionally trim filenames from file paths.

## Features

- Extract filename from a full file path
- Optionally remove everything from a specified marker
- Automatically removes the file extension

## Node: Extract & Trim Filename (No Extension)

### Inputs

- `file_path` (STRING): Full path to the file (e.g., `C:/images/image_upscaled_001.png`)
- `trim_marker` (STRING): Optional marker to trim from (e.g., `_upscaled`)

### Output

- Filename without extension, trimmed at the marker (if found)

### Example

**Input path:**  
`C:/Test/image_upscaled_001.jpg`  
**Marker:** `_upscaled`  
**Output:** `image`

## Installation

1. Clone or download this repository into your `ComfyUI/custom_nodes/` folder:

```
git clone https://github.com/yourusername/comfyui-filename-tools.git
```

2. Restart ComfyUI

## License

This project is licensed under the MIT License.
