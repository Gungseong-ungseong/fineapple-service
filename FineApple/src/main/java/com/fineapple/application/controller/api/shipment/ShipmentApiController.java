package com.fineapple.application.controller.api.shipment;

import com.fineapple.domain.shipment.service.ShipmentService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequiredArgsConstructor
@RequestMapping
public class ShipmentApiController {
    private final ShipmentService shipmentService;
//
//    @GetMapping("/api/v1/shipments/{shipmentId}")
//    public ResponseEntity<ShipmentDto> getShipmentDetail(@PathVariable Long shipmentId){
//        return ResponseEntity.ok(shipmentService.getShipmentDetail(shipmentId));
//    }
//
//    @GetMapping("/api/v1/shipments") //전체 조회
//    public ResponseEntity<List<ShipmentDto>> getAllShipments() {
//        return ResponseEntity.ok(shipmentService.findAllShipments());
//    }
//
//    @PostMapping("/api/v1/shipments")
//    public ResponseEntity<Void> createShipment(@RequestBody ShipmentRequestDto dto) {
//        shipmentService.createShipment(dto);
//        return ResponseEntity.ok().build();
//    }
//
//    @PatchMapping("/api/v1/shipments/{shipmentId}")
//    public ResponseEntity<Void> updateShipmentStatus(
//            @PathVariable Long shipmentId,
//            @RequestBody UpdateShipmentStatusRequest request) {
//
//        shipmentService.updateShipmentStatus(shipmentId, request.getDeliveryStatus());
//        return ResponseEntity.ok().build();
//    }

}
