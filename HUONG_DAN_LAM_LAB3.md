# HƯỚNG DẪN LÀM LAB 3 — Từng bước, không cần hiểu sâu

Code đã được chuẩn bị sẵn 100% (Task A xong, Task E và F đã soạn sẵn trên nhánh riêng).
Bạn chỉ cần làm theo đúng thứ tự dưới đây. Không bỏ bước nào.

Thư mục code của bạn: `C:\các nền tảng phát triển phần mềm\lab3-notes-app`

---

## PHẦN 0 — Việc tôi đã làm xong cho bạn

- ✅ Sửa `Dockerfile` để đọc cổng (PORT) từ biến môi trường.
- ✅ Thêm endpoint `/health` trong `app/main.py`.
- ✅ Đã build và chạy thử bằng Podman — `/health` trả về `{"status":"ok"}` đúng yêu cầu.
- ✅ Tạo sẵn git repo với các nhánh (branch):
  - `main` — đã có Task A
  - `task-e-version-bump` — đổi version, dùng cho Task E
  - `task-f-deliberate-failure` — lỗi cố ý, dùng cho Task F
- ✅ Tên tác giả commit đã để đúng tên bạn (Do Quoc Bao).

Việc còn lại **chỉ có bạn làm được** vì cần tài khoản GitHub/Render và điện thoại của chính bạn.

---

## PHẦN 1 — Đẩy (push) code lên GitHub

### 1.1. Tạo repository trên GitHub (nếu nhóm chưa có)

1. Vào https://github.com → đăng nhập.
2. Bấm nút **+** ở trên bên phải → **New repository**.
3. Đặt tên ví dụ `lab3-notes-app` (hoặc theo tên nhóm quy định).
4. Để **Private** hoặc **Public** theo yêu cầu môn học.
5. **KHÔNG** tick "Add a README file" (vì mình đã có code sẵn).
6. Bấm **Create repository**.
7. GitHub sẽ hiện ra một trang có dòng URL dạng:
   `https://github.com/<ten-ban>/lab3-notes-app.git`
   → copy URL đó.

### 1.2. Dùng GitHub Desktop để đẩy code lên (dễ nhất, máy bạn đã cài sẵn)

1. Mở **GitHub Desktop**.
2. Vào menu **File → Add local repository**.
3. Chọn đường dẫn: `C:\các nền tảng phát triển phần mềm\lab3-notes-app`
4. Nếu nó hỏi "This directory does not appear to be a Git repository" thì bấm **Cancel** —
   repo đã có git rồi, không cần tạo lại (nếu lỗi này hiện ra, báo lại cho tôi).
5. Ở góc trên, chọn nhánh hiện tại là `main`.
6. Vào menu **Repository → Repository settings → Remote** — hoặc đơn giản hơn:
   bấm nút **Publish repository** (nếu repo trên GitHub chưa có code) ở giữa màn hình.
   - Nếu bạn đã tạo repo trống ở bước 1.1, bỏ tick "Keep this code private" theo ý bạn,
     và chọn đúng tên repo đã tạo (hoặc bấm "Publish" để Desktop tự tạo luôn repo mới trên GitHub).
7. Bấm **Publish branch**. Đợi vài giây — xong, code đã lên GitHub.

### 1.3. (Thay thế) Dùng Git Bash nếu bạn thích dòng lệnh

Mở Git Bash tại đúng thư mục `lab3-notes-app`, chạy:

```bash
git remote add origin https://github.com/<ten-ban>/lab3-notes-app.git
git push -u origin main
git push origin task-a-platform-friendly
git push origin task-e-version-bump
git push origin task-f-deliberate-failure
```

Lần đầu push, GitHub sẽ mở trình duyệt để bạn đăng nhập/xác nhận — làm theo hướng dẫn trên màn hình.

**CHECKPOINT PHẦN 1:** Vào trang GitHub của repo, bạn thấy đủ 4 nhánh: `main`,
`task-a-platform-friendly`, `task-e-version-bump`, `task-f-deliberate-failure`.

---

## PHẦN 2 — Đăng ký Render và tạo Web Service (Task B)

### 2.1. Đăng ký Render

1. Vào https://render.com
2. Bấm **Get Started** hoặc **Sign Up**.
3. Chọn **Sign up with GitHub** (không cần thẻ tín dụng, không cần điền thẻ ở bất kỳ bước nào).
4. Nếu nó hỏi quyền truy cập GitHub (OAuth) — bấm **Authorize Render**.

⚠️ **Nếu ở bất kỳ bước nào Render hỏi bạn số thẻ/phương thức thanh toán — DỪNG LẠI và báo giảng viên.**
Gói Free không cần thẻ.

### 2.2. Tạo Web Service

1. Trong Render Dashboard, bấm **New +** → **Web Service**.
2. Chọn **Build and deploy from a Git repository** → bấm **Next**.
3. Nếu chưa thấy repo của bạn, bấm **Configure account** để cấp quyền Render đọc repo đó,
   rồi chọn đúng repo (ví dụ `lab3-notes-app`) → **Connect**.
4. Điền đúng theo bảng này:

| Mục | Giá trị |
|---|---|
| Name | tuỳ bạn, ví dụ `lab3-notes-app` |
| Language/Runtime | **Docker** |
| Branch | **main** |
| Region | chọn vùng gần Việt Nam nhất (Singapore nếu có) |
| Dockerfile Path | `./Dockerfile` (giữ mặc định) |
| Instance Type | **Free** |

5. Kéo xuống phần **Health Check Path** → gõ: `/health`
6. Bấm **Create Web Service**.

**CHECKPOINT B:** Service hiện ra trong dashboard, log build đang chạy — bạn sẽ thấy các dòng
giống trong `Dockerfile` của bạn chạy qua (pip install, uvicorn...).

---

## PHẦN 3 — Cấu hình biến môi trường (Task C)

1. Vào service vừa tạo → tab **Environment** (bên trái).
2. Bấm **Add Environment Variable**, thêm từng dòng:

| Key | Value |
|---|---|
| `DATABASE_URL` | `postgresql://app:unused@localhost:5432/appdb` |
| `APP_ENV` | `production` |

   (Không thêm `PORT` — Render tự đặt.)

3. Bấm **Save Changes**. Service sẽ tự redeploy — đây là bình thường.

**CHECKPOINT C:** Đợi vài phút, status chuyển sang **Live** (chấm xanh). Vào tab **Logs**,
thấy dòng kiểu `Uvicorn running on http://0.0.0.0:...` — nghĩa là app đã khởi động thành công.

> ⚠️ Khi chụp màn hình trang Environment để nộp báo cáo, hãy che/crop giá trị DATABASE_URL thật
> nếu sau này nó là chuỗi kết nối thật (hiện tại dùng placeholder nên chưa sao, nhưng nên tập quen).

---

## PHẦN 4 — Kiểm tra qua HTTPS (Task D)

1. Trên trang Render, ở trên cùng sẽ có URL dạng:
   `https://lab3-notes-app-xxxx.onrender.com`
2. Bấm vào URL đó / mở nó trên máy — phải tải được, có khoá HTTPS trên thanh địa chỉ.
3. **Quan trọng**: dùng **điện thoại, tắt wifi, dùng 4G/5G**, mở đúng URL đó.
   Phải load được — điều này chứng minh ai cũng truy cập được, không chỉ máy bạn trong phòng lab.
4. Mở Git Bash, kiểm tra health endpoint:

```bash
curl -si https://<url-cua-ban>.onrender.com/health | head -1
```

Kết quả mong đợi: `HTTP/2 200`

> Ghi chú: nếu service "ngủ" (không ai truy cập >15 phút), request đầu tiên có thể mất 30–60 giây
> để load lại — đó là bình thường, không phải lỗi.

**CHECKPOINT D:** URL load được qua HTTPS trên điện thoại dùng 4G, và `/health` trả 200.

---

## PHẦN 5 — Deploy lần hai (Task E)

Nhánh `task-e-version-bump` tôi đã soạn sẵn — chỉ đổi số phiên bản `APP_VERSION` từ `1.0.0` → `1.0.1`.

### 5.1. Mở Pull Request trên GitHub

1. Vào trang GitHub của repo.
2. Nó sẽ tự hiện banner "task-e-version-bump had recent pushes" → bấm **Compare & pull request**.
   (Nếu không thấy, vào tab **Pull requests → New pull request**, chọn base = `main`,
   compare = `task-e-version-bump`.)
3. Đặt tiêu đề ví dụ: `Task E: bump version to 1.0.1`
4. Bấm **Create pull request**.
5. (Nếu nhóm có bạn khác) nhờ 1 người review, bấm **Approve**.
6. Bấm **Merge pull request** → **Confirm merge**.

### 5.2. Theo dõi deploy

1. Quay lại Render → tab **Events**.
2. Bạn sẽ thấy một deploy mới tự động chạy (vì Render theo dõi nhánh `main`).
3. Đợi tới khi status **Live**.
4. Mở lại URL live — trang chủ (`/`) giờ phải hiện `"version":"1.0.1"`.
5. **Ghi lại commit hash** hiện trong Events panel cho CẢ lần deploy Task A lẫn lần deploy này
   (bấm vào từng deploy để xem hash đầy đủ, hoặc 7 ký tự đầu cũng được).

**CHECKPOINT E:** Events panel có 2 lần deploy thành công với 2 commit khác nhau, trang live
hiện bản mới (`1.0.1`).

---

## PHẦN 6 — Làm hỏng có chủ đích, rồi khôi phục (Task F)

Nhánh `task-f-deliberate-failure` tôi đã soạn sẵn — nó đọc một biến môi trường
`DEFINITELY_NOT_SET` chưa từng được đặt, nên app sẽ crash ngay khi khởi động.
Tôi đã test local: log hiện đúng `KeyError: 'DEFINITELY_NOT_SET'`.

### 6.1. Mở PR và merge nhánh lỗi

1. Trên GitHub, mở Pull Request: base = `main`, compare = `task-f-deliberate-failure`.
2. Tiêu đề: `Task F: deliberate start-up failure (for the lab exercise)`.
3. **Create pull request** → **Merge pull request** → **Confirm merge**.

### 6.2. Xem nó hỏng

1. Vào Render → **Events** — một deploy mới sẽ chạy và **thất bại** (Deploy failed, hoặc
   service sẽ ở trạng thái liên tục restart / crash loop).
2. Mở tab **Logs**, tìm dòng:
   ```
   KeyError: 'DEFINITELY_NOT_SET'
   ```
   → đây chính là dòng log cần ghi lại để nộp báo cáo.
3. Mở lại URL live trong lúc này — có thể sẽ lỗi 502 hoặc không phản hồi. Đây là kết quả mong đợi.

### 6.3. Rollback TRƯỚC (quan trọng: làm đúng thứ tự)

1. Trong Render, tab **Events**, tìm **lần deploy tốt gần nhất trước đó** (deploy Task E, version 1.0.1).
2. Bấm vào nó → bấm nút **Rollback to this deploy** (hoặc **Redeploy**, tuỳ bản UI của Render).
3. Xác nhận. Đợi tới khi Live trở lại — mở URL kiểm tra, trang chạy lại bình thường.

### 6.4. Sửa nguyên nhân (sau khi đã rollback)

Tạo một nhánh mới sửa lỗi (xoá dòng `MISSING = os.environ[...]`), merge qua PR:

```bash
git checkout main
git pull
git checkout -b task-f-fix
```

Mở file `app/main.py`, xoá dòng:
```python
MISSING = os.environ["DEFINITELY_NOT_SET"]  # Lab 3, Task F: deliberate start-up failure
```

```bash
git add -A
git commit -m "Fix: remove the deliberate start-up failure"
git push -u origin task-f-fix
```

Rồi mở PR trên GitHub (base `main`, compare `task-f-fix`) → merge như các bước trên.
Deploy mới sẽ chạy và thành công bình thường (vì đã rollback xong từ trước, bước này chỉ để
dọn sạch code trong `main`).

**CHECKPOINT F:** Bạn chỉ ra được đúng dòng log lỗi, và URL live đã chạy lại sau rollback.

---

## PHẦN 7 — Nộp bài

Dán 4 dòng sau vào form nộp bài của lớp:

1. **URL HTTPS đang chạy**: `https://<ten-service>.onrender.com`
2. **URL của Pull Request Task E** (lần deploy thứ 2): copy URL của PR ở Phần 5.1.
3. **Hai commit hash** hiển thị trong Events panel (Task A/trước và Task E).
4. **Một câu mô tả log lỗi Task F**, ví dụ:
   > "Ứng dụng crash khi khởi động với lỗi `KeyError: 'DEFINITELY_NOT_SET'` vì biến môi trường
   > `DEFINITELY_NOT_SET` được đọc ở `app/main.py` nhưng chưa được đặt trong Environment panel."

---

## Nếu gặp lỗi

| Hiện tượng | Nguyên nhân | Cách sửa |
|---|---|---|
| Build fail: "no Dockerfile found" | Tên file sai hoặc đường dẫn sai | Kiểm tra Settings → Dockerfile Path = `./Dockerfile` |
| URL timeout | App đang bind `127.0.0.1` thay vì `0.0.0.0` | Đã sửa trong Dockerfile rồi, không cần lo |
| 502 từ edge | Không có gì nghe đúng cổng PORT | Đã sửa (đọc `PORT` từ env), nếu vẫn lỗi báo tôi |
| Health check fail liên tục | Sai path, hoặc chậm | Kiểm tra Settings → Health Check Path = `/health` |
| Request đầu chậm 30-60s | Service free đang "ngủ" | Bình thường, đánh thức trước khi demo |
| `git push` không trigger deploy | Push nhánh không phải `main` | Phải **merge vào main** mới deploy |

Nếu bị kẹt ở bước nào, chụp màn hình lỗi và nói cho tôi biết — tôi sẽ đọc log cùng bạn.
