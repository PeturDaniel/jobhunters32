const search = document.getElementById('search-box')
const employer = document.getElementById('unique-employers')
const category = document.getElementById('unique-categories')
const publish_date = document.getElementById('order-publish-date')
const due_date = document.getElementById('order-due-date')
const checkbox = document.getElementById('checkbox')

//Search bar event listener
search.addEventListener('input', function () {
    const s = 'search'
    resetFilters(s)
    doSearchJobs()
})

//Dropdown filters event listeners
employer.addEventListener('change', function () {
    const e = 'employer'
    resetFilters(e)
    filterEmployer()
})
category.addEventListener('change', function () {
    const c = 'category'
    resetFilters(c)
    filterCategory()
})

//Order by buttons event listeners
publish_date.addEventListener('click', function () {
    const p = 'publish'
    resetFilters(p)
    updateURL('publish_date');
    orderJobs('publish_date');
})
due_date.addEventListener('click', function () {
    const d = 'due'
    resetFilters(d)
    updateURL('due_date');
    orderJobs('due_date');
})

//Checkbox event listener
checkbox.addEventListener('change', function () {
    const cb = 'checkbox'
    resetFilters(cb)
    filterApplied()
})

const resetFilters = (event) => {
    if (event === 'publish' || event === 'due') {
        search.value = ''
        employer.selectedIndex = 0;
        category.selectedIndex = 0;
        checkbox.checked = false
    }
    else if (event === 'search') {
        employer.selectedIndex = 0;
        category.selectedIndex = 0;
        checkbox.checked = false
    }
    else if (event === 'employer') {
        search.value = ''
        category.selectedIndex = 0;
        checkbox.checked = false
    }
    else if (event === 'category') {
        search.value = ''
        employer.selectedIndex = 0;
        checkbox.checked = false
    }
    else if (event === 'checkbox') {
        search.value = ''
        employer.selectedIndex = 0;
        category.selectedIndex = 0;
    }
}

const doSearchJobs = () => {
    const jobs = document.querySelectorAll(".well-job");
    const query = document.getElementById("search-box").value;

    jobs.forEach((job) => {
        let job_title = job.innerText.trim().split('\n')
        if (job_title[0].toLowerCase().includes(query.trim().toLowerCase())) {
            job.classList.remove("hidden");
        }
        else {
            job.classList.add("hidden");
        }
    });
};

const filterEmployer = () => {
    const company = document.getElementById('unique-employers').value;
    const jobs = document.querySelectorAll(".well-job");
    filterJobs(jobs, company, 2)
}

const filterCategory = () => {
    const category = document.getElementById('unique-categories').value;
    const jobs = document.querySelectorAll(".well-job");
    filterJobs(jobs, category, 1)
}

const filterJobs = (jobs, filter, index) => {
    jobs.forEach((job) => {
        let job_inner_text = job.innerText.trim().split('\n')
        if (job_inner_text[index].includes(filter)) {
            job.classList.remove('hidden');
        }
        else {
            job.classList.add("hidden");
        }
    });
}

const orderJobs = (order_by) => {
    fetch('/lausstorf/?order_by=' + encodeURIComponent(order_by))
        .then(response =>
            response.text()
        )
        .then(data => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(data, 'text/html');
            const ordered_job_offers = doc.querySelector('#job-offers-for');
            const current_job_offers = document.querySelector('#job-offers-for');
            if (current_job_offers.innerHTML && ordered_job_offers.innerHTML) {
                current_job_offers.innerHTML = ordered_job_offers.innerHTML;
            }
        })
}

function updateURL(order_by) {
    const url = new URL(window.location.href);
    url.searchParams.set('order_by', order_by);
    window.history.pushState({}, '', url);
}

const filterApplied = () => {
    const checkbox = document.getElementById("checkbox")
    const application_ids = document.querySelectorAll(".application")
    const applied_jobs = application_ids[0].innerText.slice(2, -1).split(", ")
    const jobs = document.querySelectorAll(".well-job");

    jobs.forEach((job) => {
        if (checkbox.checked === true && applied_jobs.indexOf(job.id) !== -1) {
            job.classList.remove("hidden")
        }
        else if (checkbox.checked === false) {
            job.classList.remove("hidden")
        }
        else {
            job.classList.add("hidden");
        }
    });
}
