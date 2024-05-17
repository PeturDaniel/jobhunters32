const doSearchEmployers = () => {
    const job_offers = document.querySelectorAll(".well_job");
    const query = document.getElementById("search-box").value;

    job_offers.forEach((job_offer) => {
        let employer_title = job_offer.innerText.trim().split('\n')
        if (employer_title[0].toLowerCase().includes(query.trim().toLowerCase())) {
            job_offer.classList.remove("hidden");
        }
        else {
            job_offer.classList.add("hidden");
        }
    });
};
