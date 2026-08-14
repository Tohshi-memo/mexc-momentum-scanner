# Decision Report

- generated_at: 2026-08-14T16:06:30.940993+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11572**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=11572, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.78% | **+0.58%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.76% | **+0.57%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_BB3S | 2/16 | 12.5% | +2.61% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.82% | **+1.53%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +1.94% | **+1.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.73% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$632.37** / 初期 $100.00 (+532.37%)
- 確定: 4040件 (Win 1269 / Loss 1329 / Flat 1442) / skip 4093件
- 成長率目線: 平均log +0.000457 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $632.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.41** / 初期 $100.00 (+49.41%)
- 確定: 1651件 (Win 471 / Loss 398 / Flat 782) / skip 3332件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0232 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $149.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.75** / 初期 $100.00 (+17.75%)
- 確定: 1531件 (Win 466 / Loss 584 / Flat 481) / pending 5件 / skip 1509件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000213 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EDEN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $117.75

## 6. Latest Market Context

- 更新: 2026-08-14T16:06:18.718450+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=62963.6
- Funnel: target 985 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +12.91% | $4,696,398.79 |
| VELVET/USDT:USDT | +4.72% | $40,775,130.15 |
| EDEN/USDT:USDT | +4.29% | $38,138,884.16 |
| AKE/USDT:USDT | +2.99% | $66,386,316.01 |
| APR/USDT:USDT | +1.95% | $5,776,241.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +4.73% | +4.72% |
| EDEN/USDT:USDT | below_1h_threshold | +4.29% | +4.28% |
| AKE/USDT:USDT | below_1h_threshold | +2.80% | +2.79% |
| APR/USDT:USDT | below_1h_threshold | +1.96% | +1.95% |
| DOS/USDT:USDT | below_1h_threshold | +1.94% | +1.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
