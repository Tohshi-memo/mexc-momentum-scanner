# Decision Report

- generated_at: 2026-05-02T05:27:03.240045+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2867**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2867, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.16% | **+1.16%** |
| ASK | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_BB3S | 5/19 | 26.3% | +2.34% | **+0.61%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.04% | **+0.47%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.43% | **+0.37%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 7件 (TP 4 / SL 3 / EXP 0)
- 最新: BIO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T05:27:01.566104+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=78032.2
- Funnel: target 755 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +150.17% | $47,605,375.62 |
| B/USDT:USDT | +14.15% | $75,585,336.25 |
| SKYAI/USDT:USDT | +13.20% | $21,198,706.72 |
| PLAY/USDT:USDT | +12.87% | $4,557,254.32 |
| RLS/USDT:USDT | +10.81% | $2,424,751.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RLS/USDT:USDT | below_1h_threshold | +3.30% | +3.43% |
| TAC/USDT:USDT | below_1h_threshold | +2.54% | +2.68% |
| PLAY/USDT:USDT | below_1h_threshold | +1.93% | +2.07% |
| BR/USDT:USDT | below_1h_threshold | +1.27% | +1.41% |
| LYN/USDT:USDT | below_1h_threshold | +1.19% | +1.33% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
