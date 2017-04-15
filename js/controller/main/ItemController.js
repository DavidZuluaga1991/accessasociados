/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


app.controller('ItemController', ['$scope', function (scope) {
        scope.$parent.isopen = (scope.$parent.default === scope.item);
        /*scope.$watch('isopen', function (newvalue, oldvalue, scope) {
            scope.$parent.isopen = newvalue;
        });*/
    }]);
