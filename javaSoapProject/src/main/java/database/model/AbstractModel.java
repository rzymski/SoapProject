package database.model;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.Objects;
import java.util.UUID;

@MappedSuperclass
public class AbstractModel {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    private Long id;

    @Transient
    private String uid = UUID.randomUUID().toString();

    @Column(nullable = false, updatable = false)
    protected LocalDateTime createDate;
    @Column(nullable = false)
    private LocalDateTime updateDate;
    @PrePersist
    protected void onCreate() {
        createDate = LocalDateTime.now();
        updateDate = createDate;
    }
    @PreUpdate
    protected void onUpdate() {
        updateDate = LocalDateTime.now();
    }

    public AbstractModel() {}

    public AbstractModel(Long id) {
        this.id = id;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getUid() {
        return uid;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        AbstractModel that = (AbstractModel) o;

        return Objects.equals(this.id,((AbstractModel) o).id);
    }

    @Override
    public int hashCode() {
        return id != null ? id.hashCode() : 0;
    }
}
