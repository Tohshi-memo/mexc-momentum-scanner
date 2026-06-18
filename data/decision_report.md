# Decision Report

- generated_at: 2026-06-18T00:41:19.370094+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6985**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6985, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.75% | **-1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +0.46% | **+0.32%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.56% | **+0.22%** |
| LIMIT_8PCT | 7/20 | 35.0% | -0.08% | **-0.03%** |
| LIMIT_7PCT | 7/20 | 35.0% | -1.08% | **-0.38%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.82% | **-0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.99% | **+2.99%** |
| MARKET_LONG | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.03% | **+1.32%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.61% | **+1.21%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.52% | **+1.13%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$208.84** / 初期 $100.00 (+108.84%)
- 確定: 1832件 (Win 505 / Loss 576 / Flat 751) / skip 1714件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $208.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$104.91** / 初期 $100.00 (+4.91%)
- 確定: 258件 (Win 70 / Loss 65 / Flat 123) / skip 138件
- 成長率目線: 平均log +0.000186 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0959 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $104.91

## 5. Latest Market Context

- 更新: 2026-06-18T00:41:14.622072+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64485.2
- Funnel: target 790 → liquid 175 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +130.08% | $24,141,046.05 |
| O/USDT:USDT | +70.22% | $1,493,843.83 |
| SYN/USDT:USDT | +36.38% | $4,279,861.31 |
| H/USDT:USDT | +23.06% | $38,903,011.11 |
| RE/USDT:USDT | +15.91% | $1,855,791.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.35% | +4.34% |
| SIREN/USDT:USDT | below_1h_threshold | +3.80% | +3.79% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +3.67% | +3.66% |
| STG/USDT:USDT | below_1h_threshold | +3.26% | +3.25% |
| US/USDT:USDT | below_1h_threshold | +2.95% | +2.94% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
