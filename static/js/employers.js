$(document).ready(function(){
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        let searchText = $('#search-box').val();
        console.log(searchText.length)
        if (searchText.trim() !== '')  {
            $.ajax( {
                url: '?leit=' + searchText.trim(),
                type: 'GET',
                success: function(resp){
                    let newHtml = resp.data.map(d => {
                        return `<div class="col">
                                    <a href="/vinnustadir/${ d.id }" class="card-link">
                                        <div class="card h-100">
                                            <img src="${ d.profile_photo }" class="employer-profile-photo rounded mx-auto d-block" alt="...">
                                            <div class="card-body">
                                                <h5 class="employer-name">${ d.name }</h5>
                                                <h6 class="employer-address">${ d.address }</h6>
                                            </div>
                                        <div class="card-footer bg-info-subtle">
                                            <small class="footer-text">blablabla</small>
                                        </div>
                                    </a>
                                </div>`
                        });
                        console.log(newHtml)
                        $('.employers').html(newHtml.join(''));
                        $('#search-box').val('');
                    },
                error: function (xhr, status, error) {
                //finna betri leið, show toastr?
                console.error(error);
                }
            });
        }
        $('#search-box').val('');
    });
});