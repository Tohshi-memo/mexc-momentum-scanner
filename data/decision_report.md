# Decision Report

- generated_at: 2026-07-07T21:20:42.928415+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8454**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8454, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.67% | **+0.67%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.20% | **+0.07%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.08% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.11% | **+0.67%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.51% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$101.56** / 初期 $100.00 (+1.56%)
- 確定トレード: 70件 (TP 24 / SL 45 / EXP 1)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.56
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$320.92** / 初期 $100.00 (+220.92%)
- 確定: 2659件 (Win 846 / Loss 897 / Flat 916) / skip 2356件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.14% 残高後 $320.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 640件 (Win 152 / Loss 158 / Flat 330) / skip 1225件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0338 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-07T21:20:37.654706+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=63526.1
- Funnel: target 847 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +27.13% | $41,512,279.56 |
| EDGE/USDT:USDT | +14.09% | $12,009,149.60 |
| PENGSTOCK/USDT:USDT | +8.45% | $1,309,088.82 |
| US/USDT:USDT | +7.10% | $13,230,514.40 |
| SPELL/USDT:USDT | +4.74% | $1,974,652.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +1.08% | +1.30% |
| SYN/USDT:USDT | below_1h_threshold | +0.97% | +1.19% |
| LUNC/USDT:USDT | below_1h_threshold | +0.89% | +1.12% |
| UAI/USDT:USDT | below_1h_threshold | +0.81% | +1.03% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.46% | +0.69% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
