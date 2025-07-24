# agent.py
import subprocess, tempfile, textwrap, time
from pydantic import BaseModel, Field, constr
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel  # or AnthropicModel, etc.


# ---------- Pydantic schemas ----------
class PythonRequest(BaseModel):
    code: constr(strip_whitespace=True, max_length=4000) = Field(
        ..., description="Pure Python. No shell."
    )
    stdin: str | None = None


class PythonResult(BaseModel):
    stdout: str
    stderr: str
    exit_code: int
    duration_s: float


# ---------- Tool ----------
def run_python(req: PythonRequest) -> PythonResult:
    start = time.time()
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(textwrap.dedent(req.code))
        path = f.name

    try:
        proc = subprocess.run(
            ["python", path],
            input=req.stdin or "",
            capture_output=True,
            text=True,
            timeout=5,  # seconds; tune
        )
        return PythonResult(
            stdout=proc.stdout[:10_000],
            stderr=proc.stderr[:10_000],
            exit_code=proc.returncode,
            duration_s=time.time() - start,
        )
    except subprocess.TimeoutExpired as e:
        return PythonResult(
            stdout=e.stdout or "", stderr="Timeout", exit_code=124, duration_s=time.time() - start
        )


# ---------- Agent ----------
agent = Agent(
    system_prompt=(
        "You are a helpful assistant. "
        "When code execution is needed, call run_python. "
        "Always show the code you intend to run before executing. "
        "Keep code short and deterministic."
    ),
    model=OpenAIModel("gpt-4.1-mini"),  # swap model
    tools=[run_python],
)

if __name__ == "__main__":
    while True:
        try:
            q = input(">>> ")
            if not q:
                break
            resp = agent.run_sync(q)  # blocking convenience
            print(resp.output)  # validated final answer
            if hasattr(resp, "tool_results"):
                print("TOOL RESULTS:", resp.tool_results)
        except (EOFError, KeyboardInterrupt):
            break
