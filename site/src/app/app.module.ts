import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {WebcamModule} from 'ngx-webcam';
import { AppComponent } from './app.component';
import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';
import { EarthAnimationComponent } from './earth-animation/earth-animation.component';
import { TrashcanComponent } from './trashcan/trashcan.component';

const port = 5001;
const config: SocketIoConfig = { url: 'http://localhost:'+port, options: {} };

@NgModule({
  declarations: [
    AppComponent,
    EarthAnimationComponent,
    TrashcanComponent
  ],
  imports: [
    BrowserModule,
    WebcamModule,
    SocketIoModule.forRoot(config)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
