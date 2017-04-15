

(function (){
    angular.module('contact.controllers',[])
        .controller('contactcontroller', function () {
            this.comments = [];
            this.comment = {};
            this.clear = function () {
                this.comment.name = null;
                this.comment.email = null;
                this.comment.phone = null;
                this.comment.body = null;
            };

            this.addcomments = function (){
               this.comment.date = Date.now();
               this.comments.push(this.comment);
               this.comment = {};
            };
        })   
                
})();


/*export default contactcontroller2;*/