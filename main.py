import collections
import collections.abc
import os
import asyncio
import PowerpointReader
import JsonWriter
import Explainer
import MakeQuery
import time


async def main():
    path = r"C:\Users\tamar\excellenteam\python_ex5\example.pptx"
    reader = PowerpointReader.PowerpointReader(path)
    data_list = reader.read_slides()
    explanations = []
    tasks = []
    for sd in data_list:
        q = MakeQuery.Query()
        q.from_slide(sd)
        task = asyncio.create_task(Explainer.get_explanation(q))
        tasks.append(task)
        # explanations.append(Explainer.get_explanation(q))
        # if ((data_list.index(sd) + 1) % 3) == 0:
        #     time.sleep(50)
    explanations = await asyncio.gather(*tasks)
    JsonWriter.to_json(os.path.splitext(os.path.basename(path))[0], *explanations)
    print("end")


if __name__ == '__main__':
    asyncio.run(main())
