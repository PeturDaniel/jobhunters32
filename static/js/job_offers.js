$(document).ready(function(){
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        const searchText = $('#search-box').val();
        $ajax( {
            url: 'lausstorf?leit=' + searchText,
            type: 'GET',
            success: function(resp){
                const newHtml = resp.data.map(d => {
                    return `<div class="well job">
                                <a href="/lausstorf/${d.id}">
                                
                                </a>
                            <div/>`

                    })
                    },
            error: function (xhr, status, error) {
            //finna betri leið, show toastr?
            console.error(error);
            }
        });
    });
});