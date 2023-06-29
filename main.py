import collections
import collections.abc
import os
import asyncio
import PowerpointReader
import JsonWriter
import Explainer
import MakeQuery
import SystemTest


async def main():
    SystemTest.test_system()
    # path = r"C:\Users\tamar\excellenteam\python_ex5\example.pptx"
    # reader = PowerpointReader.PowerpointReader(path)
    # data_list = reader.read_slides()
    # tasks = []
    # for sd in data_list:
    #     q = MakeQuery.Query()
    #     q.from_slide(sd)
    #     task = asyncio.create_task(Explainer.get_explanation(q))
    #     tasks.append(task)
    # explanations = await asyncio.gather(*tasks)
    # JsonWriter.to_json(os.path.splitext(os.path.basename(path))[0], *explanations)
    # print("end")


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
