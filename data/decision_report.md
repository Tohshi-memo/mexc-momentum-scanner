# Decision Report

- generated_at: 2026-09-22T20:46:40.183034+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15359**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15359, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.89% | **-1.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.19% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.89% | **+2.16%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +3.95% | **+0.99%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.80% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,150.12** / 初期 $100.00 (+1050.12%)
- 確定: 5842件 (Win 1728 / Loss 1879 / Flat 2235) / skip 6078件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUSEBOOK/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,150.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5417件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.15** / 初期 $100.00 (+22.15%)
- 確定: 3114件 (Win 914 / Loss 1222 / Flat 978) / pending 6件 / skip 3720件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000023 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MUSEBOOK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $122.15

## 6. Latest Market Context

- 更新: 2026-09-22T20:46:25.780580+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=86222.5
- Funnel: target 1058 → liquid 190 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.3 >= 65=1, 4h RSI 89.3 >= 65=1, 4h RSI 70.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MUSEBOOK/USDT:USDT | +51.94% | $1,068,425.93 |
| DRIFT/USDT:USDT | +35.34% | $1,435,989.06 |
| FOLKS/USDT:USDT | +23.14% | $1,194,267.82 |
| MUBARAK/USDT:USDT | +18.85% | $15,885,131.58 |
| 4/USDT:USDT | +18.60% | $1,982,608.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +2.68% | +2.59% |
| DRIFT/USDT:USDT | below_1h_threshold | +2.57% | +2.48% |
| APT/USDT:USDT | below_1h_threshold | +2.30% | +2.20% |
| FORM/USDT:USDT | below_1h_threshold | +2.21% | +2.11% |
| PENGU/USDT:USDT | below_1h_threshold | +2.16% | +2.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
