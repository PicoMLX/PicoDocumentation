# Discover Pico AI Homelab servers using Bonjour

{% hint style="info" %}
Bonjour is available in Pico AI Homelab version 1.1.1 (build 29) and newer
{% endhint %}

Consider enhancing user convenience of your chat app by adding the option to automatically detect Pico AI Homelab servers on the user's local network using Bonjour.

Pico AI Homelab will broadcast its human readable instance name (e.g. **Ronald's AI Homelab**), the server's local hostname (e.g. **macbook-pro.local**), IP address and the port Pico AI Homelab is running on (e.g. **11434**).

A chat app can use this infrormation to automatically configure the app to connect to Pico AI Homelab, without the user needing to enter IP addresses or host names. Bonjour dramatically simplifies settings up chat clients.

From the chat app user's perspective, these are the steps to take:

1. In settings or during setup, the user taps a "Scan for Pico AI Homelab" button.
2. The chat app will now listen to Bonjour packets sent by all Pico AI Homelab instances on the local area network.
3. The app displays a list of available Pico AI Homelab instances for the user to select. Each Pico AI Homelab instance has a human readable name. It is recommended to show the human readable name to the user.
4. The user selects one or more Pico AI Homelab servers to connect to connect to
5. The app will automatically store the server name, port, ip address and/or host name and (re)connect to the server automatically

{% hint style="warning" %}
Users can disable Bonjour in the Pico AI Homelab settings. Chat apps should not depend solely on Bonjour for connections. Always provide an alternative method for users to manually enter the port and hostname or IP address of the Pico AI Homelab server they wish to connect to.
{% endhint %}

{% hint style="info" %}
There can be more than one Pico AI Homelab server on a local area network. Always show a list of discovered servers.
{% endhint %}

{% hint style="info" %}
IP addresses on a local area network can be dynamic, meaning that they can change over time. While Pico AI Homelab includes the IP address in its broadcast, it's recommended to connect  to a Pico AI Homelab instance using the local host name instead of the IP address.
{% endhint %}

Pico AI Homelab broadcasts Bonjour service `_pico._tcp,`the human readable service name (e.g. Ronald's AI Homelab) and send a dictionary in the Bonjour `txtRecord` with the following info:&#x20;

* `IPAddress`: The IP address of the Pico AI Homelab server
* `Port`: The port number, specified as a string, to which the Pico AI Homelab HTTP server is bound. Default is `11434`.
* `LocalHostName`: The local host name, e.g. **ronalds-macbook.local**&#x20;
* `ServerIdentifier`:  A unique UUID string to identify a Pico AI Homelab instance, even if IP address, serice name, and local host name changed.

{% hint style="info" %}
Each Pico AI Homelab instance sends a unique UUID as its server identifier, which stays consistent between sessions. If the admin changes the computer's hostname or its IP address, this ID can still be used to connect the user to the correct instance. By scanning the network again and looking for the Pico AI Homelab instance with this specific ID, users can easily reconnect despite any changes in hostname or IP address.
{% endhint %}

### Example projects

* [BonjourPico](https://github.com/PicoMLX/BonjourPico) example project
* [Enchanted fork](https://github.com/ronaldmannak/enchanted/) by [Ronald Mannak](https://app.gitbook.com/u/frJejcEKyWM1JVY2dvzAShAUPOZ2 "mention")

### Sample client code

The easiest way to use Bonjour for Pico AI Homelab in your chat app is to add the [BonjourPico Swift package](https://github.com/PicoMLX/BonjourPico). An example app for iOS and macOS is included in the repository.

Make sure to update your app settings:

* Add an [NSBonjourServices](https://developer.apple.com/documentation/bundleresources/information-property-list/nsbonjourservices) property to your info.plist and set one of the items to `_pico._tcp`
* Add an [NSLocalNetworkUsageDescription](https://developer.apple.com/documentation/bundleresources/information_property_list/nslocalnetworkusagedescription) property to your info.plist and add an explanation why your app needs network access.
* If your app is sandboxed, enable `Outgoing Connections (Client)` in `Signing & Capabilities -> App Sandbox`.

```swift
import SwiftUI
import BonjourPico

struct ContentView: View {
    
    @State var bonjourPico = BonjourPico()
    
    var body: some View {
        VStack {
            List(bonjourPico.servers, id: \.self) { server in
                let domain = "\(server.hostName):\(server.port)"
                let ip = "\(server.ipAddress):\(server.port)"
                Text("\(server.name): \(domain) \(ip)")
            }
            
            Button(bonjourPico.isScanning ? "Stop scanning" : "Scan for Pico AI Homelab servers") {
                bonjourPico.startStop()
            }
        }
        .padding()
    }
}
```
