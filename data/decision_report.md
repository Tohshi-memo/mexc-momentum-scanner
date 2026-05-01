# Decision Report

- generated_at: 2026-05-01T22:02:38.958724+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2837**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.45% / filled 20/20。**
- 全期間 MARKET基準: n=2837, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.81% | **+0.77%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.48% | **+1.03%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.10% | **+0.60%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.96% | **+0.57%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.68% | **+0.51%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.91% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RLS/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T22:02:37.290155+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=78223.1
- Funnel: target 755 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +28.69% | $8,056,874.54 |
| RLS/USDT:USDT | +14.36% | $2,282,648.56 |
| BLESS/USDT:USDT | +9.92% | $1,025,822.00 |
| ZEN/USDT:USDT | +8.08% | $9,086,365.64 |
| SNDKSTOCK/USDT:USDT | +7.46% | $6,080,589.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RLS/USDT:USDT | below_1h_threshold | +3.40% | +3.33% |
| RIF/USDT:USDT | below_1h_threshold | +1.39% | +1.31% |
| TAG/USDT:USDT | below_1h_threshold | +1.02% | +0.95% |
| RAVE/USDT:USDT | below_1h_threshold | +0.72% | +0.64% |
| IP/USDT:USDT | below_1h_threshold | +0.50% | +0.42% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
