<template>
<div class="container">
<h1>Upload Form</h1>
<form  @submit.prevent="uploadPhoto" id='uploadForm'>

<div class="form-group">
    <label for="desc" class="form-check-label">Description </label>
    <textarea name="description" form='uploadForm' class="form-control"></textarea>
</div>
<div class="form-group">
    <input type="file" name="photo" class="form-control-file" accept="image/*">
</div>

<input type="submit" value="Submit" class="btn btn-primary">
</form>
</div>
</template>

<script>
export default {
    data() {
      return {
          csrf_token:''
      }     
    },
    methods:{
      uploadPhoto(){
        let uploadForm = document.getElementById('uploadForm');
        let form_data = new FormData(uploadForm);
        fetch("/api/upload",{
            method: 'POST',
            body: form_data,
            headers:{
                'X-CSRFToken': this.csrf_token
            }
        })
        .then(function (response){
            return response.json();
        })
        .then(function (data){
            //display a success message
            console.log(data)
        })
        .catch(function (error){
            console.log(error)
        });        
      },
      getCsrfToken(){
          let self=this;
          fetch('/api/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data.csrf_token);
                self.csrf_token=data.csrf_token;
            })
      }
    },
    created(){
        this.getCsrfToken();
    }    
}
</script>

<style scoped>
  .form-group{
  margin-top:10px;
  margin-bottom:10px;
  }  
</style>