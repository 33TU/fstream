import asyncio
import fstream


async def main():
    reader, writer = await fstream.open_connection('127.0.0.1', 5588)
    counter = 0

    while True:
        wmessage = f"Hello. Message number: {counter}".encode()

        # Send message
        writer.write(wmessage)
        writer.write(b'\n')
        await writer.drain()

        # Receive message
        rmessage = await reader.readuntil(b'\n', include_delimiter=False)
        if rmessage == wmessage:
            print('Message OK!', rmessage)
        else:
            print('Message FAILED!', rmessage)

        # Sleep
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())