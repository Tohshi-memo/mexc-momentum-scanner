# Decision Report

- generated_at: 2026-09-08T01:11:20.166703+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13929**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13929, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.66% | **-1.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +4.56% | **+1.14%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_ATR | 7/20 | 35.0% | +2.65% | **+0.93%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.56% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.91% | **+2.47%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.81% | **+1.82%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.76% | **+0.88%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.13% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$968.57** / 初期 $100.00 (+868.57%)
- 確定: 5202件 (Win 1564 / Loss 1688 / Flat 1950) / skip 5288件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $968.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2572件 (Win 717 / Loss 618 / Flat 1237) / skip 4768件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.96** / 初期 $100.00 (+21.96%)
- 確定: 2519件 (Win 743 / Loss 945 / Flat 831) / pending 6件 / skip 2877件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000361 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MEMEROBINHOOD/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $121.96

## 6. Latest Market Context

- 更新: 2026-09-08T01:11:09.983276+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=79306.6
- Funnel: target 1062 → liquid 147 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +39.52% | $6,839,012.89 |
| SOPH/USDT:USDT | +31.43% | $2,185,993.31 |
| BONER/USDT:USDT | +21.56% | $4,170,142.90 |
| AERO/USDT:USDT | +14.30% | $4,138,765.28 |
| INJ/USDT:USDT | +12.33% | $46,047,107.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +3.24% | +3.22% |
| BONER/USDT:USDT | below_1h_threshold | +2.81% | +2.78% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +2.80% | +2.77% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.46% | +2.44% |
| ARB/USDT:USDT | below_1h_threshold | +1.23% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
