# Decision Report

- generated_at: 2026-11-27T04:51:23.916759+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19760**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19760, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.36% | **-0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +3.15% | **+0.47%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_6PCT | 6/20 | 30.0% | -0.04% | **-0.01%** |
| LIMIT_9PCT | 4/20 | 20.0% | -1.00% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.19% | **+1.86%** |
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +1.65% | **+1.65%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.74% | **+1.04%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.39% | **+0.91%** |
| MARKET_LONG | 20/20 | 100.0% | +0.76% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$121.76** / 初期 $100.00 (+21.76%)
- 確定トレード: 292件 (TP 106 / SL 176 / EXP 10)
- 最新: SNXX/USDT:USDT EXPIRED PnL +2.62% 残高後 $121.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,938.41** / 初期 $100.00 (+1838.41%)
- 確定: 7644件 (Win 2199 / Loss 2460 / Flat 2985) / skip 8677件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $1,938.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$464.12** / 初期 $100.00 (+364.12%)
- 確定: 5280件 (Win 1408 / Loss 1135 / Flat 2737) / skip 7891件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SNXX/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $464.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7919件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000158 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-27T04:51:10.652824+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=61466.8
- Funnel: target 1097 → liquid 123 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +55.12% | $15,614,637.88 |
| BIGTIME/USDT:USDT | +21.43% | $3,014,732.58 |
| SNXX/USDT:USDT | +13.04% | $4,192,847.52 |
| VELVET/USDT:USDT | +12.43% | $1,381,883.16 |
| ONE/USDT:USDT | +10.93% | $1,493,386.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +3.36% | +3.24% |
| SNXX/USDT:USDT | below_1h_threshold | +2.70% | +2.58% |
| SKY/USDT:USDT | below_1h_threshold | +2.42% | +2.30% |
| KORU/USDT:USDT | below_1h_threshold | +2.32% | +2.20% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.54% | +1.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
