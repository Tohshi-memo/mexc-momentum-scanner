# Decision Report

- generated_at: 2026-10-16T09:51:27.010847+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16793**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.33% / filled 20/20。**
- 全期間 MARKET基準: n=16793, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.20% | **+0.84%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.83% | **+0.70%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.28% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.83% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.32% | **+0.50%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | -0.24% | **-0.18%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | -0.54% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.36** / 初期 $100.00 (+21.36%)
- 確定トレード: 241件 (TP 89 / SL 145 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,254.65** / 初期 $100.00 (+1154.65%)
- 確定: 6315件 (Win 1849 / Loss 2027 / Flat 2439) / skip 7039件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,254.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.95** / 初期 $100.00 (+176.95%)
- 確定: 3685件 (Win 1027 / Loss 875 / Flat 1783) / skip 6519件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0254 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $276.95

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4955件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000238 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-16T09:51:10.853626+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=82106.5
- Funnel: target 1078 → liquid 177 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +76.51% | $9,421,566.70 |
| CLAUDIA/USDT:USDT | +45.01% | $1,125,025.18 |
| ICNT/USDT:USDT | +15.21% | $1,453,440.57 |
| INJ/USDT:USDT | +14.97% | $81,337,828.90 |
| TIA/USDT:USDT | +13.80% | $44,834,296.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +2.31% | +2.44% |
| AVAX/USDT:USDT | below_1h_threshold | +1.65% | +1.77% |
| SYN/USDT:USDT | below_1h_threshold | +1.56% | +1.68% |
| RIVER/USDT:USDT | below_1h_threshold | +1.46% | +1.59% |
| ARB/USDT:USDT | below_1h_threshold | +1.05% | +1.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
