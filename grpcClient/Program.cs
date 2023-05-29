using System;
using System.Threading.Tasks;
using Grpc.Net.Client;
using Grpc.Core;

namespace grpcClient {
    class Program {
        static void Main() {

            Console.WriteLine("Searching channel...");
            var channel = new Grpc.Core.Channel("127.0.0.1:50052", ChannelCredentials.Insecure);
            //using var channel = GrpcChannel.ForAddress("https://localhost:50052");
            var client = new GrpcCoords.Coords.CoordsClient(channel);
            var reply = client.GetCoords(new Google.Protobuf.WellKnownTypes.Empty());
            Console.WriteLine("Competleted ...");
            Console.WriteLine(reply.Data);
           // await channel.Shutdown();
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
            Console.WriteLine("Hello World!");

        }
    }
}
// The port number must match the port of the gRPC server.

