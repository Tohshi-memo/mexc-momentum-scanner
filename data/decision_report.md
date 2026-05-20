# Decision Report

- generated_at: 2026-05-20T21:18:09.385861+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4581**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4581, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | -1.00% | **-0.20%** |
| LIMIT_9PCT | 6/20 | 30.0% | -2.00% | **-0.60%** |
| LIMIT_10PCT | 6/20 | 30.0% | -2.00% | **-0.60%** |
| LIMIT_5PCT | 11/20 | 55.0% | -1.11% | **-0.61%** |
| LIMIT_6PCT | 9/20 | 45.0% | -1.36% | **-0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +4.51% | **+2.71%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.85% | **+2.57%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.49% | **+1.92%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.45% | **+1.72%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.11** / 初期 $100.00 (+25.11%)
- 確定: 539件 (Win 138 / Loss 179 / Flat 222) / skip 603件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $125.11

## 4. Latest Market Context

- 更新: 2026-05-20T21:18:03.391590+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=77690.2
- Funnel: target 758 → liquid 124 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +39.21% | $27,223,188.10 |
| FIDA/USDT:USDT | +29.45% | $10,144,240.05 |
| BSB/USDT:USDT | +20.21% | $57,058,534.44 |
| NIL/USDT:USDT | +15.40% | $2,483,764.67 |
| JTO/USDT:USDT | +12.69% | $2,127,224.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.08% | +4.07% |
| EDEN/USDT:USDT | below_1h_threshold | +3.47% | +3.46% |
| FIDA/USDT:USDT | below_1h_threshold | +1.68% | +1.66% |
| BB/USDT:USDT | below_1h_threshold | +0.93% | +0.92% |
| LYN/USDT:USDT | below_1h_threshold | +0.64% | +0.63% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
