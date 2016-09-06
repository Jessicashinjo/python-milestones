# Django and Angular Together Again

To see a bare bones, but functional, Angular/Django application that shows how to make authentication work, check out the [Djangular repository](https://github.com/chortlehoort/djangular.

## Angular Application Setup

```js
// Create main Angular module
var app = angular.module('YourApp', ['ngRoute'])

// Configure to use interpolation punctuation that differs from Django's
angular.module('YourApp').config(
[
    '$interpolateProvider', 
    '$httpProvider',
    function($interpolateProvider, $routeProvider, $httpProvider) {
      $interpolateProvider.startSymbol('((');
      $interpolateProvider.endSymbol('))');
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  }
]);
```

## Authentication

### Creating a User

Use `$http` to POST credential to Django. In your controller for handling the registration view, create a function that handles POSTing the data, and then handle success and failure.

```js
$scope.register = function() {
    $http({
      url: "/register/",
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        "username": $scope.user.userName,
        "password": $scope.user.password,
        "email": $scope.user.email,
        "first_name": $scope.user.firstName,
        "last_name": $scope.user.lastName
      }
    }).success(res => {
      if (res.data === "True") {
          $location.path('/');
      } else {
          // Show dialog element telling user that registration failed
      }
    }).error(() => {
      // Show dialog element telling user that registration failed
    });
};
```

Then, in your Django application, set up a URL handler to route this request.

```py
url(r'^register/$', views.register_user, name='register_user'),
```

Now create the corresponding view.

```py
# You will need to import the json library to parse the request body from
# a JSON string into a dictionary
import json

def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
                    username=req_body['username'],
                    password=req_body['password'],
                    email=req_body['email'],
                    first_name=req_body['first_name'],
                    last_name=req_body['last_name'],
                    )

    # Commit the user to the database by saving it
    new_user.save()

    # Invoke the login_user method and return its reponse to the client
    return login_user(request)
```

### Authenticating a User

Now you need a method that will log in the user. As you saw above, when you register a user, you simply call this method (if you wish) to automatically log the user into your system if registration is successful.

```py
def login_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Use the built-in authenticate method to verify
    authenticated_user = authenticate(
            username=req_body['username'],
            password=req_body['password']
            )

    # If authentication was successful, log the user in
    success = True
    if authenticated_user is not None:
        login(request=request, user=authenticated_user)
    else:
        success = False

    data = json.dumps({"success":success})
    return HttpResponse(data, content_type='application/json')
```
