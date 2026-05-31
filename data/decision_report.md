# Decision Report

- generated_at: 2026-05-31T00:20:39.404674+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5154**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=5154, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.95% | **+0.95%** |
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.11% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.82% | **+1.82%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.65% | **+1.40%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.84% | **+0.71%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.66% | **+0.59%** |
| ASK_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 78件 (TP 23 / SL 52 / EXP 3)
- 最新: NFP/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.19** / 初期 $100.00 (+23.19%)
- 確定: 792件 (Win 183 / Loss 242 / Flat 367) / skip 923件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +6.10%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $123.19

## 4. Latest Market Context

- 更新: 2026-05-31T00:20:36.695052+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=73865.7
- Funnel: target 773 → liquid 120 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +24.69% | $6,068,691.56 |
| TA/USDT:USDT | +20.00% | $2,012,240.22 |
| BIANRENSHENG/USDT:USDT | +15.50% | $1,311,296.25 |
| ONDO/USDT:USDT | +10.68% | $32,533,144.54 |
| STG/USDT:USDT | +9.02% | $3,367,987.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXS/USDT:USDT | below_1h_threshold | +4.28% | +4.27% |
| CHIP/USDT:USDT | below_1h_threshold | +2.70% | +2.69% |
| ASTER/USDT:USDT | below_1h_threshold | +2.19% | +2.17% |
| EDEN/USDT:USDT | below_1h_threshold | +1.83% | +1.82% |
| BSB/USDT:USDT | below_1h_threshold | +1.22% | +1.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
