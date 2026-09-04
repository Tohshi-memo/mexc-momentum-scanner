# Decision Report

- generated_at: 2026-09-04T20:56:22.912550+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13666**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13666, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.93% | **-0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_BB3S | 4/16 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.99% | **+2.24%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.70% | **+1.76%** |
| MARKET_LONG | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.94% | **+1.55%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.92% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 201件 (TP 75 / SL 121 / EXP 5)
- 最新: UAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5011件 (Win 1516 / Loss 1644 / Flat 1851) / skip 5216件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.38** / 初期 $100.00 (+85.38%)
- 確定: 2422件 (Win 682 / Loss 577 / Flat 1163) / skip 4655件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0655 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.58** / 初期 $100.00 (+18.58%)
- 確定: 2303件 (Win 686 / Loss 882 / Flat 735) / pending 6件 / skip 2834件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000280 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $118.58

## 6. Latest Market Context

- 更新: 2026-09-04T20:56:12.518055+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=79693.8
- Funnel: target 1050 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.6 >= 65=1, 4h RSI 81.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +52.15% | $6,365,763.26 |
| BASECAT/USDT:USDT | +29.26% | $2,050,948.00 |
| USELESS/USDT:USDT | +10.28% | $44,436,035.43 |
| UAI/USDT:USDT | +10.22% | $7,613,499.34 |
| DASH/USDT:USDT | +9.40% | $19,101,720.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DASH/USDT:USDT | below_1h_threshold | +4.76% | +4.84% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.74% | +2.82% |
| KORU/USDT:USDT | below_1h_threshold | +2.57% | +2.65% |
| 1000BONK/USDT:USDT | below_1h_threshold | +2.35% | +2.43% |
| BLESS/USDT:USDT | below_1h_threshold | +2.23% | +2.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
