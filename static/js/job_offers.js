$(document).ready(function(){
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        const searchText = $('#search-box').val();
        $ajax( {
            url: 'lausstorf?leit=' + searchText,
            type: 'GET',
            success: function(resp){
            const newHtml = resp.data.map(d => {
                return <div className="col">
                            <div className="card">
                                <img src="..." className="card-img-top" alt="..."/>
                                <div className="card-body">
                                    <a href="/lausstorf/${d.id}">
                                        <h5 className="card-title">${d.title}</h5>
                                    </a>
                                    <!--employer name-->
                                    <!--Birt?-->
                                </div>
                                <div className="card-footer">
                                    <small className="footer-text">Umsóknarfrestur: ${d.due_date} | date:"d/m/Y"}</small>
                                </div>
                            </div>
                        </div>
                    })
                    },
            error: function (xhr, status, error) {
            //finna betri leið, show toastr?
            console.error(error);
            }
        });
    });
});