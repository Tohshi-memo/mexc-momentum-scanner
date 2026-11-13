# Decision Report

- generated_at: 2026-11-13T08:16:26.818893+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18802**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=18802, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.00% | **+0.95%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.09% | **+1.03%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.41% | **+0.92%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.93% | **+0.79%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.66% | **+0.58%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.28% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,750.19** / 初期 $100.00 (+1650.19%)
- 確定: 7272件 (Win 2095 / Loss 2330 / Flat 2847) / skip 8091件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,750.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$401.65** / 初期 $100.00 (+301.65%)
- 確定: 4821件 (Win 1300 / Loss 1073 / Flat 2448) / skip 7392件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0456 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $401.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000195 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T08:16:13.066656+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=68650.6
- Funnel: target 1086 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +68.07% | $13,705,292.43 |
| BARD/USDT:USDT | +51.89% | $12,792,797.90 |
| KOR/USDT:USDT | +43.33% | $1,803,265.50 |
| ARIA/USDT:USDT | +34.73% | $9,663,766.30 |
| H/USDT:USDT | +13.45% | $1,703,684.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BARD/USDT:USDT | below_1h_threshold | +2.08% | +1.94% |
| BEAT/USDT:USDT | below_1h_threshold | +1.02% | +0.89% |
| NVIDIA/USDT:USDT | below_1h_threshold | +0.96% | +0.82% |
| KGEN/USDT:USDT | below_1h_threshold | +0.95% | +0.81% |
| CBRSSTOCK/USDT:USDT | below_1h_threshold | +0.84% | +0.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
