# lmstudiox

**An extended Python SDK for LM Studio with support for explicitly enabling or disabling model thinking mode.**

> **Unofficial project.** `lmstudiox` is an independent, community-developed project. It is not affiliated with, endorsed by, or officially maintained by LM Studio or its developers.

`lmstudiox` extends the official [`lmstudio`](https://github.com/lmstudio-ai/lmstudio-python) Python SDK with additional capabilities, including explicit control over model thinking mode.

It provides an API compatible with the original SDK while allowing developers to disable thinking mode when needed.

## Features

- **Thinking Mode Control**: Explicitly enable or disable model thinking mode through `LlmPredictionConfig`.
- **Familiar API**: Built on top of the official `lmstudio` SDK, retaining its familiar usage patterns.
- **Streaming Support**: Supports asynchronous streaming responses.
- **Version Alignment**: The package version is kept in sync with the official [lmstudio](https://pypi.org/project/lmstudio/) package version on PyPI.

## Installation

```bash
pip install lmstudiox
```

## Usage

The following example demonstrates the difference between the official `lmstudio` SDK and `lmstudiox` when interacting with a model.

```python
import asyncio
import lmstudio
import lmstudiox


# Use the official lmstudio SDK (thinking mode enabled by default).
async def use_lmstudio():
    async with lmstudio.AsyncClient("localhost:1234") as client:
        model = await client.llm.model("qwen3.5-9b")
        stream = await model.respond_stream("hello !")
        async for x in stream:
            if x.content:
                print(x.content, end="", flush=True)
        print()


# Use lmstudiox to explicitly disable thinking mode.
async def use_lmstudiox():
    async with lmstudiox.AsyncClient("localhost:1234") as client:
        model = await client.llm.model("qwen3.5-9b")
        stream = await model.respond_stream("hello !", config=lmstudiox.LlmPredictionConfig(enable_thinking=False))
        async for x in stream:
            if x.content:
                print(x.content, end="", flush=True)
        print()


# Run both examples for comparison.
asyncio.run(use_lmstudio())
asyncio.run(use_lmstudiox())
```

## Requirements

- Python >= 3.12
- LM Studio with its local API server enabled

## Acknowledgements

This project is built on top of the official [LM Studio Python SDK](https://github.com/lmstudio-ai/lmstudio-python).

Special thanks to the LM Studio team for providing the underlying SDK and local inference platform.

## License

See [LICENSE](LICENSE) for details.