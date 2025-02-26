import asyncio
import threading


def demo1():
    async def hello():
        print("Hello world!")
        await asyncio.sleep(1)
        print("Hello again!")

    asyncio.run(hello())


def demo2():
    async def hello(name):
        print("Hello %s! (%s)" % (name, threading.current_thread))
        await asyncio.sleep(1)
        print("Hello %s again! (%s)" % (name, threading.current_thread))
        return name

    async def main():
        L = await asyncio.gather(hello("Bob"), hello("Alice"))
        print(L)

    asyncio.run(main())


def demo3():
    async def wget(host):
        print(f"wget {host}...")

        reader, writer = await asyncio.open_connection(host, 80)

        header = f"GET / HTTP/1.0\r\nHost: {host}\r\n\r\n"
        writer.write(header.encode("utf-8"))
        await writer.drain()

        while True:
            line = await reader.readline()
            if line == b"\r\n":
                break
            print("%s header > %s" % (host, line.decode("utf-8").rstrip()))

        writer.close()
        await writer.wait_closed()
        print(f"Done {host}.")

    async def main():
        await asyncio.gather(
            wget("www.sina.com.cn"), wget("www.sohu.com"), wget("www.163.com")
        )

    asyncio.run(main())


if __name__ == "__main__":
    demo1()
    demo3()
