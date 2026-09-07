# Decision Report

- generated_at: 2026-09-07T23:46:18.567734+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13923**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13923, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.66% | **-1.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 10/20 | 50.0% | +2.57% | **+1.29%** |
| LIMIT_7PCT | 5/20 | 25.0% | +4.56% | **+1.14%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.35% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.03% | **+2.73%** |
| MARKET_LONG | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.69% | **+1.61%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +3.82% | **+0.96%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.84% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$949.24** / 初期 $100.00 (+849.24%)
- 確定: 5196件 (Win 1560 / Loss 1687 / Flat 1949) / skip 5288件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $949.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2572件 (Win 717 / Loss 618 / Flat 1237) / skip 4762件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.75** / 初期 $100.00 (+21.75%)
- 確定: 2513件 (Win 741 / Loss 943 / Flat 829) / pending 4件 / skip 2877件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000315 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MEMEROBINHOOD/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $121.75

## 6. Latest Market Context

- 更新: 2026-09-07T23:46:08.553102+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=79083.5
- Funnel: target 1062 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +37.24% | $6,433,389.34 |
| BONER/USDT:USDT | +17.32% | $5,050,566.08 |
| SOPH/USDT:USDT | +15.87% | $1,779,459.00 |
| AERO/USDT:USDT | +9.92% | $3,875,694.38 |
| INJ/USDT:USDT | +9.06% | $44,039,542.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.70% | +3.49% |
| BR/USDT:USDT | below_1h_threshold | +2.40% | +2.19% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.82% | +1.61% |
| INJ/USDT:USDT | below_1h_threshold | +1.80% | +1.59% |
| PEPE/USDT:USDT | below_1h_threshold | +1.42% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
