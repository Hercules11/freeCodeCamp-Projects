var express = require('express');
const helmet = require("helmet");
var app = express();

// everything is default.
// app.use(helmet());
// 加上中间件，就类似于戴个头盔，设置一下配置参数
// learning program should see the official doc.
// https://helmetjs.github.io/

// Removes the X-Powered-By header if it was set.
app.use(helmet.hidePoweredBy());

// app.use(
//   helmet({
//     frameguard: {
//       action: "deny",
//     },
//   })
// ); test failed

// Sets "X-Frame-Options: DENY"
app.use(helmet.frameguard({ action: "deny" }));

// Sets "X-XSS-Protection: 0"
app.use(helmet.xssFilter());

// Sets "X-Content-Type-Options: nosniff"
app.use(helmet.noSniff());

// Sets "X-Download-Options: noopen"
app.use(helmet.ieNoOpen());

// Sets "Strict-Transport-Security: max-age=123456; includeSubDomains; preload"
app.use(
  helmet.hsts({
    maxAge: 90 * 24 * 60 * 60,
    preload: true,
    force: true,
  })
);

// Sets "X-DNS-Prefetch-Control: off"
app.use(
  helmet.dnsPrefetchControl({
    allow: false,
  })
);


app.use(helmet.noCache());

// Sets "Content-Security-Policy: default-src 'self';script-src 'self' example.com;object-src 'none'"
app.use(
  helmet.contentSecurityPolicy({
    directives: {
      "default-src": ["'self'"],
      "script-src": ["'self'", 'trusted-cdn.com'],
      "object-src": ["'none'"],
    },
  })
);



































module.exports = app;
var api = require('./server.js');
app.use(express.static('public'));
app.disable('strict-transport-security');
app.use('/_api', api);
app.get("/", function (request, response) {
  response.sendFile(__dirname + '/views/index.html');
});
var listener = app.listen(process.env.PORT || 3000, function () {
  console.log('Your app is listening on port ' + listener.address().port);
});
