import {Component, OnInit} from '@angular/core';
import {Subject} from 'rxjs/Subject';
import {Observable} from 'rxjs/Observable';
import {WebcamImage, WebcamInitError, WebcamUtil} from 'ngx-webcam';
import { Socket } from 'ngx-socket-io';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  classification_result = this.socket.fromEvent<string>('classification');
  classification=null;
  // toggle webcam on/off
  public showWebcam = true;
  public videoOptions: MediaTrackConstraints = {
    width: {ideal: 512},
    height: {ideal: 384}
  };
  public errors: WebcamInitError[] = [];

  // latest snapshot
  public webcamImage: WebcamImage = null;

  // webcam snapshot trigger
  private trigger: Subject<void> = new Subject<void>();
  // switch to next / previous / specific webcam; true/false: forward/backwards, string: deviceId

  constructor(private socket: Socket) { }
  
  public ngOnInit(): void {
    this.classification_result.subscribe(res=> {
      this.classification = res;
    })
  }

  public triggerSnapshot(): void {
    this.trigger.next();
  }

  public handleInitError(error: WebcamInitError): void {
    this.errors.push(error);
  }

  public handleImage(webcamImage: WebcamImage): void {
    this.webcamImage = webcamImage;
    var image_data = webcamImage.imageAsBase64
    this.socket.emit('image', image_data);
  }

  public get triggerObservable(): Observable<void> {
    return this.trigger.asObservable();
  }

  public displayCamera() {
    this.webcamImage = null;
    this.classification = null;
  }

}
