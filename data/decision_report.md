# Decision Report

- generated_at: 2026-09-09T07:41:28.344698+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14042**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14042, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +0.91% | **+0.73%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.36% | **+0.12%** |
| LIMIT_BB3S | 3/15 | 20.0% | -0.48% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.30% | **+0.14%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.13% | **+0.09%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | -0.06% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,001.99** / 初期 $100.00 (+901.99%)
- 確定: 5306件 (Win 1592 / Loss 1711 / Flat 2003) / skip 5297件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAY/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,001.99

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.26** / 初期 $100.00 (+90.26%)
- 確定: 2645件 (Win 728 / Loss 623 / Flat 1294) / skip 4808件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0068 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RAY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $190.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.81** / 初期 $100.00 (+17.81%)
- 確定: 2618件 (Win 764 / Loss 1000 / Flat 854) / pending 2件 / skip 2894件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000170 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $117.81

## 6. Latest Market Context

- 更新: 2026-09-09T07:41:17.608787+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=79196.2
- Funnel: target 1064 → liquid 161 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.7 >= 65=1, 4h RSI 88.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +70.42% | $1,272,228.97 |
| IOST/USDT:USDT | +26.77% | $2,815,296.53 |
| RAY/USDT:USDT | +19.12% | $4,657,285.80 |
| OL/USDT:USDT | +18.00% | $2,220,862.91 |
| CNPY/USDT:USDT | +15.56% | $1,057,186.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +4.79% | +4.70% |
| CNPY/USDT:USDT | below_1h_threshold | +2.68% | +2.60% |
| CATE/USDT:USDT | below_1h_threshold | +2.59% | +2.50% |
| WAVES/USDT:USDT | below_1h_threshold | +2.50% | +2.41% |
| NEAR/USDT:USDT | below_1h_threshold | +1.96% | +1.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
