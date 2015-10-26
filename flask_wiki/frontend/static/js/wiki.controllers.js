var app = angular.module('WikiApp', ['ngRoute']);

app.config(function($locationProvider){
   $locationProvider.html5Mode(true);
});

//app.config(function($routeProvider){
//    $routeProvider.
//        when($location.path(), {
//            templateUrl: '/api/pages' + $location.path(),
//            controller: 'PageDetail'
//        })
//});

app.filter("sanitize", ['$sce', function($sce){
    return function (htmlCode) {
        return $sce.trustAsHtml(htmlCode);
    }
}]);

app.controller('PageDetail', function ($scope, $http, $location) {
    $http.get('/api/pages' + $location.path()).
        success(function(data, status, headers){
            $scope.data = data;
        }).
        error(function(data, status){
            $scope.errors = status;
        })
});
