import { Component } from '@angular/core';
import { LeftSidebarComponent } from './left-sidebar/left-sidebar.component';
import { RightSidebarComponent } from './right-sidebar/right-sidebar.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [LeftSidebarComponent, RightSidebarComponent],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent {

}
