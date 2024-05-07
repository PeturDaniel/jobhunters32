$(document).ready(function(){
    $('#search-btn').on('click', function(e {
        e.preventDefault();
        let searchText = '#search-box'.val();
        $ajax( {
            url: 'lausstorf?leit=' + searchText,
            type: 'GET',
            success: function(resp){

            },
            error: function (xhr, status, error) {
            //finna betri leið, show toastr?
                console.error(error);
            }
        });
    });
});