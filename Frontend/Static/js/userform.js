const myForm = document.getElementById('myForm');

let all = [];

const createJSON = (e)=>{
    e.preventDefault();
    let data = {
        name: document.getElementById('first_name').value +" "+document.getElementById('last_name').value,
        email: document.getElementById('email').value,
        org: document.getElementById('org_name').value,
        emp_id: document.getElementById('emp_id').value,
        mobile: document.getElementById('mob_no').value,
        file: document.getElementById('file').value
    }
    all.push(data);
    document.forms[0].reset();
    console.log(all);
}

myForm.addEventListener('submit',createJSON);