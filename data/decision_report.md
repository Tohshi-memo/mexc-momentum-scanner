# Decision Report

- generated_at: 2026-06-17T05:57:19.164185+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6908**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6908, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.62% | **-1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.08% | **-0.03%** |
| LIMIT_BB3S | 4/16 | 25.0% | -1.66% | **-0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +5.63% | **+2.82%** |
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| ASK_LONG | 20/20 | 100.0% | +1.67% | **+1.67%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.24% | **+1.57%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +2.07% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$195.87** / 初期 $100.00 (+95.87%)
- 確定: 1781件 (Win 480 / Loss 557 / Flat 744) / skip 1688件
- 成長率目線: 平均log +0.000377 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $195.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.07** / 初期 $100.00 (+0.07%)
- 確定: 181件 (Win 39 / Loss 35 / Flat 107) / skip 138件
- 成長率目線: 平均log +0.000004 / 幾何平均 +0.000% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0871 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $100.07

## 5. Latest Market Context

- 更新: 2026-06-17T05:57:11.125094+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=65741.4
- Funnel: target 785 → liquid 159 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +35.20% | $11,410,483.75 |
| SQD/USDT:USDT | +26.71% | $1,704,291.28 |
| SPX/USDT:USDT | +24.10% | $7,758,897.88 |
| ESPORTS/USDT:USDT | +23.01% | $4,049,018.01 |
| UNI/USDT:USDT | +15.29% | $46,081,914.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +3.41% | +3.58% |
| WLD/USDT:USDT | below_1h_threshold | +2.26% | +2.43% |
| SPACE/USDT:USDT | below_1h_threshold | +2.11% | +2.28% |
| BLESS/USDT:USDT | below_1h_threshold | +1.33% | +1.49% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.19% | +1.36% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
