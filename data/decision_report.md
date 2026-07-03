# Decision Report

- generated_at: 2026-07-03T04:53:01.097944+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8131**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8131, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.46% | **-0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +0.91% | **+0.82%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.64% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.41% | **+1.13%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.31% | **+1.12%** |
| ASK_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +6.84% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$290.48** / 初期 $100.00 (+190.48%)
- 確定: 2453件 (Win 757 / Loss 817 / Flat 879) / skip 2239件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKHYNIXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $290.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.81** / 初期 $100.00 (+5.81%)
- 確定: 585件 (Win 141 / Loss 138 / Flat 306) / skip 957件
- 成長率目線: 平均log +0.000097 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0261 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYNIXSTOCK/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $105.81

## 5. Latest Market Context

- 更新: 2026-07-03T04:52:53.418050+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=61393.3
- Funnel: target 834 → liquid 168 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +34.04% | $6,218,190.16 |
| ZKP/USDT:USDT | +29.87% | $2,250,658.16 |
| MAGMA/USDT:USDT | +26.44% | $5,744,745.34 |
| THE/USDT:USDT | +20.14% | $2,169,308.40 |
| GUA/USDT:USDT | +20.06% | $10,351,917.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.25% | +4.27% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +4.24% | +4.27% |
| GUA/USDT:USDT | below_1h_threshold | +3.46% | +3.48% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +2.63% | +2.65% |
| US/USDT:USDT | below_1h_threshold | +2.24% | +2.26% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
