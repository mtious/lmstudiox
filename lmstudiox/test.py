import asyncio
import lmstudio as lms

async def use_lmstudio():
    async with lms.AsyncClient("localhost:1234") as client:
        model = await client.llm.model("qwen3.5-9b")
        stream = await model.respond_stream("你好")
        async for fragment in stream:
            if fragment.content:
                print(fragment.content, end="", flush=True)
        print()

async def use_lmstudiox():
    async with lms.AsyncClient("localhost:1234") as client:
        model = await client.llm.model("qwen3.5-9b")
        stream = await model.respond_stream("你好")
        async for fragment in stream:
            if fragment.content:
                print(fragment.content, end="", flush=True)
        print()

asyncio.run(use_lmstudio())
asyncio.run(use_lmstudiox())