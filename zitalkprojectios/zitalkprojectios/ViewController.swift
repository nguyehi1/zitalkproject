//
//  ViewController.swift
//  zitalkprojectios
//
//  Created by Hien Nguyen on 7/25/19.
//  Copyright © 2019 Hien Nguyen. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    @IBAction func showMessage(sender: UIButton) {
        let alertController = UIAlertController(title: "Welcome to ZiTalk", message: "Zitalk Adventure", preferredStyle: UIAlertController.Style.alert)
        
        alertController.addAction(UIAlertAction(title:"OK", style: UIAlertAction.Style.default, handler: nil))
        present(alertController, animated: true, completion: nil)
    }

}

