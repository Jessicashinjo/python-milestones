# Cross Origin Resource Sharing

This term, CORS for short, describes the mechanism that allows resources in a particular domain to be shared with clients that are outside the domain. This is a critical concept when opening up accessibility to any resource you own. You want to deny all requests from other domains that attempt to access information, or change information in your system.

For example, you have exposed an API at the URL `http://api.bangazon.com` which will allow any authorized client to make PUT, POST, and DELETE requests on your data. You need to ensure that only authorized clients can do this with a CORS policy.

With CORS, you often respond to any client request with two headers.

1. Which origins are allowed.
1. Which methods are allowed for the client.

Here's what those headers would look like if an authorized client from `http://www.zoo.com` made a request to add a new resource to your system.

```
Access-Control-Allow-Origin: http://www.zoo.com
Access-Control-Allow-Methods: POST, PUT, DELETE
```

These headers specify that `zoo.com` is allowed to access resources, and it is authorized to create new items, update items, and delete items.

## OPTIONS Request

You likely have already noticed that when you attempt an XHR request to a domain that is different than the domain of the request, the browser actually perform a prerequisite XHR with the `OPTIONS` verb. This request is where the headers described above are obtained.

Once the browser examines those headers, and verifies that the original XHR is allowed, the request will be made. If the client is not authorized, an [HTTP status code of 401](http://www.restpatterns.org/HTTP_Status_Codes/401_-_Unauthorized) will be generated to alert the client that the request is not allowed.


# Additional Resources

* [Using CORS](http://www.html5rocks.com/en/tutorials/cors/)
* [HTTP access control (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS)
