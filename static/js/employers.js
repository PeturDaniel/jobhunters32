$(document).ready(function(){
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        let searchText = $('#search-box').val();
        $.ajax( {
            url: '?leit=' + searchText,
            type: 'GET',
            success: function(resp){
                let newHtml = resp.data.map(d => {
                    return `<div class="well employer">
                                <a href="/vinnustadir/${d.id}">
                                    <img class="employer-image" src="#" alt="#"/>
                                    <h4 class="employer-title">${d.name}</h4>
                                    <p>${d.address}</p>
                                </a>
                            </div>`
                    });
                    $('.employers').html(newHtml.join(''));
                    $('#search-box').val('');
                },
            error: function (xhr, status, error) {
            //finna betri leið, show toastr?
            console.error(error);
            }
        });
    });
});