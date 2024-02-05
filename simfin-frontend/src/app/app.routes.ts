import { Routes } from '@angular/router';
import { LoginComponent } from './users/login/login.component';
import { SignupComponent } from './users/signup/signup.component';
import { DashboardComponent } from './dashboard/dashboard.component';

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
        component: DashboardComponent,
    },
];
