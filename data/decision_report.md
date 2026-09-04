# Decision Report

- generated_at: 2026-09-04T20:31:35.978731+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13663**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13663, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.93% | **-0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.81% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_BB3S | 3/15 | 20.0% | +0.77% | **+0.15%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.10% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +3.53% | **+2.83%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.78% | **+1.16%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.24% | **+1.06%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.79% | **+0.98%** |
| MARKET_LONG | 20/20 | 100.0% | +0.93% | **+0.93%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 201件 (TP 75 / SL 121 / EXP 5)
- 最新: UAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5011件 (Win 1516 / Loss 1644 / Flat 1851) / skip 5213件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.38** / 初期 $100.00 (+85.38%)
- 確定: 2422件 (Win 682 / Loss 577 / Flat 1163) / skip 4652件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0318 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.18** / 初期 $100.00 (+18.18%)
- 確定: 2301件 (Win 684 / Loss 882 / Flat 735) / pending 5件 / skip 2834件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000265 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $118.18

## 6. Latest Market Context

- 更新: 2026-09-04T20:31:25.571167+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=79733.6
- Funnel: target 1050 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.1 >= 65=1, 4h RSI 67.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +51.21% | $5,702,622.50 |
| BASECAT/USDT:USDT | +18.31% | $1,833,751.84 |
| UAI/USDT:USDT | +12.24% | $7,428,396.58 |
| MARSCOIN/USDT:USDT | +10.04% | $8,146,508.07 |
| USELESS/USDT:USDT | +9.57% | $44,230,264.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.74% | +2.77% |
| EDGE/USDT:USDT | below_1h_threshold | +2.63% | +2.66% |
| KORU/USDT:USDT | below_1h_threshold | +2.57% | +2.60% |
| TUT/USDT:USDT | below_1h_threshold | +2.42% | +2.45% |
| MUU/USDT:USDT | below_1h_threshold | +2.02% | +2.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
