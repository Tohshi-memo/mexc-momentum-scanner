# Decision Report

- generated_at: 2026-05-19T06:08:29.076647+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4461**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.42% / filled 20/20。**
- 全期間 MARKET基準: n=4461, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.42% | **+0.92%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.66% | **+0.56%** |
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.79% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.37% | **+0.83%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.93% | **+0.75%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +1.85% | **+0.56%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.44% | **+0.24%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.27% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$96.70** / 初期 $100.00 (-3.30%)
- 確定トレード: 54件 (TP 14 / SL 37 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +5.37% 残高後 $96.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.85** / 初期 $100.00 (+20.85%)
- 確定: 458件 (Win 120 / Loss 158 / Flat 180) / skip 564件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.81% 残高後 $120.85

## 4. Latest Market Context

- 更新: 2026-05-19T06:08:27.091505+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=76908.1
- Funnel: target 768 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +29.15% | $8,523,225.15 |
| ONDO/USDT:USDT | +15.18% | $49,701,912.88 |
| LIT/USDT:USDT | +11.09% | $1,110,128.98 |
| AKT/USDT:USDT | +9.88% | $1,228,018.96 |
| INJ/USDT:USDT | +8.85% | $25,648,118.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIA/USDT:USDT | below_1h_threshold | +2.12% | +2.07% |
| EDEN/USDT:USDT | below_1h_threshold | +1.50% | +1.45% |
| SIREN/USDT:USDT | below_1h_threshold | +1.48% | +1.44% |
| PLAY/USDT:USDT | below_1h_threshold | +0.50% | +0.45% |
| MONAD/USDT:USDT | below_1h_threshold | +0.45% | +0.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
