# Copyright 2025 Miromind.ai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# from e2b_code_interpreter import Sandbox
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("local-python-interpreter")

# DEFAULT CONFS
DEFAULT_TIMEOUT = 1800  # seconds


@mcp.tool()
async def create_sandbox() -> str:
    """Create a linux sandbox.

    Args:
        timeout: Time in seconds before the sandbox is automatically shutdown. The default is 300 seconds.

    Returns:
        The id of the newly created sandbox. You should use this sandbox_id to run other tools in the sandbox.
    """
    return "TODO"


@mcp.tool()
async def run_command(command: str, sandbox_id: str) -> str:
    """Execute a command in the linux sandbox.

    Args:
        command: The command to execute.
        sandbox_id: The id of the sandbox to execute the command in. To create a new sandbox, use tool `create_sandbox`.

    Returns:
        A CommandResult object containing the result of the command execution, format like CommandResult(stderr=..., stdout=..., exit_code=..., error=...)
    """
    return "TODO"


@mcp.tool()
async def run_python_code(code_block: str, sandbox_id: str) -> str:
    """Run python code in an interpreter and return the execution result.

    Args:
        code_block: The python code to run.
        sandbox_id: The id of the sandbox to run the code in. Reuse existing sandboxes whenever possible. To create a new sandbox, use tool `create_sandbox`.

    Returns:
        A CommandResult object containing the result of the command execution, format like CommandResult(stderr=..., stdout=..., exit_code=..., error=...)
    """
    return "TODO"


@mcp.tool()
async def upload_file_from_local_to_sandbox(
    sandbox_id: str, local_file_path: str, sandbox_file_path: str = "/home/user"
) -> str:
    """Upload a local file to the `/home/user` dir of the remote python interpreter.

    Args:
        sandbox_id: The id of the sandbox to run the code in. Reuse existing sandboxes whenever possible. To create a new sandbox, use tool `create_sandbox`.
        local_file_path: The path of the file on local machine to upload.
        sandbox_file_path: The path of directory to upload the file to in the sandbox. Default is `/home/user/`.

    Returns:
        The path of the uploaded file in the remote python interpreter if the upload is successful.
    """
    return "TODO"


@mcp.tool()
async def download_file_from_internet_to_sandbox(
    sandbox_id: str, url: str, sandbox_file_path: str = "/home/user"
) -> str:
    """Download a file from the internet to the `/home/user` dir of the remote python interpreter.

    Args:
        sandbox_id: The id of the sandbox to run the code in. Reuse existing sandboxes whenever possible. To create a new sandbox, use tool `create_sandbox`.
        url: The URL of the file to download.
        sandbox_file_path: The path of directory to download the file to in the sandbox. Default is `/home/user/`.

    Returns:
        The path of the downloaded file in the python interpreter if the download is successful.
    """
    return "TODO"


@mcp.tool()
async def download_file_from_sandbox_to_local(
    sandbox_id: str, sandbox_file_path: str, local_filename: str = None
) -> str:
    """Download a file from the sandbox to local system. Files in sandbox cannot be processed by tools from other servers - only local files and internet URLs can be processed by them.

    Args:
        sandbox_id: The id of the sandbox to download the file from. To have a sandbox, use tool `create_sandbox`.
        sandbox_file_path: The path of the file to download on the sandbox.
        local_filename: Optional filename to save as. If not provided, uses the original filename from sandbox_file_path.

    Returns:
        The local path of the downloaded file if successful, otherwise error message.
    """
    return "TODO"


if __name__ == "__main__":
    mcp.run(transport="stdio")
