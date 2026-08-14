# Decision Report

- generated_at: 2026-08-14T14:41:42.759671+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11564**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=11564, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +1.21% | **+0.97%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.91% | **+0.64%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.39% | **+0.33%** |
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.21% | **+1.01%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.66% | **+0.41%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.74% | **+0.41%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.47% | **+0.37%** |
| MARKET_LONG | 20/20 | 100.0% | +0.29% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$629.29** / 初期 $100.00 (+529.29%)
- 確定: 4032件 (Win 1266 / Loss 1326 / Flat 1440) / skip 4093件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $629.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.41** / 初期 $100.00 (+49.41%)
- 確定: 1651件 (Win 471 / Loss 398 / Flat 782) / skip 3324件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0099 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $149.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.87** / 初期 $100.00 (+17.87%)
- 確定: 1524件 (Win 463 / Loss 580 / Flat 481) / pending 6件 / skip 1509件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000243 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.87

## 6. Latest Market Context

- 更新: 2026-08-14T14:41:30.085595+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=62736.1
- Funnel: target 985 → liquid 180 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.0 >= 65=1, 4h RSI 70.2 >= 65=1, 4h RSI 69.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +134.11% | $39,698,244.64 |
| AKE/USDT:USDT | +67.45% | $69,624,421.92 |
| VELVET/USDT:USDT | +44.24% | $39,732,946.40 |
| CROSS/USDT:USDT | +36.78% | $1,936,208.81 |
| CAP/USDT:USDT | +30.19% | $6,617,755.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +4.48% | +4.32% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.55% | +3.39% |
| TESLA/USDT:USDT | below_1h_threshold | +2.55% | +2.39% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.29% | +2.14% |
| COAI/USDT:USDT | below_1h_threshold | +2.03% | +1.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
