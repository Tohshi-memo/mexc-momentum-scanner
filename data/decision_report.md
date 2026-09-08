# Decision Report

- generated_at: 2026-09-08T01:51:30.750217+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13933**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13933, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +4.74% | **+1.19%** |
| LIMIT_7PCT | 5/20 | 25.0% | +4.56% | **+1.14%** |
| LIMIT_ATR | 7/20 | 35.0% | +2.58% | **+0.90%** |
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.03% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.69% | **+2.42%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.70% | **+2.02%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.31% | **+0.69%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +1.98% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$974.61** / 初期 $100.00 (+874.61%)
- 確定: 5206件 (Win 1566 / Loss 1690 / Flat 1950) / skip 5288件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $974.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2572件 (Win 717 / Loss 618 / Flat 1237) / skip 4772件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.95** / 初期 $100.00 (+21.95%)
- 確定: 2523件 (Win 744 / Loss 947 / Flat 832) / pending 6件 / skip 2877件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000393 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BONER/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.95

## 6. Latest Market Context

- 更新: 2026-09-08T01:51:20.632860+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=79300.0
- Funnel: target 1062 → liquid 147 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +37.84% | $6,940,179.57 |
| SOPH/USDT:USDT | +34.70% | $2,260,338.54 |
| BONER/USDT:USDT | +30.51% | $4,364,541.45 |
| AERO/USDT:USDT | +17.67% | $4,234,552.66 |
| INJ/USDT:USDT | +14.13% | $48,023,092.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +3.24% | +3.23% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +3.01% | +2.99% |
| BR/USDT:USDT | below_1h_threshold | +2.88% | +2.86% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +2.80% | +2.78% |
| UNI/USDT:USDT | below_1h_threshold | +2.65% | +2.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
