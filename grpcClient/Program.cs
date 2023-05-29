namespace grpcClient {
    /**
     * @class Program
     * @brief Clase principal que contiene el punto de entrada del cliente gRPC.
     */
    class Program {
        /**
         * @brief Punto de entrada del programa.
         */
        static void Main() {

            var channel = new Grpc.Core.Channel("127.0.0.1:50052", ChannelCredentials.Insecure);
            var client = new GrpcCoords.Coords.CoordsClient(channel);
            var reply = client.GetCoords(new Google.Protobuf.WellKnownTypes.Empty());
            Console.WriteLine(reply.Data);
            Console.ReadKey();
        }
    }
}