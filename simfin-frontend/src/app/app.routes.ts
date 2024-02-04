import { Routes } from '@angular/router';
import { LoginComponent } from './users/login/login.component';
import { SignupComponent } from './users/signup/signup.component';
import { BankingComponent } from './dashboards/banking/banking.component';

export const routes: Routes = [
    {
        path: '',
        title: 'Log In page',
        component: LoginComponent,
    },
    {
        path: 'login',
        title: 'Log In page',
        component: LoginComponent,
    },
    {
        path: 'signup',
        title: 'Sign Up page',
        component: SignupComponent,
    },
    {
        path: 'dashboard',
        title: 'Dashboard',
        component: BankingComponent,
    },
];
