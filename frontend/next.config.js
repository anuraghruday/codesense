module.exports = {
    reactStrictMode: true,
    async rewrites() {
      return [{
        source: "/api/:path*",
        destination: "http://localhost:8000/:path*"
      }];
    }
  };