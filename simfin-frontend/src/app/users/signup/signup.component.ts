import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-signup',
  standalone: true,
  imports: [RouterLink, ReactiveFormsModule],
  templateUrl: './signup.component.html',
  styleUrl: './signup.component.css'
})
export class SignupComponent {
  signUpForm = new FormGroup({
    username: new FormControl('', [Validators.required, Validators.email]),
    password: new FormControl('', Validators.required),
    confirmPassword: new FormControl('', Validators.required)
  })

  submitSignUpForm() {
    // Handle Sign Up form submission
    // Placeholder below
    alert("Signing up "+this.signUpForm.value.username+" with password "+this.signUpForm.value.password)
  }
}
