import Foundation

struct User:Codable {
    statuc var current:User!
    var id:String
    var username:String
}