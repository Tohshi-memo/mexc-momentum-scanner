# Decision Report

- generated_at: 2026-08-14T15:06:26.313530+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11567**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.91% / filled 20/20。**
- 全期間 MARKET基準: n=11567, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +1.36% | **+1.02%** |
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.73% | **+0.62%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.79% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.21% | **+1.01%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.93% | **+0.61%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.66% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$623.01** / 初期 $100.00 (+523.01%)
- 確定: 4035件 (Win 1266 / Loss 1328 / Flat 1441) / skip 4093件
- 成長率目線: 平均log +0.000453 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $623.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.41** / 初期 $100.00 (+49.41%)
- 確定: 1651件 (Win 471 / Loss 398 / Flat 782) / skip 3327件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0115 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $149.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.66** / 初期 $100.00 (+17.66%)
- 確定: 1527件 (Win 464 / Loss 582 / Flat 481) / pending 6件 / skip 1509件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000195 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $117.66

## 6. Latest Market Context

- 更新: 2026-08-14T15:06:17.836592+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=62636.1
- Funnel: target 985 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +150.08% | $41,605,077.36 |
| AKE/USDT:USDT | +59.71% | $67,228,960.16 |
| CROSS/USDT:USDT | +44.60% | $2,020,192.83 |
| VELVET/USDT:USDT | +34.41% | $40,113,849.50 |
| H/USDT:USDT | +25.02% | $3,241,472.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CROSS/USDT:USDT | below_1h_threshold | +2.82% | +2.73% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +2.35% | +2.27% |
| APR/USDT:USDT | below_1h_threshold | +1.96% | +1.88% |
| H/USDT:USDT | below_1h_threshold | +1.65% | +1.57% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +1.20% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
