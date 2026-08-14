# Decision Report

- generated_at: 2026-08-14T14:36:36.198231+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11562**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.86% / filled 20/20。**
- 全期間 MARKET基準: n=11562, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +1.30% | **+0.97%** |
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.92% | **+0.78%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.14% | **+0.74%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.53% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.62% | **+0.50%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.36% | **+0.47%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.39% | **+0.42%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.14% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$629.30** / 初期 $100.00 (+529.30%)
- 確定: 4030件 (Win 1265 / Loss 1325 / Flat 1440) / skip 4093件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $629.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.41** / 初期 $100.00 (+49.41%)
- 確定: 1651件 (Win 471 / Loss 398 / Flat 782) / skip 3322件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0250 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $149.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.88** / 初期 $100.00 (+17.88%)
- 確定: 1522件 (Win 462 / Loss 579 / Flat 481) / pending 6件 / skip 1508件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000305 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $117.88

## 6. Latest Market Context

- 更新: 2026-08-14T14:36:28.440149+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=62706.1
- Funnel: target 985 → liquid 178 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.4 >= 65=1, 4h RSI 91.6 >= 65=1, 4h RSI 81.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +141.55% | $39,446,744.74 |
| AKE/USDT:USDT | +65.58% | $69,382,230.99 |
| CAP/USDT:USDT | +40.73% | $6,219,745.10 |
| CROSS/USDT:USDT | +34.35% | $1,928,882.76 |
| VELVET/USDT:USDT | +31.90% | $39,204,250.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_relative_strength | +5.11% | +5.00% |
| VELVET/USDT:USDT | below_1h_threshold | +3.89% | +3.78% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.55% | +3.44% |
| TESLA/USDT:USDT | below_1h_threshold | +2.55% | +2.44% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.29% | +2.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
