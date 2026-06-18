# Decision Report

- generated_at: 2026-06-18T04:44:09.118164+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7004**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7004, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.42% | **+0.11%** |
| LIMIT_5PCT | 7/20 | 35.0% | -0.16% | **-0.06%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.85% | **-0.13%** |
| LIMIT_6PCT | 4/20 | 20.0% | -1.00% | **-0.20%** |
| ASK | 20/20 | 100.0% | -0.36% | **-0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.18% | **+2.18%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.87% | **+0.57%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.77% | **+0.42%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.72% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$216.20** / 初期 $100.00 (+116.20%)
- 確定: 1850件 (Win 516 / Loss 583 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HIGH/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $216.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.85** / 初期 $100.00 (+5.85%)
- 確定: 277件 (Win 77 / Loss 71 / Flat 129) / skip 138件
- 成長率目線: 平均log +0.000205 / 幾何平均 +0.021% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0780 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HIGH/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $105.85

## 5. Latest Market Context

- 更新: 2026-06-18T04:44:02.226490+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.61% price=63860.0
- Funnel: target 792 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +127.82% | $35,251,591.41 |
| O/USDT:USDT | +62.28% | $2,062,447.88 |
| SYN/USDT:USDT | +53.36% | $4,625,424.75 |
| HOME/USDT:USDT | +34.49% | $1,457,400.47 |
| H/USDT:USDT | +29.54% | $33,941,318.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +3.60% | +4.21% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.51% | +4.13% |
| H/USDT:USDT | below_1h_threshold | +3.51% | +4.13% |
| BEAT/USDT:USDT | below_1h_threshold | +3.28% | +3.89% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.97% | +2.59% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
