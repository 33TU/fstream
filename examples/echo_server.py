import asyncio
import fstream


# globals
LINE_LIMIT = 1024 * 1024


async def handle_client(reader: fstream.StreamReader, writer: fstream.StreamWriter):
    try:
        while True:
            line = await reader.readuntil(b'\n', limit=LINE_LIMIT)
            writer.write(line)
            await writer.drain()
    except Exception as ex:
        print('handle_conn', ex, ex.__class__)
        writer.close()


async def main():
    server = await fstream.start_server(handle_client, '127.0.0.1', 5588)
    await server.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
