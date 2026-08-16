# Decision Report

- generated_at: 2026-08-16T07:51:22.033612+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11724**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.60% / filled 20/20。**
- 全期間 MARKET基準: n=11724, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.02% | **+0.46%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.42% | **+0.30%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.29% | **+0.26%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.19% | **+0.95%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.84% | **+0.55%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.40% | **+0.38%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.67% | **+0.25%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.23% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4183件 (Win 1292 / Loss 1363 / Flat 1528) / skip 4102件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CROSS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.78** / 初期 $100.00 (+54.78%)
- 確定: 1777件 (Win 494 / Loss 417 / Flat 866) / skip 3358件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0045 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.07% 残高後 $154.78

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.28** / 初期 $100.00 (+19.28%)
- 確定: 1627件 (Win 495 / Loss 618 / Flat 514) / pending 3件 / skip 1566件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000150 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PIXEL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $119.28

## 6. Latest Market Context

- 更新: 2026-08-16T07:51:12.785182+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=63028.0
- Funnel: target 986 → liquid 134 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEMI/USDT:USDT | +31.83% | $7,632,638.66 |
| H/USDT:USDT | +19.83% | $9,012,815.38 |
| SPORTFUN/USDT:USDT | +14.74% | $4,500,980.52 |
| BASED/USDT:USDT | +13.26% | $2,640,904.64 |
| AIO/USDT:USDT | +12.56% | $3,277,685.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +4.97% | +4.98% |
| APR/USDT:USDT | below_1h_threshold | +4.39% | +4.41% |
| BTW/USDT:USDT | below_1h_threshold | +1.61% | +1.62% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.42% | +1.43% |
| PRL/USDT:USDT | below_1h_threshold | +1.27% | +1.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
