# Decision Report

- generated_at: 2026-10-23T02:56:34.126234+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17183**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.06% / filled 20/20。**
- 全期間 MARKET基準: n=17183, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.13% | **+1.07%** |
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.91% | **+0.77%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.78% | **+0.55%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.65% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.46% | **+1.23%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.20% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,322.67** / 初期 $100.00 (+1222.67%)
- 確定: 6539件 (Win 1898 / Loss 2086 / Flat 2555) / skip 7205件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,322.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.89** / 初期 $100.00 (+176.89%)
- 確定: 3859件 (Win 1056 / Loss 900 / Flat 1903) / skip 6735件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0344 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $276.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5345件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000248 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T02:56:21.178291+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.78% price=81943.8
- Funnel: target 1096 → liquid 179 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.5 >= 65=1, 4h RSI 72.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +39.19% | $12,111,093.57 |
| IRYS/USDT:USDT | +27.74% | $4,240,264.26 |
| AGT/USDT:USDT | +16.44% | $5,160,465.57 |
| DNA/USDT:USDT | +12.01% | $4,217,850.55 |
| AKE/USDT:USDT | +10.21% | $11,126,215.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_relative_strength | +5.50% | +4.72% |
| BTW/USDT:USDT | below_1h_threshold | +4.21% | +3.43% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +4.20% | +3.42% |
| AGT/USDT:USDT | below_1h_threshold | +2.61% | +1.83% |
| BULLA/USDT:USDT | below_1h_threshold | +2.34% | +1.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
