# Decision Report

- generated_at: 2026-05-08T17:52:41.591212+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3812**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.98% / filled 20/20。**
- 全期間 MARKET基準: n=3812, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+1.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.98% | **+1.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.98% | **+1.98%** |
| ASK | 20/20 | 100.0% | +1.97% | **+1.97%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.29% | **+1.09%** |
| LIMIT_BB3S | 3/14 | 21.4% | +3.11% | **+0.67%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.61% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.68% | **+0.38%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.13% | **+0.06%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.18% | **-0.10%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -1.14% | **-0.17%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.53% | **-0.29%** |

## 2. $100 Live Portfolio

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定トレード: 27件 (TP 7 / SL 18 / EXP 2)
- 最新: RKLBSTOCK/USDT:USDT SL_HIT PnL -2.88% 残高後 $98.82
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 181件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T17:52:35.900951+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.45% price=80128.0
- Funnel: target 768 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COLLECT/USDT:USDT | +9.47% | $1,531,941.02 |
| CHIP/USDT:USDT | +7.71% | $50,260,610.47 |
| IO/USDT:USDT | +7.29% | $1,213,301.50 |
| SIREN/USDT:USDT | +6.81% | $16,177,258.74 |
| AKT/USDT:USDT | +6.21% | $1,084,259.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COLLECT/USDT:USDT | below_1h_threshold | +4.97% | +4.52% |
| AKT/USDT:USDT | below_1h_threshold | +4.13% | +3.68% |
| PYTH/USDT:USDT | below_1h_threshold | +3.38% | +2.93% |
| FHE/USDT:USDT | below_1h_threshold | +3.38% | +2.92% |
| LINEA/USDT:USDT | below_1h_threshold | +3.28% | +2.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
