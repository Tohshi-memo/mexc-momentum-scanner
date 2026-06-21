# Decision Report

- generated_at: 2026-06-21T01:51:15.229288+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7286**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7286, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.86% | **-0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.05% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.81% | **+1.97%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.41% | **+1.33%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +1.64% | **+1.23%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.95% | **+1.07%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.65% | **+1.06%** |

## 2. $100 Live Portfolio

- 残高: **$102.46** / 初期 $100.00 (+2.46%)
- 確定トレード: 25件 (TP 10 / SL 15 / EXP 0)
- 最新: AGT/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.46
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$237.39** / 初期 $100.00 (+137.39%)
- 確定: 2015件 (Win 597 / Loss 660 / Flat 758) / skip 1832件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SLX/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $237.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 387件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0288 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-21T01:51:10.049996+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64238.0
- Funnel: target 796 → liquid 134 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.4 >= 65=1, 4h RSI 85.8 >= 65=1, 4h RSI 67.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +47.72% | $49,060,085.42 |
| ALICE/USDT:USDT | +41.81% | $2,840,234.41 |
| RESOLV/USDT:USDT | +27.65% | $3,460,820.92 |
| VELVET/USDT:USDT | +10.15% | $16,989,394.15 |
| SLX/USDT:USDT | +9.71% | $1,790,439.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +2.86% | +2.90% |
| RIF/USDT:USDT | below_1h_threshold | +2.57% | +2.61% |
| JTO/USDT:USDT | below_1h_threshold | +2.08% | +2.12% |
| RESOLV/USDT:USDT | below_1h_threshold | +1.48% | +1.52% |
| JUP/USDT:USDT | below_1h_threshold | +1.27% | +1.31% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
