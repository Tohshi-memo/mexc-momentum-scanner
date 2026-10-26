# Decision Report

- generated_at: 2026-10-26T02:26:36.951810+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17454**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=17454, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +6.28% | **+1.57%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_7PCT | 6/20 | 30.0% | +3.40% | **+1.02%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.70% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.55% | **+0.33%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.47% | **+0.26%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.35% | **+0.17%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.11% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 251件 (TP 93 / SL 150 / EXP 8)
- 最新: CT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,557.64** / 初期 $100.00 (+1457.64%)
- 確定: 6707件 (Win 1953 / Loss 2143 / Flat 2611) / skip 7308件
- 成長率目線: 平均log +0.000409 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,557.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$314.90** / 初期 $100.00 (+214.90%)
- 確定: 3997件 (Win 1110 / Loss 947 / Flat 1940) / skip 6868件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0621 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $314.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5614件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000286 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T02:26:24.683382+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=79521.9
- Funnel: target 1070 → liquid 138 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMCHI/USDT:USDT | +37.84% | $2,589,846.20 |
| CLAUDIA/USDT:USDT | +22.09% | $1,062,148.85 |
| BR/USDT:USDT | +10.89% | $7,246,156.98 |
| AXIS/USDT:USDT | +7.89% | $2,094,999.10 |
| DODO/USDT:USDT | +7.30% | $1,027,000.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXIS/USDT:USDT | below_1h_threshold | +1.15% | +1.39% |
| UNITREE/USDT:USDT | below_1h_threshold | +1.11% | +1.35% |
| TIA/USDT:USDT | below_1h_threshold | +0.70% | +0.94% |
| KIMCHI/USDT:USDT | below_1h_threshold | +0.45% | +0.69% |
| BR/USDT:USDT | below_1h_threshold | +0.37% | +0.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
