# Decision Report

- generated_at: 2026-07-03T05:31:02.666487+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8133**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8133, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.14% | **+0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.46% | **+1.31%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.66% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +6.84% | **+0.68%** |
| ASK_LONG | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.08% | **+0.49%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.51% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$289.03** / 初期 $100.00 (+189.03%)
- 確定: 2455件 (Win 757 / Loss 818 / Flat 880) / skip 2239件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NOM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $289.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.44** / 初期 $100.00 (+5.44%)
- 確定: 587件 (Win 141 / Loss 139 / Flat 307) / skip 957件
- 成長率目線: 平均log +0.000090 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0356 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NOM/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $105.44

## 5. Latest Market Context

- 更新: 2026-07-03T05:30:55.615127+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.33% price=61620.5
- Funnel: target 834 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +38.67% | $6,274,415.35 |
| ZKP/USDT:USDT | +29.19% | $2,566,360.99 |
| MAGMA/USDT:USDT | +27.58% | $6,103,980.76 |
| GUA/USDT:USDT | +25.08% | $10,112,673.07 |
| THE/USDT:USDT | +18.49% | $2,202,368.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOM/USDT:USDT | below_1h_threshold | +3.42% | +3.09% |
| GUA/USDT:USDT | below_1h_threshold | +2.90% | +2.57% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.82% | +2.50% |
| LIT/USDT:USDT | below_1h_threshold | +2.45% | +2.12% |
| BLESS/USDT:USDT | below_1h_threshold | +2.25% | +1.93% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
