import asyncio
import lmstudio, lmstudiox

# Use the official lmstudio SDK (thinking mode enabled by default).
async def use_lmstudio():
    async with lmstudio.AsyncClient("localhost:1234") as client:
        model = await client.llm.model("qwen3.5-9b")
        stream = await model.respond_stream("hello !")
        async for fragment in stream:
            if fragment.content:
                print(fragment.content, end="", flush=True)
        print()


# Use lmstudiox to explicitly disable thinking mode.
async def use_lmstudiox():
    async with lmstudiox.AsyncClient("localhost:1234") as client:
        model = await client.llm.model("qwen3.5-9b")
        stream = await model.respond_stream("hello !", config=lmstudiox.LlmPredictionConfig(enable_thinking=False))
        async for fragment in stream:
            if fragment.content:
                print(fragment.content, end="", flush=True)
        print()


# Run both examples for comparison.
asyncio.run(use_lmstudio())
asyncio.run(use_lmstudiox())